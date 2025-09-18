#!/usr/bin/env python3
"""
Test runner for sentiment analysis agent demonstrating semantic criteria evaluation.
"""

import asyncio
from typing import Optional, List
import sys

# Import evaluation cases to trigger decorator registration
import evals.cases.sentiment_analysis  # noqa: F401

from evals.registry import EvalRegistry
from evals.runner import EvalRunner
from evals.llm_client_config import get_llm_client_or_exit
from evals.utils import print_summary

# Import agent and models
from src.workflow_nodes.scratchpad.sentiment_analysis_agent import SentimentAnalysisAgent
from src.models.scratchpad_models import TextInput, SentimentAnalysisOutput


async def run_sentiment_analysis_evals(
    llm_client,
    case_names: Optional[List[str]] = None,
    tags: Optional[List[str]] = None,
    limit: Optional[int] = None
):
    """
    Run evaluation cases for SentimentAnalysisAgent.

    Args:
        llm_client: The LLM client to use
        case_names: Optional list of specific case names to run
        tags: Optional list of tags to filter cases by
        limit: Optional limit on number of cases to run

    Returns:
        List of evaluation results
    """
    # Create registry and load cases
    registry = EvalRegistry.for_agent(
        agent_class=SentimentAnalysisAgent,
        input_type=TextInput,
        output_type=SentimentAnalysisOutput
    )

    # Print registry summary
    summary = registry.summary()
    print(f"\n{'='*60}")
    print(f"Sentiment Analysis Evaluation")
    print(f"Agent: {summary['agent']}")
    print(f"Total cases: {summary['total_cases']}")
    print(f"Available tags: {', '.join(sorted(summary['tags']))}")
    print(f"{'='*60}\n")

    # Get cases to run
    if case_names:
        cases = registry.get_cases(names=case_names)
        print(f"Running specific cases: {case_names}")
    elif tags:
        cases = registry.get_cases(tags=tags)
        print(f"Running cases with tags: {tags}")
    else:
        cases = registry.get_all_cases()
        print(f"Running all {len(cases)} cases")

    # Apply limit if specified
    if limit and len(cases) > limit:
        cases = cases[:limit]
        print(f"Limited to {limit} cases")

    if not cases:
        print("No evaluation cases found matching criteria")
        return []

    # Initialize runner with result saving
    runner = EvalRunner(
        agent_class=SentimentAnalysisAgent,
        llm_client=llm_client,
        save_results=True
    )

    # Run evaluations (smaller batch for semantic evaluation)
    print("\nRunning evaluations...")
    results = await runner.run_batch(cases, parallel=False, batch_size=2)

    # Print detailed results
    print_summary(results)

    # Show specific details for semantic evaluation cases
    print("\n" + "="*60)
    print("SEMANTIC EVALUATION DETAILS")
    print("="*60)

    for result in results:
        # Find the original case to check if it had Criteria validation (semantic)
        matching_case = next((c for c in cases if c.name == result.case_name), None)
        if matching_case and matching_case.field_validations:
            # Check if any field uses Criteria validator
            from evals.field_validators import Criteria
            has_criteria = any(
                isinstance(v, Criteria)
                for v in matching_case.field_validations.values()
            )
            if has_criteria:
                print(f"\n📝 {result.case_name}")
                print(f"   Status: {'✅ PASSED' if result.passed else '❌ FAILED'}")
                if result.actual_output:
                    # Handle both dict and Pydantic model outputs
                    if isinstance(result.actual_output, dict):
                        sentiment = result.actual_output.get('sentiment', 'N/A')
                        reasoning = result.actual_output.get('reasoning', 'N/A')
                    else:
                        sentiment = getattr(result.actual_output, 'sentiment', 'N/A')
                        reasoning = getattr(result.actual_output, 'reasoning', 'N/A')
                    print(f"   Sentiment: {sentiment}")
                    print(f"   Reasoning: {reasoning}")
                if not result.passed and result.failure_reason:
                    print(f"   Failure: {result.failure_reason}")

    # Print cost summary
    total_cost = sum(r.llm_cost or 0 for r in results)
    print(f"\n{'='*60}")
    print(f"Total LLM Cost: ${total_cost:.6f}")
    print(f"Average Cost per Case: ${total_cost/len(results):.6f}")
    print(f"{'='*60}\n")

    return results


async def main():
    """Main entry point."""
    # Get LLM client
    llm_client = get_llm_client_or_exit()

    # Parse command line arguments
    args = sys.argv[1:]

    case_names = None
    tags = None
    limit = None

    # Simple argument parsing
    if args:
        if "--tags" in args:
            idx = args.index("--tags")
            if idx + 1 < len(args):
                tags = args[idx + 1].split(",")
        elif "--cases" in args:
            idx = args.index("--cases")
            if idx + 1 < len(args):
                case_names = args[idx + 1].split(",")
        elif "--limit" in args:
            idx = args.index("--limit")
            if idx + 1 < len(args):
                limit = int(args[idx + 1])
        elif args[0].isdigit():
            limit = int(args[0])

    # Run evaluations
    results = await run_sentiment_analysis_evals(
        llm_client,
        case_names=case_names,
        tags=tags,
        limit=limit
    )

    # Return appropriate exit code
    failed_count = sum(1 for r in results if not r.passed)
    sys.exit(1 if failed_count > 0 else 0)


if __name__ == "__main__":
    asyncio.run(main())