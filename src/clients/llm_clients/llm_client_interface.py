from abc import ABC, abstractmethod
from typing import Dict, Any


class LLMClientInterface(ABC):
    @abstractmethod
    async def generate(
        self, 
        system_prompt: str, 
        user_prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1000
    ) -> str:
        """Generate LLM response"""
        pass
