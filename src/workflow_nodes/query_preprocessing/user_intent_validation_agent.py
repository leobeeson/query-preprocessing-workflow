from typing import Type

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.entity_extraction_models import UserIntentValidationOutput
from src.parsers.xml_tag_parser import get_xml_tag_content, parse_boolean_tag
from src.prompts.user_intent_validation_prompt import get_instructions, get_task


class UserIntentValidationAgent(AgentNodeBase):
    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.1,
            max_tokens=500  # Much smaller output expected
        )
        # Set the prompts from the prompt file
        self.set_prompts(
            system_prompt=get_instructions(),
            task_prompt=get_task("{query}")  # Template will be filled by base class
        )
    
    def parse_response(self, llm_response: str) -> UserIntentValidationOutput:
        """Parse the LLM response to extract validation result"""
        # Extract the valid field as boolean
        valid = parse_boolean_tag(llm_response, "valid")
        
        # Extract the justification
        justification = get_xml_tag_content(llm_response, "justification")
        
        # If justification is empty, provide a default
        if not justification:
            justification = "Valid query" if valid else "Invalid query"
        
        return UserIntentValidationOutput(
            valid=valid,
            justification=justification,
            raw_response=llm_response
        )
    
    def get_output_model(self) -> Type[UserIntentValidationOutput]:
        """Return the Pydantic model class for the output"""
        return UserIntentValidationOutput