from abc import ABC, abstractmethod
from typing import Type, TypeVar
from pydantic import BaseModel

from src.clients.llm_clients.llm_client_interface import LLMClientInterface

T = TypeVar('T', bound=BaseModel)


class AgentNodeBase(ABC):
      
    def __init__(
        self,
        llm_client: LLMClientInterface,
        model_name: str = "default",
        temperature: float = 0.1,
        max_tokens: int = 1000
    ):
        self.llm_client = llm_client
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens


    def set_prompts(self, system_prompt: str, task_prompt: str) -> None:
        self.system_prompt: str = system_prompt
        self.task_prompt: str = task_prompt


    @abstractmethod
    def parse_response(self, llm_response: str) -> BaseModel:
        """Parse the LLM response into a Pydantic model"""
        pass
    
    @abstractmethod
    def get_output_model(self) -> Type[BaseModel]:
        """Return the Pydantic model class for the output"""
        pass
    
    async def process(self, user_input: str) -> BaseModel:
        """Template method that calls LLM and parses response"""
        # Generate the task prompt with user input
        task_prompt = self.task_prompt.format(query=user_input) if hasattr(self, 'task_prompt') else user_input
        
        # Call LLM with the prompts
        llm_response = await self.llm_client.generate(
            system_prompt=self.system_prompt,
            user_prompt=task_prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        # Parse and return the response
        return self.parse_response(llm_response)
