"""
LLM Pricing Configuration Module
Stores pricing information for different LLM models
"""

from typing import Dict


class ModelPricing:
    """Pricing configuration for a specific LLM model"""
    
    def __init__(self, input_cost_per_million: float, output_cost_per_million: float):
        """
        Initialize model pricing.
        
        Args:
            input_cost_per_million: Cost per million input tokens in USD
            output_cost_per_million: Cost per million output tokens in USD
        """
        self.input_cost_per_million = input_cost_per_million
        self.output_cost_per_million = output_cost_per_million
    
    def calculate_cost(self, input_tokens: int, output_tokens: int) -> Dict[str, float]:
        """
        Calculate the cost for a given number of tokens.
        
        Args:
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            
        Returns:
            Dictionary with input_cost, output_cost, and total_cost in USD
        """
        input_cost = (input_tokens / 1_000_000) * self.input_cost_per_million
        output_cost = (output_tokens / 1_000_000) * self.output_cost_per_million
        
        return {
            "input_cost": input_cost,
            "output_cost": output_cost,
            "total_cost": input_cost + output_cost
        }


class PricingConfig:
    """Central configuration for all LLM model pricing"""
    
    # Anthropic model pricing (as of September 2025)
    ANTHROPIC_PRICING: Dict[str, ModelPricing] = {
        # Claude Opus 4.1
        "claude-opus-4-1-20250805": ModelPricing(
            input_cost_per_million=15.0,   # $15 per million input tokens
            output_cost_per_million=75.0   # $75 per million output tokens
        ),
        # Claude Opus 4
        "claude-opus-4-20250514": ModelPricing(
            input_cost_per_million=15.0,   # $15 per million input tokens
            output_cost_per_million=75.0   # $75 per million output tokens
        ),
        # Claude Sonnet 4
        "claude-sonnet-4-20250514": ModelPricing(
            input_cost_per_million=3.0,    # $3 per million input tokens
            output_cost_per_million=15.0   # $15 per million output tokens
        ),
        # Claude Sonnet 3.7
        "claude-3-7-sonnet-20250219": ModelPricing(
            input_cost_per_million=3.0,    # $3 per million input tokens
            output_cost_per_million=15.0   # $15 per million output tokens
        ),
        # Claude Haiku 3.5
        "claude-3-5-haiku-20241022": ModelPricing(
            input_cost_per_million=0.80,   # $0.80 per million input tokens
            output_cost_per_million=4.0    # $4 per million output tokens
        ),
        # Claude Haiku 3
        "claude-3-haiku-20240307": ModelPricing(
            input_cost_per_million=0.25,   # $0.25 per million input tokens
            output_cost_per_million=1.25   # $1.25 per million output tokens
        ),
    }
    
    @classmethod
    def get_pricing(cls, model_name: str) -> ModelPricing:
        """
        Get pricing for a specific model.
        
        Args:
            model_name: Name of the model
            
        Returns:
            ModelPricing instance for the model
            
        Raises:
            ValueError: If model pricing is not configured
        """
        if model_name in cls.ANTHROPIC_PRICING:
            return cls.ANTHROPIC_PRICING[model_name]
        
        raise ValueError(f"Pricing not configured for model: {model_name}")