import time
from anthropic import AsyncAnthropic
from anthropic.types import TextBlock

from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.clients.llm_clients.pricing import PricingConfig
from src.models.llm_metrics import LLMResponse, LLMMetrics


class AnthropicLLMClient(LLMClientInterface):
    def __init__(self, api_key: str, model: str = "claude-3-5-haiku-20241022"):
        self.client = AsyncAnthropic(api_key=api_key)
        self.model = model
        self.pricing = PricingConfig.get_pricing(model)
    
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0,
        max_tokens: int = 500
    ) -> LLMResponse:
        """Generate LLM response using Anthropic's API with metrics tracking"""
        
        # Start timing
        start_time = time.perf_counter()
        
        # Make API call
        response = await self.client.messages.create(
            model=self.model,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # End timing
        end_time = time.perf_counter()
        response_time_ms = (end_time - start_time) * 1000
        
        # Extract text from the first content block
        content = response.content[0]
        if isinstance(content, TextBlock):
            text = content.text
        else:
            text = str(content)
        
        # Extract token usage
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        total_tokens = input_tokens + output_tokens
        
        # Calculate costs
        costs = self.pricing.calculate_cost(input_tokens, output_tokens)
        
        # Create metrics
        metrics = LLMMetrics(
            response_time_ms=response_time_ms,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            input_cost=costs["input_cost"],
            output_cost=costs["output_cost"],
            total_cost=costs["total_cost"],
            model=self.model
        )
        
        return LLMResponse(text=text, metrics=metrics)