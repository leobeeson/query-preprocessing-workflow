"""
Core data models for the evaluation framework.
"""

from typing import Any, Dict, List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field, model_validator


# Type variables for generic EvalCase
TInput = TypeVar('TInput', bound=BaseModel)
TOutput = TypeVar('TOutput')


class EvalCase(BaseModel, Generic[TInput, TOutput]):
    """
    A single evaluation test case with typed input and output.

    Attributes:
        name: Unique identifier for the test case
        input_data: Typed input data to pass to the agent node
        expected_output: Expected typed output
        field_validations: Validation rules for specific fields (including semantic via Criteria)
        description: Optional human-readable description
    """
    name: str = Field(description="Unique identifier for the test case")
    input_data: TInput = Field(description="Typed input data for the agent")
    expected_output: TOutput = Field(description="Expected output (documentation of what we expect)")
    field_validations: Optional[Dict[str, Any]] = Field(default=None, description="Field-level validation rules")
    description: Optional[str] = Field(default=None, description="Human-readable description")


class EvalResult(BaseModel):
    """
    Result of running an evaluation test case.

    Attributes:
        case_name: Name of the test case
        input: The input data that was sent to the agent
        expected_output: The expected output (if applicable)
        actual_output: The actual output from the agent
        passed: Whether the test passed
        error: Any error that occurred during execution
        failure_reason: Explanation of why the test failed (if applicable)
        model_name: Name of the model used
        timestamp: When the test was executed
        duration_ms: How long the test took in milliseconds
        llm_cost: Cost of LLM API calls for this test in USD
        input_tokens: Number of input tokens used
        output_tokens: Number of output tokens used
    """
    case_name: str = Field(description="Name of the test case")
    passed: bool = Field(description="Whether the test passed")
    input: Optional[Any] = Field(default=None, description="Input data sent to the agent")
    expected_output: Optional[Any] = Field(default=None, description="The expected output")
    actual_output: Any = Field(description="The actual output from the agent")
    error: Optional[str] = Field(default=None, description="Error during execution")
    failure_reason: Optional[str] = Field(default=None, description="Why the test failed")
    model_name: Optional[str] = Field(default=None, description="Model name used for this test")
    timestamp: Optional[str] = Field(default=None, description="ISO timestamp of execution")
    duration_ms: Optional[float] = Field(default=None, description="Execution time in milliseconds")
    llm_cost: Optional[float] = Field(default=None, description="LLM API cost in USD")
    input_tokens: Optional[int] = Field(default=None, description="Input tokens used")
    output_tokens: Optional[int] = Field(default=None, description="Output tokens used")
    cache_write_tokens: Optional[int] = Field(default=None, description="Cache write tokens used")
    cache_read_tokens: Optional[int] = Field(default=None, description="Cache read tokens used")
    cache_write_cost: Optional[float] = Field(default=None, description="Cache write cost in USD")
    cache_read_cost: Optional[float] = Field(default=None, description="Cache read cost in USD")
    
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
        
        if self.expected_output is not None:
            details.append(f"Expected: {self.expected_output}")
            details.append(f"Actual: {self.actual_output}")
        
        return "\n".join(details)