#!/usr/bin/env python3
"""
Runner for QueryCharacteristicsExtractionAgent evaluation cases using the decorator pattern.
"""

import asyncio
from typing import Any, Dict, Optional, List

# Import evaluation cases at top level to trigger decorator registration
import evals.cases.query_characteristics_extraction  # noqa: F401

from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from evals.core import EvalCase, EvalResult
from evals.registry import EvalRegistry
from evals.runner import EvalRunner
from evals.llm_client_config import get_llm_client_or_exit

# Import agent and models
from src.workflow_nodes.query_preprocessing.query_characteristics_extraction_agent import QueryCharacteristicsExtractionAgent
from src.models.query_characteristics_models import QueryCharacteristicsInput, QueryCharacteristicsOutput


async def run_query_characteristics_evals(
    llm_client: LLMClientInterface,
    case_names: Optional[List[str]] = None,
    tags: Optional[List[str]] = None
) -> List[EvalResult]:
    """
    Run evaluation cases for QueryCharacteristicsExtractionAgent.

    Args:
        llm_client: The LLM client to use
        case_names: Optional list of specific case names to run
        tags: Optional list of tags to filter cases by

    Returns:
        List of evaluation results
    """
    # Create registry and load cases
    registry = EvalRegistry.for_agent(
        agent_class=QueryCharacteristicsExtractionAgent,
        input_type=QueryCharacteristicsInput,
        output_type=QueryCharacteristicsOutput
    )

    # Print registry summary
    summary: Dict[str, Any] = registry.summary()
    print(f"\n{'='*60}")
    print(f"Evaluation Registry Summary")
    print(f"Agent: {summary['agent']}")
    print(f"Total cases: {summary['total_cases']}")
    print(f"Available tags: {', '.join(summary['tags'])}")
    print(f"{'='*60}\n")

    # Get cases to run
    if case_names:
        cases: List[EvalCase] = registry.get_cases(names=case_names)
        print(f"Running specific cases: {case_names}")
    elif tags:
        cases: List[EvalCase] = registry.get_cases(tags=tags)
        print(f"Running cases with tags: {tags}")
    else:
        cases: List[EvalCase] = registry.get_all_cases()
        print(f"Running all {len(cases)} cases")

    if not cases:
        print("No evaluation cases found matching criteria")
        return []

    # Initialize runner with result saving enabled
    runner = EvalRunner(
        agent_class=QueryCharacteristicsExtractionAgent,
        llm_client=llm_client,
        save_results=True  # Enable saving results to disk
    )

    # Run evaluations with smaller batch size to avoid rate limits
    results: List[EvalResult] = await runner.run_batch(cases, parallel=True, batch_size=3)

    # Print results summary
    passed: int = sum(1 for r in results if r.passed)
    failed: int = sum(1 for r in results if not r.passed)

    # Calculate total costs
    total_cost: float = sum(r.llm_cost for r in results if r.llm_cost)
    avg_cost: float = total_cost / len(results) if results else 0

    print(f"\n{'='*60}")
    print(f"Evaluation Results")
    print(f"Passed: {passed}/{len(results)}")
    print(f"Failed: {failed}/{len(results)}")
    print(f"Pass Rate: {(passed/len(results)*100):.1f}%")
    print(f"Total LLM Cost: ${total_cost:.6f}")
    print(f"Average Cost per Case: ${avg_cost:.6f}")
    print(f"{'='*60}\n")

    # Print failures
    if failed > 0:
        print("Failed cases:")
        for result in results:
            if not result.passed:
                print(f"  - {result.case_name}: {result.failure_reason or result.error}")

    return results


async def main():
    """Main entry point."""
    # Get LLM client from centralized config
    llm_client: LLMClientInterface = get_llm_client_or_exit()

    # Run all evaluations
    results: List[EvalResult] = await run_query_characteristics_evals(llm_client)

    # Example: Run only specific tags
    # results = await run_query_characteristics_evals(
    #     llm_client,
    #     tags=["aggregation", "feasible"]
    # )

    # Example: Run specific cases
    # results = await run_query_characteristics_evals(
    #     llm_client,
    #     case_names=["simple_aggregation_transport", "grouped_ranking_merchants"]
    # )

    # Example: Run only infeasible cases
    # results = await run_query_characteristics_evals(
    #     llm_client,
    #     tags=["infeasible"]
    # )

    return results


if __name__ == "__main__":
    asyncio.run(main())
