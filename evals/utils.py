"""
Utility functions for the evaluation framework.
"""

from typing import Any, Dict, List
from .core import EvalResult, ValidationMethod


def create_summary(results: List[EvalResult]) -> Dict[str, Any]:
    """
    Create a summary of evaluation results.
    
    Args:
        results: List of evaluation results
        
    Returns:
        Dictionary with summary statistics
    """
    total: int = len(results)
    passed: int = sum(1 for r in results if r.passed)
    failed: int = total - passed
    
    # Group failures by validation method
    failures_by_method: Dict[ValidationMethod, List[EvalResult]] = {}
    for result in results:
        if not result.passed and result.validation_method:
            if result.validation_method not in failures_by_method:
                failures_by_method[result.validation_method] = []
            failures_by_method[result.validation_method].append(result)
    
    # Collect all failed cases
    failed_cases: List[EvalResult] = [r for r in results if not r.passed]
    
    summary: Dict[str, Any] = {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": (passed / total * 100) if total > 0 else 0,
        "failures_by_method": {
            method.value: len(cases) 
            for method, cases in failures_by_method.items()
        },
        "failed_cases": failed_cases
    }
    
    return summary


def print_summary(results: List[EvalResult]) -> None:
    """
    Print a formatted summary of evaluation results.
    
    Args:
        results: List of evaluation results
    """
    summary: Dict[str, Any] = create_summary(results)
    
    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)
    
    print(f"Total tests: {summary['total']}")
    print(f"Passed: {summary['passed']}")
    print(f"Failed: {summary['failed']}")
    print(f"Pass rate: {summary['pass_rate']:.1f}%")
    
    if summary['failures_by_method']:
        print("\nFailures by validation method:")
        for method, count in summary['failures_by_method'].items():
            print(f"  {method}: {count}")
    
    if summary['failed_cases']:
        print("\n" + "=" * 60)
        print(f"FAILED CASES ({summary['failed']})")
        print("=" * 60)
        
        for result in summary['failed_cases']:
            print(f"\n❌ {result.case_name}")
            if result.error:
                print(f"   Error: {result.error}")
            elif result.failure_reason:
                print(f"   Reason: {result.failure_reason}")
            
            if result.expected_output is not None:
                print(f"   Expected: {result.expected_output}")
                print(f"   Actual: {result.actual_output}")
    
    print("\n" + "=" * 60 + "\n")


def format_test_report(results: List[EvalResult]) -> str:
    """
    Format a detailed test report.
    
    Args:
        results: List of evaluation results
        
    Returns:
        Formatted report string
    """
    lines: List[str] = []
    
    lines.append("# Evaluation Test Report")
    lines.append("")
    
    # Summary section
    summary: Dict[str, Any] = create_summary(results)
    lines.append("## Summary")
    lines.append(f"- Total tests: {summary['total']}")
    lines.append(f"- Passed: {summary['passed']}")
    lines.append(f"- Failed: {summary['failed']}")
    lines.append(f"- Pass rate: {summary['pass_rate']:.1f}%")
    lines.append("")
    
    # Passed tests
    passed_results: List[EvalResult] = [r for r in results if r.passed]
    if passed_results:
        lines.append("## Passed Tests")
        for result in passed_results:
            lines.append(f"- ✅ {result.case_name}")
        lines.append("")
    
    # Failed tests with details
    failed_results: List[EvalResult] = [r for r in results if not r.passed]
    if failed_results:
        lines.append("## Failed Tests")
        for result in failed_results:
            lines.append(f"\n### ❌ {result.case_name}")
            
            if result.validation_method:
                lines.append(f"**Validation Method:** {result.validation_method.value}")
            
            if result.error:
                lines.append(f"**Error:** {result.error}")
            elif result.failure_reason:
                lines.append(f"**Failure Reason:** {result.failure_reason}")
            
            if result.expected_output is not None:
                lines.append(f"**Expected:** `{result.expected_output}`")
                lines.append(f"**Actual:** `{result.actual_output}`")
        lines.append("")
    
    return "\n".join(lines)