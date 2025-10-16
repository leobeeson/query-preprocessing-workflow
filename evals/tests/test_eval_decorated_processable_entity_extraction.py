#!/usr/bin/env python3
"""
Runner for evaluation cases using the decorator pattern.
"""

import argparse
import asyncio
from typing import Any, Dict, Optional, List

# Import evaluation cases at top level to trigger decorator registration
import evals.cases.processable_entity_extraction  # noqa: F401

from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from evals.core import EvalCase, EvalResult
from evals.registry import EvalRegistry
from evals.runner import EvalRunner
from evals.llm_client_config import get_llm_client_or_exit

# Import agent and models
from src.workflow_nodes.query_preprocessing.processable_entity_extraction_agent import ProcessableEntityExtractionAgent
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import ProcessableEntityExtractionOutput


async def run_processable_entity_extraction_evals(
    llm_client: LLMClientInterface,
    case_names: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
    tags_match_all: bool = True
) -> List[EvalResult]:
    """
    Run evaluation cases for ProcessableEntityExtractionAgent.

    Args:
        llm_client: The LLM client to use
        case_names: Optional list of specific case names to run
        tags: Optional list of tags to filter cases by
        tags_match_all: If True, cases must have ALL tags (AND). If False, cases with ANY tag (OR).

    Returns:
        List of evaluation results
    """
    # Create registry and load cases
    registry = EvalRegistry.for_agent(
        agent_class=ProcessableEntityExtractionAgent,
        input_type=QueryInput,
        output_type=ProcessableEntityExtractionOutput
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
        if tags_match_all:
            # For AND logic, we need to filter cases that have ALL specified tags
            # The registry stores metadata on the function objects
            matching_cases: List[EvalCase] = []

            # Get all cases and check their metadata
            for name, func in registry._functions.items():
                metadata: Dict[str, Any] = getattr(func, "eval_metadata", {})
                case_tags: List[str] = metadata.get("tags", [])

                # Check if this case has ALL the required tags
                if all(tag in case_tags for tag in tags):
                    case: Optional[EvalCase] = registry.get_case(name)
                    if case:
                        matching_cases.append(case)

            cases: List[EvalCase] = matching_cases
            print(f"Running cases with ALL tags: {tags} (AND logic)")
            print(f"Filtered cases: {len(cases)} out of {summary['total_cases']} total")
        else:
            # Get cases with ANY of the tags (default registry behavior)
            cases: List[EvalCase] = registry.get_cases(tags=tags)
            print(f"Running cases with ANY tags: {tags} (OR logic)")
            print(f"Filtered cases: {len(cases)} out of {summary['total_cases']} total")
    else:
        cases: List[EvalCase] = registry.get_all_cases()
        print(f"Running all {len(cases)} cases")

    if not cases:
        print("No evaluation cases found matching criteria")
        return []

    # Initialize runner with result saving enabled
    runner = EvalRunner(
        agent_class=ProcessableEntityExtractionAgent,
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


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run evaluation cases for ProcessableEntityExtractionAgent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all tests
  python -m evals.tests.test_eval_decorated_processable_entity_extraction

  # Run tests with a single tag
  python -m evals.tests.test_eval_decorated_processable_entity_extraction --tags merchant

  # Run tests that have ALL specified tags (AND logic)
  python -m evals.tests.test_eval_decorated_processable_entity_extraction --tags merchant basic

  # Run tests with specific case names
  python -m evals.tests.test_eval_decorated_processable_entity_extraction --cases basic_merchant amount_threshold

Available tags:
  Check the registry summary when running to see all available tags
        """
    )

    parser.add_argument(
        "--tags",
        nargs="+",
        help="Run cases that have ALL specified tags (AND logic). Example: --tags merchant basic"
    )

    parser.add_argument(
        "--cases",
        nargs="+",
        help="Run specific cases by name. Example: --cases basic_merchant amount_threshold"
    )

    return parser.parse_args()


async def main() -> List[EvalResult]:
    """Main entry point."""
    # Parse command-line arguments
    args = parse_arguments()

    # Get LLM client from centralized config
    llm_client: LLMClientInterface = get_llm_client_or_exit()

    # Run evaluations based on arguments
    if args.cases:
        # Run specific cases by name
        results: List[EvalResult] = await run_processable_entity_extraction_evals(
            llm_client,
            case_names=args.cases
        )
    elif args.tags:
        # Run cases with specified tags (AND logic)
        results: List[EvalResult] = await run_processable_entity_extraction_evals(
            llm_client,
            tags=args.tags,
            tags_match_all=True  # Use AND logic for multiple tags
        )
    else:
        # Run all evaluations
        results: List[EvalResult] = await run_processable_entity_extraction_evals(llm_client)

    return results


if __name__ == "__main__":
    asyncio.run(main())