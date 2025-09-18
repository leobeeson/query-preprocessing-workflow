from typing import Type, Literal, cast

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import (
    UnprocessableEntity,
    UnprocessableEntityExtractionOutput
)
from src.parsers.xml_tag_parser import parse_list_of_objects
from src.prompts.unprocessable_entity_extraction_prompt import get_instructions, get_task


class UnprocessableEntityExtractionAgent(AgentNodeBase[QueryInput, UnprocessableEntityExtractionOutput]):
    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.1,
            max_tokens=1500
        )
        # Set the system prompt from the prompt file
        self.system_prompt = get_instructions()
    
    def parse_response(self, llm_response: str) -> UnprocessableEntityExtractionOutput:
        """Parse the LLM response to extract unprocessable entities"""
        # Extract entities from the response
        entities_data = parse_list_of_objects(
            xml_string=llm_response,
            object_tag="entity",
            field_tags=["type", "value", "critical"]
        )
        
        # Convert to Pydantic models with validation
        entities = []
        standard_types = [
            "geographic", 
            "payment_method", 
            "person_recipient",
            "transaction_channel",
            "product_service",
            "bank_reference",
            "financial_product",
            "transaction_status",
            "account"
        ]
        
        for entity in entities_data:
            entity_type = entity.get("type", "").lower().replace("_", " ").replace("-", " ")
            # Normalize type to match our enum
            if "payment" in entity_type and "method" in entity_type:
                entity_type = "payment_method"
            elif "person" in entity_type or "recipient" in entity_type:
                entity_type = "person_recipient"
            elif "transaction" in entity_type and "channel" in entity_type:
                entity_type = "transaction_channel"
            elif "product" in entity_type or "service" in entity_type:
                entity_type = "product_service"
            elif "bank" in entity_type:
                entity_type = "bank_reference"
            elif "financial" in entity_type:
                entity_type = "financial_product"
            elif "transaction" in entity_type and "status" in entity_type:
                entity_type = "transaction_status"
            elif "geographic" in entity_type or entity_type in ["geographic"]:
                entity_type = "geographic"
            
            # Check if it's a standard type we support
            if entity_type in standard_types:
                typed_entity_type = cast(
                    Literal[
                        "geographic", 
                        "payment_method", 
                        "person_recipient",
                        "transaction_channel",
                        "product_service",
                        "bank_reference",
                        "financial_product",
                        "transaction_status",
                        "account"
                    ],
                    entity_type
                )
                
                # Parse critical as boolean
                critical_str = entity.get("critical", "true").lower()
                critical = critical_str in ["true", "yes", "1"]
                
                entities.append(
                    UnprocessableEntity(
                        type=typed_entity_type,
                        value=entity.get("value", ""),
                        critical=critical
                    )
                )
            # Skip dynamic types that don't match our schema for now
        
        return UnprocessableEntityExtractionOutput(
            entities=entities,
            raw_response=llm_response
        )
    
    def get_input_model(self) -> Type[QueryInput]:
        """Return the Pydantic model class for the input"""
        return QueryInput

    def get_output_model(self) -> Type[UnprocessableEntityExtractionOutput]:
        """Return the Pydantic model class for the output"""
        return UnprocessableEntityExtractionOutput

    def format_user_prompt(self, input_data: QueryInput) -> str:
        """Format the input data into a user prompt for the LLM"""
        return get_task(input_data.query)