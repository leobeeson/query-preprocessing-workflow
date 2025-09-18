"""
Evaluator for evaluation framework with field-level validation support.
"""

from typing import Optional, Dict, Any, Tuple, List
from pydantic import BaseModel

from evals.field_validators import (
    FieldValidator,
    Exact,
    OneOf,
    AllOf,
    Contains,
    Criteria,
    Substring,
    ListMatches
)


class Evaluator:
    """
    Evaluator that supports field-level validation rules and equality fallback.
    """

    def __init__(self, judge_client=None):
        """
        Initialize the evaluator.

        Args:
            judge_client: Optional LLM client for Criteria validation
        """
        self.judge_client = judge_client

    async def validate(
        self,
        actual: BaseModel,
        expected_output: Optional[BaseModel] = None,
        field_validations: Optional[Dict[str, FieldValidator]] = None
    ) -> Tuple[bool, Optional[str]]:
        """
        Validate actual output against validation rules.

        Validation priority:
        1. If field_validations is provided, use field-level validation (including Criteria for semantic)
        2. If no field_validations but expected_output provided, use equality check
        3. Otherwise, validation fails

        Args:
            actual: The actual output from the agent (Pydantic model)
            expected_output: Expected output for equality fallback
            field_validations: Validation rules for specific fields (including Criteria for semantic evaluation)

        Returns:
            Tuple of (passed, failure_reason)
        """
        # If field_validations is provided and not empty, use field-level validation
        if field_validations:
            return await self._validate_fields(actual, field_validations)

        # If no field_validations but expected_output provided, fallback to equality
        if expected_output is not None:
            # Create copies to avoid modifying originals
            actual_copy = actual.model_copy()
            expected_copy = expected_output.model_copy()

            # Remove raw_response fields if they exist (we don't want to compare these)
            if hasattr(actual_copy, 'raw_response'):
                actual_copy.raw_response = None # type: ignore
            if hasattr(expected_copy, 'raw_response'):
                expected_copy.raw_response = None # type: ignore

            if actual_copy == expected_copy:
                return True, None
            else:
                # Only convert to dict for error message
                actual_dict = actual_copy.model_dump()
                expected_dict = expected_copy.model_dump()
                return False, f"Output mismatch: expected {expected_dict}, got {actual_dict}"

        # No validation rules specified
        return False, "No validation rules specified (no field_validations or expected_output)"

    async def _validate_fields(
        self,
        actual: BaseModel,
        field_validations: Dict[str, FieldValidator]
    ) -> Tuple[bool, Optional[str]]:
        """
        Validate each specified field against its validation rules.

        Args:
            actual: The actual output from the agent
            field_validations: Validation rules for specific fields

        Returns:
            Tuple of (passed, failure_reason)
        """
        # Get actual output as dict
        actual_dict = actual.model_dump()
        failures = []

        # Validate each field with specified rules
        for field_name, validator in field_validations.items():
            # Check field exists
            if field_name not in actual_dict:
                failures.append(f"Field '{field_name}' not found in output")
                continue

            actual_value = actual_dict[field_name]

            # Apply appropriate validation
            if isinstance(validator, Exact):
                if actual_value != validator.value:
                    failures.append(
                        f"Field '{field_name}': expected {validator.value}, got {actual_value}"
                    )

            elif isinstance(validator, OneOf):
                if actual_value not in validator.values:
                    failures.append(
                        f"Field '{field_name}': expected one of {validator.values}, got {actual_value}"
                    )

            elif isinstance(validator, AllOf):
                if not isinstance(actual_value, list):
                    failures.append(
                        f"Field '{field_name}': expected list for AllOf validation, got {type(actual_value)}"
                    )
                elif set(actual_value) != set(validator.values):
                    failures.append(
                        f"Field '{field_name}': expected all of {validator.values}, got {actual_value}"
                    )

            elif isinstance(validator, Contains):
                if not isinstance(actual_value, list):
                    failures.append(
                        f"Field '{field_name}': expected list for Contains validation, got {type(actual_value)}"
                    )
                elif not set(validator.values).issubset(set(actual_value)):
                    missing = set(validator.values) - set(actual_value)
                    failures.append(
                        f"Field '{field_name}': missing required values {missing}"
                    )

            elif isinstance(validator, Criteria):
                # Use LLM judge for this field
                passed, reason = await self._validate_field_with_criteria(
                    field_name, actual_value, validator.criteria
                )
                if not passed:
                    failures.append(f"Field '{field_name}': {reason}")

            elif isinstance(validator, Substring):
                if not isinstance(actual_value, str):
                    failures.append(
                        f"Field '{field_name}': expected string for Substring validation, got {type(actual_value)}"
                    )
                elif validator.value not in actual_value:
                    failures.append(
                        f"Field '{field_name}': expected to contain '{validator.value}', got '{actual_value}'"
                    )

            elif isinstance(validator, ListMatches):
                if not isinstance(actual_value, list):
                    failures.append(
                        f"Field '{field_name}': expected list for ListMatches validation, got {type(actual_value)}"
                    )
                else:
                    # Validate that list contains items matching the specifications
                    list_failures = await self._validate_list_matches(
                        field_name, actual_value, validator.items
                    )
                    if list_failures:
                        failures.extend(list_failures)

            else:
                failures.append(f"Field '{field_name}': unknown validator type {type(validator)}")

        # Return results
        if failures:
            return False, "; ".join(failures)
        return True, None

    async def _validate_list_matches(
        self,
        field_name: str,
        actual_list: List[Dict],
        expected_specs: List[Dict]
    ) -> List[str]:
        """
        Validate that a list contains items matching the specifications.

        Args:
            field_name: Name of the field being validated
            actual_list: Actual list of items to validate
            expected_specs: List of specifications (each spec is a dict mapping field names to validators)

        Returns:
            List of failure messages (empty if all specs match)
        """
        failures = []

        for spec_idx, spec in enumerate(expected_specs):
            # For each spec, try to find a matching item in actual_list
            found_match = False

            for actual_item in actual_list:
                # Check if this item matches all validators in the spec
                item_matches = True

                for item_field, validator in spec.items():
                    if not isinstance(validator, FieldValidator):
                        # Handle plain values as Exact validators
                        validator = Exact(value=validator)

                    # Get the actual value from the item
                    actual_field_value = actual_item.get(item_field) if isinstance(actual_item, dict) else None

                    # Validate this field
                    field_valid = False

                    if isinstance(validator, Exact):
                        field_valid = actual_field_value == validator.value
                    elif isinstance(validator, Substring):
                        field_valid = (
                            isinstance(actual_field_value, str) and
                            validator.value in actual_field_value
                        )
                    elif isinstance(validator, OneOf):
                        field_valid = actual_field_value in validator.values
                    # Add more validator types as needed

                    if not field_valid:
                        item_matches = False
                        break

                if item_matches:
                    found_match = True
                    break

            if not found_match:
                # Format the spec for error message
                spec_str = ", ".join(
                    f"{k}={v.value if isinstance(v, Exact) else v.value if isinstance(v, Substring) else v}"
                    for k, v in spec.items()
                )
                failures.append(
                    f"Field '{field_name}': no item matching spec [{spec_str}]"
                )

        return failures

    async def _validate_field_with_criteria(
        self,
        field_name: str,
        actual_value: Any,
        criteria: List[str]
    ) -> Tuple[bool, Optional[str]]:
        """Validate a specific field using LLM-as-Judge."""
        if not self.judge_client:
            return False, "No judge client configured for criteria validation"

        # Import here to avoid circular dependency
        from evals.judge import LLMJudge
        judge = LLMJudge(self.judge_client)

        # Use judge to evaluate the field
        result = await judge.evaluate(
            output=str({field_name: actual_value}), #TODO: better serialization
            criteria=criteria
        )

        if result.passed:
            return True, None
        return False, result.rationale or "Criteria not met"
