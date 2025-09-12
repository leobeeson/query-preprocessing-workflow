"""
Test file to verify the simplified evaluation framework works correctly.

Run with: python scratchpad/evals/test_framework.py
"""

import asyncio
import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from typing import Any, Dict, Optional
from scratchpad.evals.core import EvalCase, EvalResult, ValidationMethod
from scratchpad.evals.context import ConversationContext
from scratchpad.evals.validators import StringValidator, MultiChoiceValidator, BooleanValidator
from scratchpad.evals.runner import EvalRunner
from scratchpad.evals.utils import create_summary, print_summary


# Test LLM Client
class TestLLMClient:
    """Test LLM client with predictable responses."""
    
    def __init__(self):
        self.responses: Dict[str, str] = {
            "classify: what is vat?": "CONCEPTUAL",
            "classify: how do i create an invoice?": "PROCEDURAL",
            "classify: where is the settings menu?": "NAVIGATION",
            "classify: can i export to pdf?": "CAPABILITY",
            "classify: the system is not working": "TROUBLESHOOTING",
            "classify: how do i?": "AMBIGUOUS",
            "validate: test@example.com": "true",
            "validate: not-an-email": "false",
        }
    
    async def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.1,
        max_tokens: int = 1000
    ) -> str:
        """Return predictable responses for testing."""
        # Normalize the query
        query_lower: str = user_prompt.lower().strip()
        
        # Return mapped response or default
        for key, response in self.responses.items():
            if key in query_lower:
                return response
        
        return "UNKNOWN"


# Test Agent Node
class TestClassificationAgent:
    """Test agent for classification."""
    
    def __init__(self, llm_client: Any):
        self.llm_client: Any = llm_client
        self.node_name: str = "TestClassificationAgent"
    
    async def process(self, context: ConversationContext) -> ConversationContext:
        """Process and classify query."""
        query: str = context.query
        
        response: str = await self.llm_client.generate(
            system_prompt="Classify the query",
            user_prompt=f"Classify: {query}"
        )
        
        context.update_workflow_node(
            self.node_name,
            classification=response.strip()
        )
        
        return context


class TestValidationAgent:
    """Test agent for validation."""
    
    def __init__(self, llm_client: Any):
        self.llm_client: Any = llm_client
        self.node_name: str = "TestValidationAgent"
    
    async def process(self, context: ConversationContext) -> ConversationContext:
        """Validate input."""
        query: str = context.query
        
        response: str = await self.llm_client.generate(
            system_prompt="Validate the input",
            user_prompt=f"Validate: {query}"
        )
        
        is_valid: bool = response.strip().lower() == "true"
        
        context.update_workflow_node(
            self.node_name,
            is_valid=is_valid
        )
        
        return context


async def test_string_validation():
    """Test string validation."""
    print("\n🧪 Testing String Validation...")
    
    validator = StringValidator(field_name="classification")
    
    # Test exact match
    actual = {"classification": "CONCEPTUAL"}
    passed, reason = await validator.validate(actual, "CONCEPTUAL")
    assert passed, f"String validation should pass: {reason}"
    print("  ✅ Exact match works")
    
    # Test mismatch
    passed, reason = await validator.validate(actual, "PROCEDURAL")
    assert not passed, "String validation should fail for mismatch"
    assert "Expected 'PROCEDURAL'" in reason
    print("  ✅ Mismatch detection works")
    
    # Test missing field
    actual = {"other_field": "value"}
    passed, reason = await validator.validate(actual, "CONCEPTUAL")
    assert not passed, "Should fail for missing field"
    print("  ✅ Missing field detection works")


async def test_multi_choice_validation():
    """Test multi-choice validation."""
    print("\n🧪 Testing Multi-Choice Validation...")
    
    validator = MultiChoiceValidator(field_name="classification")
    
    # Test valid choice
    actual = {"classification": "PROCEDURAL"}
    choices = ["PROCEDURAL", "CAPABILITY", "AMBIGUOUS"]
    passed, reason = await validator.validate(actual, choices)
    assert passed, f"Should pass for valid choice: {reason}"
    print("  ✅ Valid choice works")
    
    # Test invalid choice
    actual = {"classification": "NAVIGATION"}
    passed, reason = await validator.validate(actual, choices)
    assert not passed, "Should fail for invalid choice"
    assert "Expected one of" in reason
    print("  ✅ Invalid choice detection works")


async def test_boolean_validation():
    """Test boolean validation."""
    print("\n🧪 Testing Boolean Validation...")
    
    validator = BooleanValidator(field_name="is_valid")
    
    # Test true match
    actual = {"is_valid": True}
    passed, reason = await validator.validate(actual, True)
    assert passed, f"Boolean validation should pass: {reason}"
    print("  ✅ Boolean true works")
    
    # Test false match
    actual = {"is_valid": False}
    passed, reason = await validator.validate(actual, False)
    assert passed, f"Boolean validation should pass: {reason}"
    print("  ✅ Boolean false works")
    
    # Test mismatch
    passed, reason = await validator.validate(actual, True)
    assert not passed, "Should fail for boolean mismatch"
    print("  ✅ Boolean mismatch detection works")


