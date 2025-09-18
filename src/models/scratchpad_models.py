"""
Models for scratchpad/testing agents.
"""

from typing import Optional
from pydantic import BaseModel, Field


class TextInput(BaseModel):
    """Simple text input for testing."""
    text: str = Field(description="The text to analyze")


class SentimentAnalysisOutput(BaseModel):
    """Output model for sentiment analysis agent."""
    sentiment: str = Field(description="The detected sentiment: positive, negative, or neutral")
    reasoning: str = Field(description="Explanation for the sentiment classification")
    raw_response: Optional[str] = Field(default=None, description="Raw LLM response")