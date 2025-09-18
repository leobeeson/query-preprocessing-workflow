from abc import ABC, abstractmethod
from typing import Type, TypeVar, Optional, Generic
from pydantic import BaseModel

from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.llm_metrics import LLMMetrics

TInput = TypeVar('TInput', bound=BaseModel)
TOutput = TypeVar('TOutput', bound=BaseModel)


class AgentNodeBase(ABC, Generic[TInput, TOutput]):
      
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
        self.last_metrics: Optional[LLMMetrics] = None


    def set_prompts(self, system_prompt: str, task_prompt: str) -> None:
        self.system_prompt: str = system_prompt
        self.task_prompt: str = task_prompt


    @abstractmethod
    def parse_response(self, llm_response: str) -> TOutput:
        """Parse the LLM response into a Pydantic model"""
        pass

    @abstractmethod
    def get_input_model(self) -> Type[TInput]:
        """Return the Pydantic model class for the input"""
        pass

    @abstractmethod
    def get_output_model(self) -> Type[TOutput]:
        """Return the Pydantic model class for the output"""
        pass

    @abstractmethod
    def format_user_prompt(self, input_data: TInput) -> str:
        """Format the input data into a user prompt for the LLM"""
        pass

    async def process(self, input_data: TInput) -> TOutput:
        """Template method that calls LLM and parses response"""
        # Format the user prompt from input data
        user_prompt = self.format_user_prompt(input_data)

        # Call LLM with the prompts (now returns LLMResponse)
        llm_response = await self.llm_client.generate(
            system_prompt=self.system_prompt,
            user_prompt=user_prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        # Store metrics for later retrieval
        self.last_metrics = llm_response.metrics

        # Parse and return the response
        return self.parse_response(llm_response.text)
    
    def get_last_metrics(self) -> Optional[LLMMetrics]:
        """Get metrics from the last LLM call"""
        return self.last_metrics
