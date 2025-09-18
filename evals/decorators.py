"""
Decorator infrastructure for evaluation cases.
"""

from typing import Callable, Optional, List, Dict, Any, Type
from functools import wraps

from pydantic import BaseModel
from evals.core import EvalCase


# Global registry to store decorated evaluation cases
_EVAL_REGISTRY = {}


def eval_case(
    name: str,
    agent_class: Optional[Type] = None,
    description: Optional[str] = None,
    tags: Optional[List[str]] = None,
    priority: int = 0
):
    """
    Decorator for defining evaluation cases.

    Args:
        name: Unique name for the evaluation case
        agent_class: The agent class this case is for
        description: Description of what this case tests
        tags: Optional tags for grouping/filtering cases
        priority: Priority for test execution (higher = run first)

    Example:
        @eval_case(
            name="basic_merchant",
            agent_class=ProcessableEntityExtractionAgent,
            description="Simple merchant extraction",
            tags=["merchant", "basic"]
        )
        def eval_basic_merchant():
            return {
                "input": QueryInput(query="Tesco transactions"),
                "expected": ProcessableEntityExtractionOutput(...),
                "field_validations": {...}
            }
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # Store metadata
        wrapper.eval_metadata = {
            "name": name,
            "agent_class": agent_class,
            "description": description,
            "tags": tags or [],
            "priority": priority,
            "function": func
        }

        # Register the case
        if agent_class:
            agent_name = agent_class.__name__
            if agent_name not in _EVAL_REGISTRY:
                _EVAL_REGISTRY[agent_name] = {}
            _EVAL_REGISTRY[agent_name][name] = wrapper
        else:
            # Store without agent class (will need to specify when running)
            if "__unassigned__" not in _EVAL_REGISTRY:
                _EVAL_REGISTRY["__unassigned__"] = {}
            _EVAL_REGISTRY["__unassigned__"][name] = wrapper

        return wrapper

    return decorator


def get_eval_case(
    func: Callable,
    input_type: Type[BaseModel],
    output_type: Type[BaseModel]
) -> EvalCase:
    """
    Convert a decorated function to an EvalCase.

    Args:
        func: The decorated function
        input_type: Type for input data
        output_type: Type for output data

    Returns:
        EvalCase instance
    """
    # Get the case data from the function
    case_data = func()

    # Extract components
    input_data = case_data.get("input")
    expected_output = case_data.get("expected")
    field_validations = case_data.get("field_validations")

    # Get metadata
    metadata = getattr(func, "eval_metadata", {})

    # Create EvalCase
    return EvalCase[input_type, output_type](
        name=metadata.get("name", func.__name__),
        input_data=input_data,
        expected_output=expected_output,
        field_validations=field_validations,
        description=metadata.get("description")
    )


def clear_registry():
    """Clear all registered evaluation cases."""
    global _EVAL_REGISTRY
    _EVAL_REGISTRY = {}


def get_registry():
    """Get the global evaluation registry."""
    return _EVAL_REGISTRY