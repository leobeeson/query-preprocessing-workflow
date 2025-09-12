from abc import ABC, abstractmethod
from typing import Dict, Any

from src.models.llm_metrics import LLMResponse


class LLMClientInterface(ABC):
    @abstractmethod
    async def generate(
        self, 
        system_prompt: str, 
        user_prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1000
    ) -> LLMResponse:
        """Generate LLM response with metrics"""
        pass
