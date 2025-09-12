"""
Complete example demonstrating the simplified evaluation framework.

This example shows how to:
1. Create a simple agent node
2. Define test cases with different validation methods
3. Run evaluations
4. Interpret results
"""

import asyncio
from typing import Dict, Any, Optional
from dataclasses import dataclass

# Import framework components
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from scratchpad.evals.core import EvalCase
from scratchpad.evals.context import ConversationContext
from scratchpad.evals.runner import EvalRunner


# Example LLM Client (mock implementation for demo)
class MockLLMClient:
    """Mock LLM client for demonstration purposes."""
    
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1000
    ) -> str:
        """Mock LLM generation."""
        # Simple rule-based responses for demo
        query_lower: str = user_prompt.lower()
        
        # Classification logic
        if "what is" in query_lower or "explain" in query_lower:
            return "CONCEPTUAL"
        elif "how do i" in query_lower or "how to" in query_lower:
            return "PROCEDURAL"
        elif "where" in query_lower:
            return "NAVIGATION"
        elif "can i" in query_lower or "is it possible" in query_lower:
            return "CAPABILITY"
        elif "not working" in query_lower or "error" in query_lower:
            return "TROUBLESHOOTING"
        elif any(word in query_lower for word in ["valid", "correct", "right"]):
            return "true"
        elif any(word in query_lower for word in ["invalid", "wrong", "incorrect"]):
            return "false"
        else:
            return "AMBIGUOUS"


# Example Agent Node
class QueryClassificationAgent:
    """
    Example agent node that classifies user queries.
    
    This demonstrates the pattern expected by the evaluation framework.
    """
    
    def __init__(self, llm_client: Any, model_name: Optional[str] = None):
        """Initialize the agent with an LLM client."""
        self.llm_client: Any = llm_client
        self.model_name: Optional[str] = model_name or "default"
        self.node_name: str = "QueryClassificationAgent"
    
    
    async def process(self, context: ConversationContext) -> ConversationContext:
        """
        Process the conversation context and classify the query.
        
        Args:
            context: Conversation context with query
            
        Returns:
            Updated context with classification result
        """
        # Extract query
        query: str = context.query
        
        # Generate classification using LLM
        system_prompt: str = """You are a query classifier. Classify the user query into one of these categories:
        - CONCEPTUAL: What is, explain, define
        - PROCEDURAL: How to, steps to
        - NAVIGATION: Where is, find location
        - CAPABILITY: Can I, is it possible
        - TROUBLESHOOTING: Not working, error, issue
        - AMBIGUOUS: Unclear or needs context
        
        Respond with just the category name."""
        
        classification: str = await self.llm_client.generate(
            system_prompt=system_prompt,
            user_prompt=f"Classify this query: {query}",
            temperature=0.1,
            max_tokens=50
        )
        
        # Store result in context
        context.update_workflow_node(
            self.node_name,
            query_type=classification.strip(),
            original_query=query,
            confidence=0.95  # Mock confidence
        )
        
        return context


class ValidityCheckAgent:
    """Another example agent that checks if input is valid."""
    
    def __init__(self, llm_client: Any, model_name: Optional[str] = None):
        """Initialize the agent."""
        self.llm_client: Any = llm_client
        self.node_name: str = "ValidityCheckAgent"
    
    
    async def process(self, context: ConversationContext) -> ConversationContext:
        """Check if the query is valid."""
        query: str = context.query
        
        # Simple validation logic
        response: str = await self.llm_client.generate(
            system_prompt="Determine if the input is valid. Respond with 'true' or 'false'.",
            user_prompt=query,
            temperature=0.1,
            max_tokens=10
        )
        
        is_valid: bool = response.strip().lower() == "true"
        
        context.update_workflow_node(
            self.node_name,
            valid=is_valid,
            reason="Query contains valid content" if is_valid else "Query is invalid"
        )
        
        return context


