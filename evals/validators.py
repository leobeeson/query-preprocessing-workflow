"""
Output validation strategies for different types of expected outputs.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class Validator(ABC):
    """Abstract base class for output validators."""
    
    @abstractmethod
    async def validate(
        self,
        actual_output: Dict[str, Any],
        expected: Any,
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, Optional[str]]:
        """
        Validate actual output against expected output.
        
        Args:
            actual_output: The actual output from the agent
            expected: The expected output
            context: Optional context for validation
            
        Returns:
            Tuple of (passed, failure_reason)
        """
        pass


class StringValidator(Validator):
    """Validator for exact string matching."""
    
    def __init__(self, field_name: Optional[str] = None):
        """
        Initialize the string validator.
        
        Args:
            field_name: Optional field name to extract from output dict
        """
        self.field_name: Optional[str] = field_name
    
    
    async def validate(
        self,
        actual_output: Dict[str, Any],
        expected: str,
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, Optional[str]]:
        """Validate string output."""
        # Extract the actual value
        if self.field_name:
            actual_value: Any = actual_output.get(self.field_name)
        else:
            # Try to find the main output field
            actual_value = self._extract_main_output(actual_output)
        
        if actual_value is None:
            return False, f"Output field not found"
        
        # Convert to string for comparison
        actual_str: str = str(actual_value)
        
        if actual_str == expected:
            return True, None
        else:
            return False, f"Expected '{expected}', got '{actual_str}'"
    
    
    def _extract_main_output(self, output: Dict[str, Any]) -> Optional[Any]:
        """Try to extract the main output from common field names."""
        common_fields: List[str] = [
            "output", "result", "response", "answer", "value",
            "classification", "category", "type", "label"
        ]
        
        for field in common_fields:
            if field in output:
                return output[field]
        
        # If dict has single key, use that
        if len(output) == 1:
            return next(iter(output.values()))
        
        return None


class MultiChoiceValidator(Validator):
    """Validator for multiple valid outputs."""
    
    def __init__(self, field_name: Optional[str] = None):
        """
        Initialize the multi-choice validator.
        
        Args:
            field_name: Optional field name to extract from output dict
        """
        self.field_name: Optional[str] = field_name
        self.string_validator: StringValidator = StringValidator(field_name)
    
    
    async def validate(
        self,
        actual_output: Dict[str, Any],
        expected: List[str],
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, Optional[str]]:
        """Validate output against multiple valid choices."""
        # Extract the actual value using string validator's logic
        if self.field_name:
            actual_value: Any = actual_output.get(self.field_name)
        else:
            actual_value = self.string_validator._extract_main_output(actual_output)
        
        if actual_value is None:
            return False, f"Output field not found"
        
        # Convert to string for comparison
        actual_str: str = str(actual_value)
        
        if actual_str in expected:
            return True, None
        else:
            return False, f"Expected one of {expected}, got '{actual_str}'"


class BooleanValidator(Validator):
    """Validator for boolean outputs."""
    
    def __init__(self, field_name: Optional[str] = None):
        """
        Initialize the boolean validator.
        
        Args:
            field_name: Optional field name to extract from output dict
        """
        self.field_name: Optional[str] = field_name
    
    
    async def validate(
        self,
        actual_output: Dict[str, Any],
        expected: bool,
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, Optional[str]]:
        """Validate boolean output."""
        # Extract the actual value
        if self.field_name:
            actual_value: Any = actual_output.get(self.field_name)
        else:
            # Try common boolean field names
            for field in ["valid", "result", "passed", "success", "value"]:
                if field in actual_output:
                    actual_value = actual_output[field]
                    break
            else:
                # If dict has single key, use that
                if len(actual_output) == 1:
                    actual_value = next(iter(actual_output.values()))
                else:
                    actual_value = None
        
        if actual_value is None:
            return False, f"Boolean output field not found"
        
        # Convert to boolean
        if isinstance(actual_value, bool):
            actual_bool: bool = actual_value
        elif isinstance(actual_value, str):
            actual_bool = actual_value.lower() in ["true", "yes", "1"]
        else:
            actual_bool = bool(actual_value)
        
        if actual_bool == expected:
            return True, None
        else:
            return False, f"Expected {expected}, got {actual_bool}"


class CriteriaValidator(Validator):
    """
    Validator using LLM-as-a-Judge for semantic criteria.

    This validator requires an LLMJudge instance to be provided.
    """

    def __init__(self, llm_judge: Optional[Any] = None):
        """
        Initialize the criteria validator.

        Args:
            llm_judge: LLMJudge instance for evaluation
        """
        self.llm_judge: Optional[Any] = llm_judge


    async def validate(
        self,
        actual_output: Dict[str, Any],
        expected: List[str],  # List of criteria
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, Optional[str]]:
        """Validate output against semantic criteria using LLM judge."""
        if not self.llm_judge:
            return False, "LLMJudge not configured for criteria validation"

        # Convert output to string for evaluation
        import json
        output_str: str = json.dumps(actual_output, indent=2)

        # Evaluate with judge
        judge_result = await self.llm_judge.evaluate(
            output=output_str,
            criteria=expected,
            context=context
        )

        if judge_result.passed:
            return True, None
        else:
            return False, judge_result.rationale or "Criteria not met"


class EntityListValidator(Validator):
    """
    Validator for entity extraction outputs.

    Validates lists of entities with type and value fields.
    Supports exact matching and subset validation.
    """

    def __init__(self, field_name: str = "entities", ordered: bool = False):
        """
        Initialize the entity list validator.

        Args:
            field_name: Name of the field containing entities list
            ordered: Whether order matters in comparison
        """
        self.field_name: str = field_name
        self.ordered: bool = ordered


    async def validate(
        self,
        actual_output: Dict[str, Any],
        expected: Union[List[Dict[str, Any]], Dict[str, Any]],
        context: Optional[Dict[str, Any]] = None
    ) -> tuple[bool, Optional[str]]:
        """
        Validate entity list output.

        Args:
            actual_output: The actual output containing entities
            expected: List of expected entities or dict with entities field
            context: Optional context (unused)

        Returns:
            Tuple of (passed, failure_reason)
        """
        # Extract entities from output
        actual_entities = actual_output.get(self.field_name, [])

        # Handle expected being a dict (from Pydantic model_dump())
        if isinstance(expected, dict):
            expected_entities = expected.get(self.field_name, [])
        else:
            expected_entities = expected

        # Handle empty expectations
        if not expected_entities:
            if actual_entities:
                return False, f"Expected no entities, but got {len(actual_entities)}"
            return True, None

        # Handle empty actual output
        if not actual_entities:
            return False, f"Expected {len(expected_entities)} entities, but got none"

        # Normalize entities for comparison
        def normalize_entity(entity: Dict[str, Any]) -> tuple:
            """Create a comparable representation of an entity."""
            return (
                entity.get('type', '').lower().strip(),
                entity.get('value', '').strip()
            )

        # Convert to sets for comparison (if order doesn't matter)
        if not self.ordered:
            expected_set = {normalize_entity(e) for e in expected_entities}
            actual_set = {normalize_entity(e) for e in actual_entities}

            # Check if all expected entities are present
            missing = expected_set - actual_set
            if missing:
                missing_str = ', '.join([f"{t}:{v}" for t, v in missing])
                return False, f"Missing entities: {missing_str}"

            # Check for unexpected entities (optional - could be lenient)
            extra = actual_set - expected_set
            if extra:
                extra_str = ', '.join([f"{t}:{v}" for t, v in extra])
                return False, f"Unexpected entities: {extra_str}"

            return True, None

        else:
            # Ordered comparison
            if len(actual_entities) != len(expected_entities):
                return False, f"Expected {len(expected_entities)} entities, got {len(actual_entities)}"

            for i, (exp, act) in enumerate(zip(expected_entities, actual_entities)):
                exp_norm = normalize_entity(exp)
                act_norm = normalize_entity(act)

                if exp_norm != act_norm:
                    return False, f"Entity {i}: expected {exp_norm[0]}:{exp_norm[1]}, got {act_norm[0]}:{act_norm[1]}"

            return True, None