"""
Base models for agent inputs and outputs.
"""

from pydantic import BaseModel, Field


class QueryInput(BaseModel):
    """
    Simple input model for agents that only need a query string.
    """
    query: str = Field(
        description="The user query to process"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "query": "Show me transactions at Tesco last month"
            }
        }