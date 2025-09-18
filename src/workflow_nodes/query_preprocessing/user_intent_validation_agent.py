from typing import Type

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import UserIntentValidationOutput
from src.parsers.xml_tag_parser import get_xml_tag_content, parse_boolean_tag
from src.prompts.user_intent_validation_prompt import get_instructions, get_task


class UserIntentValidationAgent(AgentNodeBase[QueryInput, UserIntentValidationOutput]):
    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.1,
            max_tokens=500  # Much smaller output expected
        )
        # Set the system prompt from the prompt file
        self.system_prompt = get_instructions()
    
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
    
    def get_input_model(self) -> Type[QueryInput]:
        """Return the Pydantic model class for the input"""
        return QueryInput

    def get_output_model(self) -> Type[UserIntentValidationOutput]:
        """Return the Pydantic model class for the output"""
        return UserIntentValidationOutput

    def format_user_prompt(self, input_data: QueryInput) -> str:
        """Format the input data into a user prompt for the LLM"""
        return get_task(input_data.query)