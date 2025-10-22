from typing import Type

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import (
    PIIEntity,
    PIIExtractionOutput
)
from src.parsers.xml_tag_parser import parse_list_of_objects
from src.prompts.pii_extraction_prompt import get_instructions, get_task


class PIIExtractionAgent(AgentNodeBase[QueryInput, PIIExtractionOutput]):
    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.1,
            max_tokens=1500
        )
        # Set the system prompt from the prompt file
        self.system_prompt = get_instructions()

    def parse_response(self, llm_response: str) -> PIIExtractionOutput:
        """Parse the LLM response to extract PII entities"""
        # Extract entities from the response
        entities_data = parse_list_of_objects(
            xml_string=llm_response,
            object_tag="entity",
            field_tags=["type", "value"]
        )

        # Convert to Pydantic models
        # Note: The prompt outputs UPPERCASE types (e.g., CARD_NUMBER, CVV)
        # but we normalize to lowercase for consistency
        entities = []
        for entity in entities_data:
            # Normalize type to lowercase
            entity_type = entity.get("type", "").lower()
            entity_value = entity.get("value", "")

            # Create PIIEntity with normalized type
            entities.append(
                PIIEntity(type=entity_type, value=entity_value)
            )

        return PIIExtractionOutput(
            entities=entities,
            raw_response=llm_response
        )

    def get_input_model(self) -> Type[QueryInput]:
        """Return the Pydantic model class for the input"""
        return QueryInput

    def get_output_model(self) -> Type[PIIExtractionOutput]:
        """Return the Pydantic model class for the output"""
        return PIIExtractionOutput

    def format_user_prompt(self, input_data: QueryInput) -> str:
        """Format the input data into a user prompt for the LLM"""
        return get_task(input_data.query)
