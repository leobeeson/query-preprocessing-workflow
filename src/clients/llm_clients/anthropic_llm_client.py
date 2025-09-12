from anthropic import AsyncAnthropic
from anthropic.types import TextBlock
from src.clients.llm_clients.llm_client_interface import LLMClientInterface


class AnthropicLLMClient(LLMClientInterface):
    def __init__(self, api_key: str):
        self.client = AsyncAnthropic(api_key=api_key)
    
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1000
    ) -> str:
        """Generate LLM response using Anthropic's API"""
        response = await self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        # Extract text from the first content block
        content = response.content[0]
        if isinstance(content, TextBlock):
            return content.text
        # Fallback for other content types
        return str(content)