async def test_eval_runner():
    """Test the evaluation runner."""
    print("\n🧪 Testing Evaluation Runner...")
    
    llm_client = TestLLMClient()
    
    # Create test cases
    test_cases = [
        EvalCase(
            name="conceptual_classification",
            input_data={"query": "What is VAT?"},
            expected_output="CONCEPTUAL"
        ),
        EvalCase(
            name="procedural_classification",
            input_data={"query": "How do I create an invoice?"},
            expected_output="PROCEDURAL"
        ),
        EvalCase(
            name="ambiguous_classification",
            input_data={"query": "How do I?"},
            expected_output=["AMBIGUOUS", "PROCEDURAL"]  # Multi-choice
        ),
        EvalCase(
            name="navigation_classification",
            input_data={"query": "Where is the settings menu?"},
            expected_output="NAVIGATION"
        ),
    ]
    
    # Initialize runner
    runner = EvalRunner(
        agent_class=TestClassificationAgent,
        llm_client=llm_client,
        default_field_name="classification",
        use_judge_for_criteria=False  # Not testing judge here
    )
    
    # Run single test
    single_result = await runner.run_single(test_cases[0])
    assert single_result.passed, f"Single test should pass: {single_result.failure_reason}"
    print("  ✅ Single test execution works")
    
    # Run batch tests
    results = await runner.run_batch(test_cases, parallel=False)
    assert len(results) == len(test_cases), "Should have results for all tests"
    
    # Check results
    passed_count = sum(1 for r in results if r.passed)
    assert passed_count == len(test_cases), f"All tests should pass, got {passed_count}/{len(test_cases)}"
    print("  ✅ Batch test execution works")
    
    # Test summary creation
    summary = create_summary(results)
    assert summary["total"] == len(test_cases)
    assert summary["passed"] == len(test_cases)
    assert summary["failed"] == 0
    assert summary["pass_rate"] == 100.0
    print("  ✅ Summary creation works")


async def test_validation_methods():
    """Test that validation methods are correctly identified."""
    print("\n🧪 Testing Validation Method Detection...")
    
    # String validation
    case = EvalCase(name="test", input_data={}, expected_output="string")
    assert case.get_validation_method() == ValidationMethod.STRING
    print("  ✅ String method detected")
    
    # Multi-choice validation
    case = EvalCase(name="test", input_data={}, expected_output=["opt1", "opt2"])
    assert case.get_validation_method() == ValidationMethod.MULTI_CHOICE
    print("  ✅ Multi-choice method detected")
    
    # Boolean validation
    case = EvalCase(name="test", input_data={}, expected_output=True)
    assert case.get_validation_method() == ValidationMethod.BOOLEAN
    print("  ✅ Boolean method detected")
    
    # Criteria validation
    case = EvalCase(name="test", input_data={}, criteria=["criterion1"])
    assert case.get_validation_method() == ValidationMethod.CRITERIA
    print("  ✅ Criteria method detected")


async def test_failure_handling():
    """Test that failures are properly handled and reported."""
    print("\n🧪 Testing Failure Handling...")
    
    llm_client = TestLLMClient()
    
    # Create test case that will fail
    failing_case = EvalCase(
        name="expected_failure",
        input_data={"query": "What is VAT?"},
        expected_output="WRONG_ANSWER"  # This will fail
    )
    
    runner = EvalRunner(
        agent_class=TestClassificationAgent,
        llm_client=llm_client,
        default_field_name="classification",
        use_judge_for_criteria=False
    )
    
    result = await runner.run_single(failing_case)
    assert not result.passed, "Test should fail"
    assert result.failure_reason is not None
    assert "Expected 'WRONG_ANSWER'" in result.failure_reason
    assert "got 'CONCEPTUAL'" in result.failure_reason
    print("  ✅ Failure detection works")
    print("  ✅ Failure reason is informative")
    
    # Test error handling
    class ErrorAgent:
        def __init__(self, llm_client):
            self.node_name = "ErrorAgent"
        
        async def process(self, context):
            raise ValueError("Simulated error")
    
    runner = EvalRunner(
        agent_class=ErrorAgent,
        llm_client=llm_client,
        use_judge_for_criteria=False
    )
    
    error_case = EvalCase(
        name="error_case",
        input_data={"query": "test"},
        expected_output="anything"
    )
    
    result = await runner.run_single(error_case)
    assert not result.passed, "Test should fail on error"
    assert result.error is not None
    assert "Simulated error" in result.error
    print("  ✅ Error handling works")


async def run_all_tests():
    """Run all framework tests."""
    print("\n" + "=" * 60)
    print("SIMPLIFIED EVALUATION FRAMEWORK TESTS")
    print("=" * 60)
    
    try:
        # Run individual component tests
        await test_string_validation()
        await test_multi_choice_validation()
        await test_boolean_validation()
        await test_validation_methods()
        
        # Run integration tests
        await test_eval_runner()
        await test_failure_handling()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\nThe simplified evaluation framework is working correctly.")
        print("It provides all core functionality in ~400 lines of clean code.")
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        raise
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(run_all_tests())