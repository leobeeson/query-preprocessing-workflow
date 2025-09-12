from typing import Type, Literal, cast

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.entity_extraction_models import (
    ProcessableEntity,
    ProcessableEntityExtractionOutput
)
from src.parsers.xml_tag_parser import parse_list_of_objects
from src.prompts.processable_entity_extraction_prompt import get_instructions, get_task


class ProcessableEntityExtractionAgent(AgentNodeBase):
    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.1,
            max_tokens=1500
        )
        # Set the prompts from the prompt file
        self.set_prompts(
            system_prompt=get_instructions(),
            task_prompt=get_task("{query}")  # Template will be filled by base class
        )
    
    def parse_response(self, llm_response: str) -> ProcessableEntityExtractionOutput:
        """Parse the LLM response to extract entities"""
        # Extract entities from the response
        entities_data = parse_list_of_objects(
            xml_string=llm_response,
            object_tag="entity",
            field_tags=["type", "value"]
        )
        
        # Convert to Pydantic models with validation
        entities = []
        valid_types = ["temporal", "category", "merchant", "amount", "environmental"]
        for entity in entities_data:
            # Validate entity type and skip invalid ones
            entity_type = entity.get("type", "").lower()
            if entity_type in valid_types:
                # Cast to the correct Literal type
                typed_entity_type = cast(
                    Literal["temporal", "category", "merchant", "amount", "environmental"],
                    entity_type
                )
                entities.append(
                    ProcessableEntity(type=typed_entity_type, value=entity.get("value", ""))
                )
        
        return ProcessableEntityExtractionOutput(
            entities=entities,
            raw_response=llm_response
        )
    
    def get_output_model(self) -> Type[ProcessableEntityExtractionOutput]:
        """Return the Pydantic model class for the output"""
        return ProcessableEntityExtractionOutput
