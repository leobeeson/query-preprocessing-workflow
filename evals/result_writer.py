"""
Result writer for persisting evaluation results to disk.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

from evals.core import EvalResult


class ResultWriter:
    """
    Handles writing evaluation results to disk in JSONL and JSON formats.
    """

    def __init__(self, agent_name: str, results_dir: Optional[Path] = None):
        """
        Initialize the result writer.

        Args:
            agent_name: Name of the agent being evaluated
            results_dir: Optional base directory for results (defaults to evals/results)
        """
        self.agent_name = agent_name
        self.timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        if results_dir is None:
            results_dir = Path(__file__).parent / "results"

        # Create agent-specific directory
        self.results_dir = results_dir / agent_name
        self.results_dir.mkdir(parents=True, exist_ok=True)

        # Initialize file paths with timestamp as filename
        self.results_file = self.results_dir / f"{self.timestamp}.jsonl"
        self.summary_file = self.results_dir / f"{self.timestamp}_summary.json"

        # Track results for summary
        self.all_results: List[EvalResult] = []

    def write_result(self, result: EvalResult) -> None:
        """
        Append a single result to the JSONL file.

        Args:
            result: EvalResult to write
        """
        # Store for summary
        self.all_results.append(result)

        # Convert to dict and ensure JSON serializable
        result_dict = result.model_dump()

        # Remove raw_response fields from actual_output and expected_output if they exist
        if isinstance(result_dict.get('actual_output'), dict) and 'raw_response' in result_dict['actual_output']:
            del result_dict['actual_output']['raw_response']

        if isinstance(result_dict.get('expected_output'), dict) and 'raw_response' in result_dict['expected_output']:
            del result_dict['expected_output']['raw_response']

        # Convert any datetime objects to ISO format strings
        for key, value in result_dict.items():
            if isinstance(value, datetime):
                result_dict[key] = value.isoformat()

        # Append to JSONL file
        with open(self.results_file, "a", encoding="utf-8") as f:
            json.dump(result_dict, f, ensure_ascii=False)
            f.write("\n")

    def write_summary(
        self,
        results: List[EvalResult],
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Write summary statistics to JSON file.

        Args:
            results: List of all evaluation results
            metadata: Optional metadata about the run (model, config, etc.)
        """
        if not results:
            results = self.all_results

        # Calculate statistics
        total_cases = len(results)
        passed = sum(1 for r in results if r.passed)
        failed = total_cases - passed
        pass_rate = (passed / total_cases * 100) if total_cases > 0 else 0

        # Calculate total duration
        total_duration_ms = sum(
            r.duration_ms for r in results
            if hasattr(r, 'duration_ms') and r.duration_ms
        )

        # Calculate total costs
        total_cost = sum(
            r.llm_cost for r in results
            if hasattr(r, 'llm_cost') and r.llm_cost
        )

        # Calculate token statistics
        total_input_tokens = sum(
            r.input_tokens for r in results
            if hasattr(r, 'input_tokens') and r.input_tokens
        )

        total_output_tokens = sum(
            r.output_tokens for r in results
            if hasattr(r, 'output_tokens') and r.output_tokens
        )

        # Calculate cache token statistics
        total_cache_write_tokens = sum(
            r.cache_write_tokens for r in results
            if hasattr(r, 'cache_write_tokens') and r.cache_write_tokens
        )

        total_cache_read_tokens = sum(
            r.cache_read_tokens for r in results
            if hasattr(r, 'cache_read_tokens') and r.cache_read_tokens
        )

        # Calculate cache costs
        total_cache_write_cost = sum(
            r.cache_write_cost for r in results
            if hasattr(r, 'cache_write_cost') and r.cache_write_cost
        )

        total_cache_read_cost = sum(
            r.cache_read_cost for r in results
            if hasattr(r, 'cache_read_cost') and r.cache_read_cost
        )

        # Calculate averages (only count cases that have token data)
        cases_with_tokens = sum(
            1 for r in results
            if hasattr(r, 'input_tokens') and r.input_tokens
        )

        avg_input_tokens = (
            round(total_input_tokens / cases_with_tokens, 2)
            if cases_with_tokens > 0 else 0
        )

        avg_output_tokens = (
            round(total_output_tokens / cases_with_tokens, 2)
            if cases_with_tokens > 0 else 0
        )

        # Calculate averages for cache tokens
        cases_with_cache = sum(
            1 for r in results
            if hasattr(r, 'cache_write_tokens') and r.cache_write_tokens is not None
        )

        avg_cache_write_tokens = (
            round(total_cache_write_tokens / cases_with_cache, 2)
            if cases_with_cache > 0 else 0
        )

        avg_cache_read_tokens = (
            round(total_cache_read_tokens / cases_with_cache, 2)
            if cases_with_cache > 0 else 0
        )

        # Build summary
        summary = {
            "agent": self.agent_name,
            "timestamp": datetime.now().isoformat(),
            "total_cases": total_cases,
            "passed": passed,
            "failed": failed,
            "pass_rate": round(pass_rate, 2),
            "total_duration_ms": total_duration_ms,
            "average_duration_ms_per_case": round(total_duration_ms / total_cases, 2) if total_cases > 0 else 0,
            "total_cost_usd": round(total_cost, 6),
            "average_cost_per_case": round(total_cost / total_cases, 6) if total_cases > 0 else 0,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "average_input_tokens_per_case": avg_input_tokens,
            "average_output_tokens_per_case": avg_output_tokens,
            "total_cache_write_tokens": total_cache_write_tokens,
            "total_cache_read_tokens": total_cache_read_tokens,
            "average_cache_write_tokens_per_case": avg_cache_write_tokens,
            "average_cache_read_tokens_per_case": avg_cache_read_tokens,
            "total_cache_write_cost": round(total_cache_write_cost, 6),
            "total_cache_read_cost": round(total_cache_read_cost, 6),
        }

        # Add metadata if provided
        if metadata:
            summary["configuration"] = metadata

        # Add failure details
        failed_cases = [
            {
                "name": r.case_name,
                "reason": r.failure_reason or r.error
            }
            for r in results if not r.passed
        ]
        if failed_cases:
            summary["failed_cases"] = failed_cases

        # Write summary file
        with open(self.summary_file, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)

    def get_results_path(self) -> Path:
        """
        Get the path to the results directory.

        Returns:
            Path to results directory
        """
        return self.results_dir

    def get_summary_path(self) -> Path:
        """
        Get the path to the summary file.

        Returns:
            Path to summary file
        """
        return self.summary_file