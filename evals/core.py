"""
Core data models for the evaluation framework.
"""

from typing import Any, Dict, List, Optional, Union
from enum import Enum
from dataclasses import dataclass, field


class ValidationMethod(Enum):
    """Types of validation methods available."""
    STRING = "string"
    MULTI_CHOICE = "multi_choice"
    BOOLEAN = "boolean"
    CRITERIA = "criteria"


@dataclass
class EvalCase:
    """
    A single evaluation test case.
    
    Attributes:
        name: Unique identifier for the test case
        input_data: Input data to pass to the agent node
        expected_output: Expected output (string, list, bool, or dict)
        criteria: Optional list of semantic criteria for LLM-as-a-Judge
        description: Optional human-readable description
    """
    name: str
    input_data: Dict[str, Any]
    expected_output: Optional[Union[str, List[str], bool, Dict[str, Any]]] = None
    criteria: Optional[List[str]] = None
    description: Optional[str] = None
    
    def __post_init__(self) -> None:
        """Validate that either expected_output or criteria is provided."""
        if self.expected_output is None and self.criteria is None:
            raise ValueError(
                f"EvalCase '{self.name}' must have either expected_output or criteria"
            )
        
        if self.expected_output is not None and self.criteria is not None:
            raise ValueError(
                f"EvalCase '{self.name}' cannot have both expected_output and criteria. "
                "Choose one validation method."
            )
    
    
    def get_validation_method(self) -> ValidationMethod:
        """Determine the validation method based on the expected output type."""
        if self.criteria is not None:
            return ValidationMethod.CRITERIA
        elif isinstance(self.expected_output, bool):
            return ValidationMethod.BOOLEAN
        elif isinstance(self.expected_output, list):
            return ValidationMethod.MULTI_CHOICE
        else:
            return ValidationMethod.STRING


@dataclass
class EvalResult:
    """
    Result of running an evaluation test case.
    
    Attributes:
        case_name: Name of the test case
        passed: Whether the test passed
        actual_output: The actual output from the agent
        expected_output: The expected output (if applicable)
        validation_method: The validation method used
        error: Any error that occurred during execution
        failure_reason: Explanation of why the test failed (if applicable)
    """
    case_name: str
    passed: bool
    actual_output: Dict[str, Any]
    expected_output: Optional[Any] = None
    validation_method: Optional[ValidationMethod] = None
    error: Optional[str] = None
    failure_reason: Optional[str] = None
    
    def __str__(self) -> str:
        """String representation for clear reporting."""
        status: str = "✅ PASSED" if self.passed else "❌ FAILED"
        result: str = f"{status}: {self.case_name}"
        if self.failure_reason:
            result += f"\n  Reason: {self.failure_reason}"
        if self.error:
            result += f"\n  Error: {self.error}"
        return result
    
    
    def get_failure_details(self) -> str:
        """Get detailed information about the failure."""
        if self.passed:
            return "Test passed"
        
        details: List[str] = [f"Test case: {self.case_name}"]
        
        if self.error:
            details.append(f"Error: {self.error}")
        
        if self.failure_reason:
            details.append(f"Failure reason: {self.failure_reason}")
        
        if self.validation_method:
            details.append(f"Validation method: {self.validation_method.value}")
        
        if self.expected_output is not None:
            details.append(f"Expected: {self.expected_output}")
            details.append(f"Actual: {self.actual_output}")
        
        return "\n".join(details)