async def run_classification_example():
    """Run query classification evaluation example."""
    print("\n" + "=" * 60)
    print("QUERY CLASSIFICATION EVALUATION EXAMPLE")
    print("=" * 60)
    
    # Initialize LLM client
    llm_client = MockLLMClient()
    
    # Define test cases
    test_cases = [
        # String validation - exact match
        EvalCase(
            name="conceptual_query",
            input_data={"query": "What is machine learning?"},
            expected_output="CONCEPTUAL",
            description="Should classify 'what is' questions as CONCEPTUAL"
        ),
        
        # Multi-choice validation - multiple valid answers
        EvalCase(
            name="ambiguous_how_query",
            input_data={"query": "How do I use this feature?"},
            expected_output=["PROCEDURAL", "CAPABILITY"],
            description="'How do I' could be procedural or capability question"
        ),
        
        # String validation
        EvalCase(
            name="navigation_query",
            input_data={"query": "Where can I find the settings?"},
            expected_output="NAVIGATION",
            description="'Where' questions should be NAVIGATION"
        ),
        
        # Edge case
        EvalCase(
            name="troubleshooting_query",
            input_data={"query": "The export is not working"},
            expected_output="TROUBLESHOOTING",
            description="Problem descriptions should be TROUBLESHOOTING"
        ),
        
        # This one will fail (for demo)
        EvalCase(
            name="complex_query",
            input_data={"query": "Is quantum computing the future?"},
            expected_output="CONCEPTUAL",  # Will actually return CAPABILITY
            description="Complex philosophical question"
        ),
    ]
    
    # Initialize runner
    runner = EvalRunner(
        agent_class=QueryClassificationAgent,
        llm_client=llm_client,
        default_field_name="query_type"  # Tell runner which field to validate
    )
    
    # Run evaluations
    print("\nRunning evaluations...")
    results = await runner.run_batch(test_cases, parallel=False)
    
    # Print results
    runner.print_summary(results)
    
    return results


async def run_validity_example():
    """Run validity check evaluation example."""
    print("\n" + "=" * 60)
    print("VALIDITY CHECK EVALUATION EXAMPLE")
    print("=" * 60)
    
    # Initialize LLM client
    llm_client = MockLLMClient()
    
    # Define test cases with boolean validation
    test_cases = [
        EvalCase(
            name="valid_query",
            input_data={"query": "This is a valid question"},
            expected_output=True,
            description="Normal query should be valid"
        ),
        
        EvalCase(
            name="invalid_query",
            input_data={"query": "This is wrong and incorrect"},
            expected_output=False,
            description="Query with 'wrong' should be invalid"
        ),
        
        EvalCase(
            name="check_correctness",
            input_data={"query": "Is this the right approach?"},
            expected_output=True,
            description="Query with 'right' should be valid"
        ),
    ]
    
    # Initialize runner
    runner = EvalRunner(
        agent_class=ValidityCheckAgent,
        llm_client=llm_client,
        default_field_name="valid"  # Boolean field
    )
    
    # Run evaluations
    print("\nRunning evaluations...")
    results = await runner.run_batch(test_cases)
    
    # Print results
    runner.print_summary(results)
    
    return results


async def run_criteria_example():
    """
    Run example with LLM-as-a-Judge criteria validation.
    
    Note: This would require a real LLM client for proper evaluation.
    """
    print("\n" + "=" * 60)
    print("CRITERIA-BASED EVALUATION EXAMPLE")
    print("=" * 60)
    
    print("\nNote: Criteria-based evaluation requires a real LLM client.")
    print("This example shows how to define test cases with semantic criteria:\n")
    
    # Example test case with criteria
    example_case = EvalCase(
        name="response_quality",
        input_data={
            "query": "Explain how neural networks work",
            "context": "User is a beginner in machine learning"
        },
        criteria=[
            "The explanation uses simple, non-technical language",
            "Core concepts (neurons, layers, weights) are mentioned",
            "An analogy or example is provided",
            "The explanation is under 200 words"
        ],
        description="Should provide beginner-friendly explanation"
    )
    
    print(f"Test case: {example_case.name}")
    print(f"Description: {example_case.description}")
    print("\nCriteria for evaluation:")
    for i, criterion in enumerate(example_case.criteria, 1):
        print(f"  {i}. {criterion}")
    
    print("\nWith a real LLM client, this would evaluate if the generated")
    print("explanation meets ALL the specified criteria.")


async def main():
    """Run all examples."""
    # Run classification example
    classification_results = await run_classification_example()
    
    # Run validity example
    validity_results = await run_validity_example()
    
    # Show criteria example
    await run_criteria_example()
    
    print("\n" + "=" * 60)
    print("EXAMPLE COMPLETE")
    print("=" * 60)
    print("\nThis demonstration showed:")
    print("1. String validation (exact match)")
    print("2. Multi-choice validation (multiple valid answers)")
    print("3. Boolean validation")
    print("4. How to define criteria-based tests")
    print("\nThe framework is simple, flexible, and easy to extend!")


if __name__ == "__main__":
    # Run the examples
    asyncio.run(main())