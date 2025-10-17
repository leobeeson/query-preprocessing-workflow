"""
Test runner for executing evaluations.
"""

import asyncio
import random
import time
from datetime import datetime
from pathlib import Path
from typing import Any, List, Optional, Type, TypeVar, Generic

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from pydantic import BaseModel

try:
    # Try relative imports first (when used as a package)
    from .core import EvalCase, EvalResult
    from .evaluator import Evaluator
except ImportError:
    # Fall back to absolute imports (when running directly)
    from core import EvalCase, EvalResult
    from evaluator import Evaluator

# Type variables for agent input/output
TInput = TypeVar('TInput', bound=BaseModel)
TOutput = TypeVar('TOutput', bound=BaseModel)


class EvalRunner(Generic[TInput, TOutput]):
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
        agent_class: Type[AgentNodeBase[TInput, TOutput]],
        llm_client: LLMClientInterface,
        model_name: Optional[str] = None,
        default_field_name: Optional[str] = None,
        use_judge_for_criteria: bool = True,
        max_retries: int = 3,
        initial_retry_delay: float = 1.0,
        batch_delay_seconds: float = 5.0,
        sequential_delay_seconds: float = 2,
        jitter_factor: float = 0.1,
        save_results: bool = True,
        results_dir: Optional[Path] = None
    ):
        """
        Initialize the evaluation runner.

        Args:
            agent_class: The agent node class to test (must inherit from AgentNodeBase)
            llm_client: LLM client for the agent (must implement LLMClientInterface)
            model_name: Optional model name override
            default_field_name: Default field to extract from output
            use_judge_for_criteria: Whether to use LLM-as-a-Judge for criteria
            max_retries: Maximum number of retries for rate-limited requests
            initial_retry_delay: Initial delay in seconds for retry backoff
            batch_delay_seconds: Delay between batches to avoid rate limits
            sequential_delay_seconds: Delay between sequential requests (non-parallel mode)
            jitter_factor: Random jitter factor (0.0-1.0) for retry delays to prevent thundering herd
            save_results: Whether to save results to disk
            results_dir: Optional directory for saving results
        """
        self.agent_class: Type[AgentNodeBase[TInput, TOutput]] = agent_class
        self.llm_client: LLMClientInterface = llm_client
        # Get the actual model name from the LLM client
        self.actual_model_name: str = getattr(llm_client, 'model', 'unknown')
        self.model_name: Optional[str] = model_name
        self.default_field_name: Optional[str] = default_field_name
        self.max_retries: int = max_retries
        self.initial_retry_delay: float = initial_retry_delay
        self.batch_delay_seconds: float = batch_delay_seconds
        self.sequential_delay_seconds: float = sequential_delay_seconds
        self.jitter_factor: float = jitter_factor
        self.save_results: bool = save_results
        self.results_dir: Optional[Path] = results_dir

        # Initialize agent instance
        # AgentNodeBase constructor requires llm_client and optionally model_name
        if model_name:
            self.agent = agent_class(
                llm_client=llm_client,
                model_name=model_name
            )
        else:
            self.agent = agent_class(
                llm_client=llm_client
            )

        # Initialize the evaluator
        judge_client = llm_client if use_judge_for_criteria else None
        self.evaluator = Evaluator(judge_client=judge_client)

        # Initialize result writer if saving results
        self.result_writer = None
        if self.save_results:
            from evals.result_writer import ResultWriter
            self.result_writer = ResultWriter(
                agent_name=agent_class.__name__,
                results_dir=results_dir
            )
    
    
    async def run_single_with_summary(self, eval_case: EvalCase) -> EvalResult:
        """
        Run a single evaluation case and write summary.

        This is the public interface for running a single test case.
        It ensures that results and summary are saved.

        Args:
            eval_case: The test case to execute

        Returns:
            EvalResult with test outcome
        """
        result = await self.run_single(eval_case)

        # Write summary if saving results
        if self.result_writer:
            metadata = {
                "model": self.actual_model_name,
                "batch_size": 1,
                "max_retries": self.max_retries,
                "parallel": False
            }
            self.result_writer.write_summary([result], metadata)

            # Print results path
            print(f"\n📁 Results saved to: {self.result_writer.get_results_path()}")
            print(f"📊 Summary: {self.result_writer.get_summary_path()}")

        return result

    async def run_single(self, eval_case: EvalCase) -> EvalResult:
        """
        Run a single evaluation case with retry logic for rate limits.

        Args:
            eval_case: The test case to execute

        Returns:
            EvalResult with test outcome
        """
        retry_count = 0
        delay = self.initial_retry_delay

        while retry_count <= self.max_retries:
            try:
                # Track timing
                start_time = time.perf_counter()
                timestamp = datetime.now().isoformat()

                # Directly call agent.process with typed input
                actual_output: Any = await self.agent.process(eval_case.input_data)

                # Calculate duration
                duration_ms = (time.perf_counter() - start_time) * 1000

                # Get LLM metrics from agent
                metrics = self.agent.get_last_metrics() if hasattr(self.agent, 'get_last_metrics') else None

                # Validate output using evaluator
                passed: bool
                failure_reason: Optional[str]

                # Validate using field_validations with equality fallback
                passed, failure_reason = await self.evaluator.validate(
                    actual=actual_output,
                    expected_output=eval_case.expected_output,
                    field_validations=eval_case.field_validations
                )

                # Create result with metrics
                result: EvalResult = EvalResult(
                    case_name=eval_case.name,
                    passed=passed,
                    input=eval_case.input_data,
                    expected_output=eval_case.expected_output,
                    actual_output=actual_output,
                    failure_reason=failure_reason,
                    model_name=self.actual_model_name,
                    timestamp=timestamp,
                    duration_ms=duration_ms,
                    llm_cost=metrics.total_cost if metrics else None,
                    input_tokens=metrics.input_tokens if metrics else None,
                    output_tokens=metrics.output_tokens if metrics else None,
                    cache_write_tokens=metrics.cache_write_tokens if metrics else None,
                    cache_read_tokens=metrics.cache_read_tokens if metrics else None,
                    cache_write_cost=metrics.cache_write_cost if metrics else None,
                    cache_read_cost=metrics.cache_read_cost if metrics else None
                )

                # Save result if configured
                if self.result_writer:
                    self.result_writer.write_result(result)

                return result

            except Exception as e:
                error_str = str(e)

                # Check if it's a rate limit error (429)
                if "429" in error_str or "rate_limit_error" in error_str:
                    if retry_count < self.max_retries:
                        # Add jitter to prevent thundering herd
                        jitter = random.uniform(0, delay * self.jitter_factor)
                        sleep_time = delay + jitter

                        print(f"Rate limit hit for {eval_case.name}, retrying in {sleep_time:.1f}s (attempt {retry_count + 1}/{self.max_retries})")
                        await asyncio.sleep(sleep_time)

                        # Exponential backoff
                        delay *= 2
                        retry_count += 1
                        continue

                # Handle execution errors or max retries exceeded
                result: EvalResult = EvalResult(
                    case_name=eval_case.name,
                    passed=False,
                    input=eval_case.input_data,
                    expected_output=eval_case.expected_output,
                    actual_output=None,
                    error=error_str,
                    model_name=self.actual_model_name,
                    timestamp=datetime.now().isoformat()
                )

                # Save failed result if configured
                if self.result_writer:
                    self.result_writer.write_result(result)

                return result

        # This shouldn't be reached, but just in case
        result = EvalResult(
            case_name=eval_case.name,
            passed=False,
            input=eval_case.input_data,
            expected_output=eval_case.expected_output,
            actual_output=None,
            error="Max retries exceeded",
            model_name=self.actual_model_name,
            timestamp=datetime.now().isoformat()
        )

        # Save failed result if configured
        if self.result_writer:
            self.result_writer.write_result(result)

        return result
    
    
    async def run_batch(
        self,
        eval_cases: List[EvalCase],
        parallel: bool = True,
        batch_size: int = 5
    ) -> List[EvalResult]:
        """
        Run multiple evaluation cases with delays between batches.

        Args:
            eval_cases: List of test cases to execute
            parallel: Whether to run cases in parallel
            batch_size: Number of concurrent executions (if parallel), reduced to 5 to avoid rate limits

        Returns:
            List of EvalResult objects
        """
        if not parallel:
            # Sequential execution with configurable delay between each
            results: List[EvalResult] = []
            for i, case in enumerate(eval_cases):
                result: EvalResult = await self.run_single(case)
                results.append(result)
                # Add configurable delay between sequential requests
                if i < len(eval_cases) - 1:
                    await asyncio.sleep(self.sequential_delay_seconds)
            return results

        # Parallel execution in batches with delays
        results: List[EvalResult] = []
        total_batches = (len(eval_cases) + batch_size - 1) // batch_size

        for batch_num, i in enumerate(range(0, len(eval_cases), batch_size)):
            batch: List[EvalCase] = eval_cases[i:i + batch_size]

            print(f"Running batch {batch_num + 1}/{total_batches} ({len(batch)} cases)")

            # Run batch concurrently
            batch_results: List[EvalResult] = await asyncio.gather(
                *[self.run_single(case) for case in batch],
                return_exceptions=False
            )

            results.extend(batch_results)

            # Add delay between batches to avoid rate limits (except after last batch)
            if batch_num < total_batches - 1:
                print(f"Waiting {self.batch_delay_seconds}s before next batch...")
                await asyncio.sleep(self.batch_delay_seconds)

        # Write summary if saving results
        if self.result_writer:
            metadata = {
                "model": self.actual_model_name,
                "batch_size": batch_size,
                "max_retries": self.max_retries,
                "parallel": parallel
            }
            self.result_writer.write_summary(results, metadata)

            # Print results path
            print(f"\n📁 Results saved to: {self.result_writer.get_results_path()}")
            print(f"📊 Summary: {self.result_writer.get_summary_path()}")

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