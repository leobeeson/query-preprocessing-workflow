from typing import List, Literal, Optional
from pydantic import BaseModel, Field


class ProcessableEntity(BaseModel):
    """Model for a processable entity extracted from user query"""
    type: Literal["temporal", "category", "merchant", "amount", "environmental", "budget"] = Field(
        description="The type of entity"
    )
    value: str = Field(
        description="The exact text value from the query"
    )


class ProcessableEntityExtractionOutput(BaseModel):
    """Output model for ProcessableEntityExtractionAgent"""
    entities: List[ProcessableEntity] = Field(
        default_factory=list,
        description="List of extracted processable entities"
    )
    raw_response: Optional[str] = Field(
        default=None,
        description="Raw LLM response for debugging"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "entities": [
                    {"type": "merchant", "value": "Tesco"},
                    {"type": "temporal", "value": "last month"}
                ],
                "raw_response": "<response>...</response>"
            }
        }


class UnprocessableEntity(BaseModel):
    """Model for an unprocessable entity extracted from user query"""
    type: Literal[
        "geographic", 
        "payment_method", 
        "person_recipient",
        "transaction_channel",
        "product_service",
        "bank_reference",
        "financial_product",
        "transaction_status",
        "account"
    ] = Field(description="The type of unprocessable entity")
    value: str = Field(description="The exact text value from the query")
    critical: bool = Field(
        description="Whether this entity makes the query unprocessable"
    )


class UnprocessableEntityExtractionOutput(BaseModel):
    """Output model for UnprocessableEntityExtractionAgent"""
    entities: List[UnprocessableEntity] = Field(
        default_factory=list,
        description="List of extracted unprocessable entities"
    )
    raw_response: Optional[str] = Field(
        default=None,
        description="Raw LLM response for debugging"
    )


class UserIntentValidationOutput(BaseModel):
    """Output model for UserIntentValidationAgent"""
    valid: bool = Field(
        description="Whether the user query is valid for the banking domain"
    )
    justification: str = Field(
        description="Brief justification for the validity decision (max 5 words)"
    )
    raw_response: Optional[str] = Field(
        default=None,
        description="Raw LLM response for debugging"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "valid": True,
                "justification": "Valid spending analysis query",
                "raw_response": "<response>...</response>"
            }
        }


class QuerySecurityValidationOutput(BaseModel):
    """Output model for QuerySecurityValidationAgent"""
    valid: bool = Field(
        description="Whether the query is technically safe to process"
    )
    justification: str = Field(
        description="Brief security justification (max 5 words)"
    )
    raw_response: Optional[str] = Field(
        default=None,
        description="Raw LLM response for debugging"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "valid": True,
                "justification": "Clean natural language query",
                "raw_response": "<response>...</response>"
            }
        }