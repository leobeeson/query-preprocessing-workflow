"""
Test runner for executing evaluations.
"""

import asyncio
from typing import Any, Dict, List, Optional, Type

try:
    # Try relative imports first (when used as a package)
    from .core import EvalCase, EvalResult, ValidationMethod
    from .context import ConversationContext
    from .validators import (
        Validator,
        StringValidator,
        MultiChoiceValidator,
        BooleanValidator,
        CriteriaValidator,
    )
    from .judge import LLMJudge
except ImportError:
    # Fall back to absolute imports (when running directly)
    from core import EvalCase, EvalResult, ValidationMethod
    from context import ConversationContext
    from validators import (
        Validator,
        StringValidator,
        MultiChoiceValidator,
        BooleanValidator,
        CriteriaValidator,
    )
    from judge import LLMJudge


class EvalRunner:
    """
    Main test runner for executing agent node evaluations.
    
    This class handles:
    - Agent node initialization
    - Test case execution
    - Output validation
    - Result reporting
    """
    
    def __init__(
        self,
        agent_class: Type[Any],
        llm_client: Any,
        model_name: Optional[str] = None,
        default_field_name: Optional[str] = None,
        use_judge_for_criteria: bool = True
    ):
        """
        Initialize the evaluation runner.
        
        Args:
            agent_class: The agent node class to test
            llm_client: LLM client for the agent (and optionally judge)
            model_name: Optional model name override
            default_field_name: Default field to extract from output
            use_judge_for_criteria: Whether to use LLM-as-a-Judge for criteria
        """
        self.agent_class: Type[Any] = agent_class
        self.llm_client: Any = llm_client
        self.model_name: Optional[str] = model_name
        self.default_field_name: Optional[str] = default_field_name
        
        # Initialize agent instance
        if model_name and hasattr(agent_class, '__init__'):
            # Try to pass model_name if supported
            try:
                self.agent: Any = agent_class(llm_client=llm_client, model_name=model_name)
            except TypeError:
                # Fallback to just llm_client
                self.agent = agent_class(llm_client=llm_client)
        else:
            self.agent = agent_class(llm_client=llm_client)
        
        # Initialize validators
        self.validators: Dict[ValidationMethod, Validator] = {
            ValidationMethod.STRING: StringValidator(default_field_name),
            ValidationMethod.MULTI_CHOICE: MultiChoiceValidator(default_field_name),
            ValidationMethod.BOOLEAN: BooleanValidator(default_field_name),
        }
        
        # Initialize LLM judge if needed
        if use_judge_for_criteria:
            self.llm_judge: Optional[LLMJudge] = LLMJudge(llm_client)
            self.validators[ValidationMethod.CRITERIA] = CriteriaValidator(self.llm_judge)
        else:
            self.llm_judge = None
    
    
    async def run_single(self, eval_case: EvalCase) -> EvalResult:
        """
        Run a single evaluation case.
        
        Args:
            eval_case: The test case to execute
            
        Returns:
            EvalResult with test outcome
        """
        try:
            # Create conversation context
            context: ConversationContext = ConversationContext(
                query=eval_case.input_data.get("query", ""),
                previous_node_output=eval_case.input_data.get("previous_output"),
                metadata=eval_case.input_data.get("metadata")
            )
            
            # Execute the agent node
            result_context: ConversationContext = await self.agent.process(context)
            
            # Extract output
            node_name: str = getattr(self.agent, 'node_name', self.agent.__class__.__name__)
            actual_output: Dict[str, Any] = result_context.get_node_output(node_name)
            
            # If no output in workflow_nodes, try to get from agent directly
            if not actual_output and hasattr(result_context, 'output'):
                actual_output = result_context.output
            
            # Determine validation method
            validation_method: ValidationMethod = eval_case.get_validation_method()
            
            # Get appropriate validator
            validator: Validator = self.validators[validation_method]
            
            # Prepare expected value and context for validation
            if validation_method == ValidationMethod.CRITERIA:
                expected: Any = eval_case.criteria
                validation_context: Dict[str, Any] = eval_case.input_data
            else:
                expected = eval_case.expected_output
                validation_context = None
            
            # Validate output
            passed: bool
            failure_reason: Optional[str]
            passed, failure_reason = await validator.validate(
                actual_output=actual_output,
                expected=expected,
                context=validation_context
            )
            
            # Create result
            result: EvalResult = EvalResult(
                case_name=eval_case.name,
                passed=passed,
                actual_output=actual_output,
                expected_output=eval_case.expected_output,
                validation_method=validation_method,
                failure_reason=failure_reason
            )
            return result
            
        except Exception as e:
            # Handle execution errors
            result: EvalResult = EvalResult(
                case_name=eval_case.name,
                passed=False,
                actual_output={},
                expected_output=eval_case.expected_output,
                validation_method=eval_case.get_validation_method(),
                error=str(e)
            )
            return result
    
    
    async def run_batch(
        self,
        eval_cases: List[EvalCase],
        parallel: bool = True,
        batch_size: int = 10
    ) -> List[EvalResult]:
        """
        Run multiple evaluation cases.
        
        Args:
            eval_cases: List of test cases to execute
            parallel: Whether to run cases in parallel
            batch_size: Number of concurrent executions (if parallel)
            
        Returns:
            List of EvalResult objects
        """
        if not parallel:
            # Sequential execution
            results: List[EvalResult] = []
            for case in eval_cases:
                result: EvalResult = await self.run_single(case)
                results.append(result)
            return results
        
        # Parallel execution in batches
        results: List[EvalResult] = []
        
        for i in range(0, len(eval_cases), batch_size):
            batch: List[EvalCase] = eval_cases[i:i + batch_size]
            
            # Run batch concurrently
            batch_results: List[EvalResult] = await asyncio.gather(
                *[self.run_single(case) for case in batch],
                return_exceptions=False
            )
            
            results.extend(batch_results)
        
        return results
    
    
    def print_summary(self, results: List[EvalResult]) -> None:
        """
        Print a summary of evaluation results.
        
        Args:
            results: List of evaluation results
        """
        try:
            from .utils import print_summary
        except ImportError:
            from utils import print_summary
        print_summary(results)