"""
LLM Metrics Models
Models for tracking LLM response metrics including timing and cost
"""

from typing import Optional
from pydantic import BaseModel, Field


class LLMMetrics(BaseModel):
    """Metrics for a single LLM API call"""
    
    response_time_ms: float = Field(
        description="Response time in milliseconds"
    )
    input_tokens: int = Field(
        description="Number of input tokens"
    )
    output_tokens: int = Field(
        description="Number of output tokens"
    )
    total_tokens: int = Field(
        description="Total tokens (input + output)"
    )
    input_cost: float = Field(
        description="Cost of input tokens in USD"
    )
    output_cost: float = Field(
        description="Cost of output tokens in USD"
    )
    total_cost: float = Field(
        description="Total cost in USD"
    )
    model: str = Field(
        description="Model name used for generation"
    )
    
    def format_cost(self) -> str:
        """Format cost in a readable way"""
        if self.total_cost < 0.01:
            return f"${self.total_cost:.6f}"
        elif self.total_cost < 1:
            return f"${self.total_cost:.4f}"
        else:
            return f"${self.total_cost:.2f}"
    
    def format_time(self) -> str:
        """Format response time in a readable way"""
        if self.response_time_ms < 1000:
            return f"{self.response_time_ms:.0f}ms"
        else:
            return f"{self.response_time_ms/1000:.2f}s"
    
    class Config:
        json_schema_extra = {
            "example": {
                "response_time_ms": 1234.56,
                "input_tokens": 500,
                "output_tokens": 200,
                "total_tokens": 700,
                "input_cost": 0.0015,
                "output_cost": 0.003,
                "total_cost": 0.0045,
                "model": "claude-3-5-sonnet-20241022"
            }
        }


class LLMResponse(BaseModel):
    """Response from LLM with text and metrics"""
    
    text: str = Field(
        description="The generated text response"
    )
    metrics: LLMMetrics = Field(
        description="Metrics for this LLM call"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "This is the LLM response text...",
                "metrics": {
                    "response_time_ms": 1234.56,
                    "input_tokens": 500,
                    "output_tokens": 200,
                    "total_tokens": 700,
                    "input_cost": 0.0015,
                    "output_cost": 0.003,
                    "total_cost": 0.0045,
                    "model": "claude-3-5-sonnet-20241022"
                }
            }
        }