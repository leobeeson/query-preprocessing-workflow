"""
Query Preprocessing Workflow
Orchestrates multiple agents to validate and extract entities from user queries
"""

import asyncio
from typing import Dict, Any, Optional, List
from dataclasses import dataclass
from datetime import datetime

from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.llm_metrics import LLMMetrics

# Import agents
from src.workflow_nodes.query_preprocessing.processable_entity_extraction_agent import ProcessableEntityExtractionAgent
from src.workflow_nodes.query_preprocessing.unprocessable_entity_extraction_agent import UnprocessableEntityExtractionAgent
from src.workflow_nodes.query_preprocessing.user_intent_validation_agent import UserIntentValidationAgent
from src.workflow_nodes.query_preprocessing.query_security_validation_agent import QuerySecurityValidationAgent
from src.workflow_nodes.query_preprocessing.category_normalisation_agent import CategoryNormalisationAgent

# Import models
from src.models.entity_extraction_models import ProcessableEntity
from src.models.category_normalisation_models import CategoryNormalisationInput, CategoryEntity

# Import exceptions
from src.workflows.exceptions import (
    InsecureQueryError,
    InvalidQueryError,
    UnprocessableEntityError,
    NoProcessableEntitiesError
)


@dataclass
class WorkflowResult:
    """Result from the query preprocessing workflow"""
    query: str
    processable_entities: List[ProcessableEntity]
    normalised_categories: List[Any]
    unprocessable_entities: List[Any]
    is_secure: bool
    is_valid: bool
    metrics: Dict[str, LLMMetrics]
    total_time_ms: float
    
    def get_total_cost(self) -> float:
        """Calculate total cost across all agents"""
        return sum(m.total_cost for m in self.metrics.values())


