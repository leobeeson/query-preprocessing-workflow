from typing import List, Optional
from pydantic import BaseModel, Field


class CategoryEntity(BaseModel):
    """Model for a category entity to be normalised"""
    type: str = Field(default="category", description="Entity type (always 'category')")
    value: str = Field(description="Original extracted category value")


class NormalisedCategoryEntity(BaseModel):
    """Model for a normalised category entity"""
    type: str = Field(default="category", description="Entity type (always 'category')")
    value: str = Field(description="Original extracted category value")
    canon: str = Field(description="Canonical category code")


class CategoryNormalisationInput(BaseModel):
    """Input model for CategoryNormalisationAgent"""
    query: str = Field(description="The original user query")
    entities: List[CategoryEntity] = Field(
        default_factory=list,
        description="List of category entities to normalise"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "How much did I spend on groceries and utilities?",
                "entities": [
                    {"type": "category", "value": "groceries"},
                    {"type": "category", "value": "utilities"}
                ]
            }
        }


class CategoryNormalisationOutput(BaseModel):
    """Output model for CategoryNormalisationAgent"""
    entities: List[NormalisedCategoryEntity] = Field(
        default_factory=list,
        description="List of normalised category entities"
    )
    raw_response: Optional[str] = Field(
        default=None,
        description="Raw LLM response for debugging"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "entities": [
                    {
                        "type": "category",
                        "value": "groceries",
                        "canon": "expenses:groceries.supermarkets"
                    },
                    {
                        "type": "category",
                        "value": "utilities",
                        "canon": "expenses:bills.utilities"
                    }
                ],
                "raw_response": "<response>...</response>"
            }
        }