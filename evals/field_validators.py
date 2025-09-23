"""
Field-level validation wrappers for fine-grained control over output validation.
"""

from typing import Any, List, Union
from pydantic import BaseModel


class FieldValidator(BaseModel):
    """Base class for field validators."""
    pass


class Exact(FieldValidator):
    """Field must exactly match this value."""
    value: Any
    case_sensitive: bool = False


class OneOf(FieldValidator):
    """Field must be one of these values."""
    values: List[Any]
    case_sensitive: bool = False


class AllOf(FieldValidator):
    """Field must contain all these values (for list fields)."""
    values: List[Any]


class Contains(FieldValidator):
    """Field must contain at least these values (subset check)."""
    values: List[Any]


class Criteria(FieldValidator):
    """Field evaluated by LLM-as-Judge against criteria."""
    criteria: List[str]


class Substring(FieldValidator):
    """Field must contain this substring (for string fields)."""
    value: str
    case_sensitive: bool = False


class ListMatches(FieldValidator):
    """
    List must contain items matching the specification.

    Each item in the list is validated against the item_spec,
    which maps field names to validators.

    Example:
        ListMatches(items=[
            {"type": Exact(value="category"), "value": Substring(value="transport")}
        ])
    """
    items: List[dict]