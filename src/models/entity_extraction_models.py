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
    type: str = Field(
        description="The type of unprocessable entity - can be standard types (geographic, payment_method, etc.) or dynamic 1-3 word descriptive types"
    )
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


class PIIEntity(BaseModel):
    """Model for a PII entity extracted from user query"""
    type: str = Field(
        description="The type of PII entity. Expected values: phone, name, email, username, password, cvv, card_number, card_expiry, pin, bank_account, swift_code, aws_key, nhs_number, ni_number, utr_number, other"
    )
    value: str = Field(
        description="The exact text value from the query"
    )


class PIIExtractionOutput(BaseModel):
    """Output model for PIIExtractionAgent"""
    entities: List[PIIEntity] = Field(
        default_factory=list,
        description="List of extracted PII entities"
    )
    raw_response: Optional[str] = Field(
        default=None,
        description="Raw LLM response for debugging"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "entities": [
                    {"type": "email", "value": "john.smith@gmail.com"},
                    {"type": "phone", "value": "07700900123"}
                ],
                "raw_response": "<response>...</response>"
            }
        }