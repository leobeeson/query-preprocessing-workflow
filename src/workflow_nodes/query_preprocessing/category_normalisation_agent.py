from typing import Type

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.category_normalisation_models import (
    CategoryNormalisationInput,
    CategoryNormalisationOutput,
    NormalisedCategoryEntity
)
from src.parsers.xml_tag_parser import parse_list_of_objects
from src.prompts.category_normalisation_prompt import get_instructions, get_task


class CategoryNormalisationAgent(AgentNodeBase):
    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.1,
            max_tokens=1000
        )
        # Set only the system prompt here, task prompt will be built dynamically
        self.system_prompt = get_instructions()
    
    async def process(self, input_data: CategoryNormalisationInput) -> CategoryNormalisationOutput:
        """
        Process category entities for normalisation.
        Overrides base process method to handle structured input.
        """
        # Build the entities XML string from the input
        entities_xml = ""
        for entity in input_data.entities:
            entities_xml += f"""<entity>
<type>{entity.type}</type>
<value>{entity.value}</value>
</entity>
"""
        
        # Build the task prompt with query and entities
        task_prompt = get_task(input_data.query, entities_xml.strip())
        
        # Call LLM with the prompts
        llm_response = await self.llm_client.generate(
            system_prompt=self.system_prompt,
            user_prompt=task_prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        # Parse and return the response
        return self.parse_response(llm_response)
    
    def parse_response(self, llm_response: str) -> CategoryNormalisationOutput:
        """Parse the LLM response to extract normalised categories"""
        # Extract entities from the response
        entities_data = parse_list_of_objects(
            xml_string=llm_response,
            object_tag="entity",
            field_tags=["type", "value", "canon"]
        )
        
        # Convert to Pydantic models
        normalised_entities = [
            NormalisedCategoryEntity(
                type=entity.get("type", "category"),
                value=entity.get("value", ""),
                canon=entity.get("canon", "")
            )
            for entity in entities_data
        ]
        
        return CategoryNormalisationOutput(
            entities=normalised_entities,
            raw_response=llm_response
        )
    
    def get_output_model(self) -> Type[CategoryNormalisationOutput]:
        """Return the Pydantic model class for the output"""
        return CategoryNormalisationOutput