class QueryPreprocessingWorkflow:
    """
    Workflow that processes user queries through multiple validation and extraction agents.
    
    Flow:
    1. Run 4 agents concurrently: processable extraction, security validation, 
       unprocessable extraction, user intent validation
    2. Check results in order for early termination
    3. Run category normalisation if processable entities exist
    """
    
    def __init__(self, llm_client: LLMClientInterface):
        """
        Initialize the workflow with all required agents.
        
        Args:
            llm_client: The LLM client to use for all agents
        """
        self.llm_client = llm_client
        
        # Initialize all agents
        self.processable_agent = ProcessableEntityExtractionAgent(llm_client)
        self.unprocessable_agent = UnprocessableEntityExtractionAgent(llm_client)
        self.security_agent = QuerySecurityValidationAgent(llm_client)
        self.intent_agent = UserIntentValidationAgent(llm_client)
        self.category_agent = CategoryNormalisationAgent(llm_client)
    
    async def process(self, query: str) -> WorkflowResult:
        """
        Process a query through all validation and extraction steps.
        
        Args:
            query: The user query to process
            
        Returns:
            WorkflowResult containing all extracted entities and metadata
            
        Raises:
            InsecureQueryError: If query fails security validation
            InvalidQueryError: If query fails intent validation
            UnprocessableEntityError: If query has critical unprocessable entities
            NoProcessableEntitiesError: If no processable entities found
        """
        start_time = datetime.now()
        metrics = {}
        
        # Step 1: Run 4 agents concurrently
        # Import QueryInput for agents that need it
        from src.models.base_models import QueryInput

        # Create input for agents
        query_input = QueryInput(query=query)

        results = await asyncio.gather(
            self.processable_agent.process(query_input),
            self.security_agent.process(query_input),
            self.unprocessable_agent.process(query_input),
            self.intent_agent.process(query_input),
            return_exceptions=False  # Let exceptions propagate
        )
        
        # Unpack results
        processable_result = results[0]
        security_result = results[1]
        unprocessable_result = results[2]
        intent_result = results[3]
        
        # Collect metrics
        if self.processable_agent.last_metrics:
            metrics["processable_extraction"] = self.processable_agent.last_metrics
        if self.security_agent.last_metrics:
            metrics["security_validation"] = self.security_agent.last_metrics
        if self.unprocessable_agent.last_metrics:
            metrics["unprocessable_extraction"] = self.unprocessable_agent.last_metrics
        if self.intent_agent.last_metrics:
            metrics["intent_validation"] = self.intent_agent.last_metrics
        
        # Step 2: Check results in specified order
        
        # 2.1: Check security validation
        if not security_result.valid:
            raise InsecureQueryError(
                message="Query failed security validation",
                justification=security_result.justification
            )
        
        # 2.2: Check user intent validation
        if not intent_result.valid:
            raise InvalidQueryError(
                message="Query is invalid for banking domain",
                justification=intent_result.justification
            )
        
        # 2.3: Check for critical unprocessable entities
        critical_unprocessable = [
            entity for entity in unprocessable_result.entities
            if entity.critical
        ]
        if critical_unprocessable:
            raise UnprocessableEntityError(
                message="Query contains critical unprocessable entities",
                entities=critical_unprocessable
            )
        
        # 2.4: Check for processable entities
        if not processable_result.entities:
            raise NoProcessableEntitiesError()
        
        # Step 3: Run category normalisation for category entities
        normalised_categories = []
        category_entities = [
            entity for entity in processable_result.entities
            if entity.type == "category"
        ]
        
        if category_entities:
            # Create input for category normalisation
            category_input = CategoryNormalisationInput(
                query=query,
                entities=[
                    CategoryEntity(type="category", value=entity.value)
                    for entity in category_entities
                ]
            )
            
            # Run category normalisation
            category_result = await self.category_agent.process(category_input)
            normalised_categories = category_result.entities
            
            # Add metrics
            if self.category_agent.last_metrics:
                metrics["category_normalisation"] = self.category_agent.last_metrics
        
        # Calculate total time
        end_time = datetime.now()
        total_time_ms = (end_time - start_time).total_seconds() * 1000
        
        # Build and return result
        return WorkflowResult(
            query=query,
            processable_entities=processable_result.entities,
            normalised_categories=normalised_categories,
            unprocessable_entities=unprocessable_result.entities,
            is_secure=security_result.valid,
            is_valid=intent_result.valid,
            metrics=metrics,
            total_time_ms=total_time_ms
        )
    
    def get_workflow_summary(self, result: WorkflowResult) -> str:
        """
        Generate a human-readable summary of the workflow result.
        
        Args:
            result: The workflow result to summarize
            
        Returns:
            Formatted string summary
        """
        lines = [
            "=" * 60,
            "QUERY PREPROCESSING RESULT",
            "=" * 60,
            f"Query: {result.query}",
            f"Security: {'✅ Secure' if result.is_secure else '❌ Insecure'}",
            f"Validity: {'✅ Valid' if result.is_valid else '❌ Invalid'}",
            f"\nProcessable Entities ({len(result.processable_entities)}):"
        ]
        
        for entity in result.processable_entities:
            lines.append(f"  • {entity.type}: {entity.value}")
        
        if result.normalised_categories:
            lines.append(f"\nNormalised Categories ({len(result.normalised_categories)}):")
            for cat in result.normalised_categories:
                lines.append(f"  • {cat.value} → {cat.canon}")
        
        if result.unprocessable_entities:
            lines.append(f"\nUnprocessable Entities ({len(result.unprocessable_entities)}):")
            for entity in result.unprocessable_entities:
                critical_marker = "🔴" if entity.critical else "🟡"
                lines.append(f"  {critical_marker} {entity.type}: {entity.value}")
        
        lines.extend([
            f"\nPerformance:",
            f"  Total Time: {result.total_time_ms:.0f}ms",
            f"  Total Cost: ${result.get_total_cost():.6f}",
            f"  Agents Run: {len(result.metrics)}",
            "=" * 60
        ])
        
        return "\n".join(lines)