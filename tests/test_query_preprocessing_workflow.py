#!/usr/bin/env python3
"""
Test script for QueryPreprocessingWorkflow
Tests concurrent execution, error handling, and metrics aggregation
"""

import asyncio
import os
from dotenv import load_dotenv
from typing import Dict, Any

from src.clients.llm_clients.anthropic_llm_client import AnthropicLLMClient
from src.workflows.query_preprocessing_workflow import QueryPreprocessingWorkflow
from src.workflows.exceptions import (
    InsecureQueryError,
    InvalidQueryError,
    UnprocessableEntityError,
    NoProcessableEntitiesError
)
from src.core_nodes.metrics_aggregator import MetricsAggregator


async def test_workflow():
    """Test the QueryPreprocessingWorkflow with various scenarios"""
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables")
        print("Please create a .env file with your API key")
        return
    
    # Initialize
    llm_client = AnthropicLLMClient(api_key=api_key)
    workflow = QueryPreprocessingWorkflow(llm_client=llm_client)
    
    # Test cases covering all scenarios
    test_cases = [
        # Success cases
        {
            "query": "Show me Tesco groceries over £50 last month",
            "expected": "success",
            "description": "Valid query with multiple entities"
        },
        {
            "query": "Netflix and Spotify subscriptions this year",
            "expected": "success",
            "description": "Valid query with merchants and temporal"
        },
        {
            "query": "Weekend spending on entertainment",
            "expected": "success",
            "description": "Valid query with category normalization"
        },
        
        # Failure cases
        {
            "query": "DROP TABLE users; SELECT * FROM accounts",
            "expected": "insecure",
            "description": "SQL injection attempt"
        },
        {
            "query": "What's the weather today?",
            "expected": "invalid",
            "description": "Non-banking query"
        },
        {
            "query": "Show me credit card 4532-1234-5678-9012 transactions",
            "expected": "unprocessable",
            "description": "Query with PII (critical unprocessable)"
        },
        {
            "query": "How much did I spend?",
            "expected": "no_entities",
            "description": "Query with no extractable entities"
        },
        
        # Edge cases
        {
            "query": "Group by category and sort by amount",
            "expected": "success",
            "description": "Entity class references"
        },
        {
            "query": "Transactions between £20 and £100 at supermarkets",
            "expected": "success",
            "description": "Amount range with category"
        },
        {
            "query": "Carbon footprint from transport purchases",
            "expected": "success",
            "description": "Environmental tracking query"
        }
    ]
    
    print("=" * 80)
    print("QUERY PREPROCESSING WORKFLOW TEST")
    print("=" * 80)
    print(f"\nRunning {len(test_cases)} test scenarios...")
    print("=" * 80)
    
    success_count = 0
    expected_failures = 0
    unexpected_failures = 0
    global_metrics = MetricsAggregator()
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n[{i}/{len(test_cases)}] {test_case['description']}")
        print(f"📝 Query: \"{test_case['query']}\"")
        print("-" * 60)
        
        try:
            # Process the query
            result = await workflow.process(test_case['query'])
            
            if test_case["expected"] == "success":
                print("✅ SUCCESS - Query processed successfully")
                print(f"   • Processable entities: {len(result.processable_entities)}")
                print(f"   • Normalised categories: {len(result.normalised_categories)}")
                print(f"   • Unprocessable entities: {len(result.unprocessable_entities)}")
                print(f"   • Time: {result.total_time_ms:.0f}ms")
                print(f"   • Cost: ${result.get_total_cost():.6f}")
                print(f"   • Agents run: {len(result.metrics)}")
                
                # Add metrics to aggregator
                for agent_name, metrics in result.metrics.items():
                    global_metrics.add_metrics(agent_name, metrics)
                
                success_count += 1
            else:
                print(f"❌ UNEXPECTED SUCCESS - Expected {test_case['expected']} but got success")
                unexpected_failures += 1
                
        except InsecureQueryError as e:
            if test_case["expected"] == "insecure":
                print(f"✅ EXPECTED FAILURE - Security validation failed")
                print(f"   Reason: {e.justification}")
                expected_failures += 1
            else:
                print(f"❌ UNEXPECTED InsecureQueryError: {e}")
                unexpected_failures += 1
                
        except InvalidQueryError as e:
            if test_case["expected"] == "invalid":
                print(f"✅ EXPECTED FAILURE - Intent validation failed")
                print(f"   Reason: {e.justification}")
                expected_failures += 1
            else:
                print(f"❌ UNEXPECTED InvalidQueryError: {e}")
                unexpected_failures += 1
                
        except UnprocessableEntityError as e:
            if test_case["expected"] == "unprocessable":
                print(f"✅ EXPECTED FAILURE - Critical unprocessable entities")
                print(f"   Entities: {e.entities}")
                expected_failures += 1
            else:
                print(f"❌ UNEXPECTED UnprocessableEntityError: {e}")
                unexpected_failures += 1
                
        except NoProcessableEntitiesError as e:
            if test_case["expected"] == "no_entities":
                print(f"✅ EXPECTED FAILURE - No processable entities found")
                expected_failures += 1
            else:
                print(f"❌ UNEXPECTED NoProcessableEntitiesError: {e}")
                unexpected_failures += 1
                
        except Exception as e:
            print(f"❌ UNEXPECTED ERROR: {type(e).__name__}: {e}")
            unexpected_failures += 1
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    print(f"✅ Successful queries: {success_count}")
    print(f"✅ Expected failures: {expected_failures}")
    if unexpected_failures > 0:
        print(f"❌ Unexpected failures: {unexpected_failures}")
    print(f"📊 Total tests: {len(test_cases)}")
    print(f"📊 Pass rate: {((success_count + expected_failures)/len(test_cases))*100:.1f}%")
    print("=" * 80)
    
    # Display metrics for successful runs
    if global_metrics.get_summary()['total_calls'] > 0:
        print("\n" + global_metrics.format_summary())
        
        # Workflow-specific insights
        summary = global_metrics.get_summary()
        print("\n" + "=" * 60)
        print("WORKFLOW PERFORMANCE INSIGHTS")
        print("=" * 60)
        
        # Calculate average workflow cost (sum of all agents per query)
        avg_agents_per_query = len(summary['agents'])  # Approximate
        avg_workflow_cost = summary['total_cost'] / (summary['total_calls'] / avg_agents_per_query) if summary['total_calls'] > 0 else 0
        
        print(f"💵 Estimated cost per complete workflow: ${avg_workflow_cost:.6f}")
        print(f"⚡ Average agent response time: {summary['avg_response_time_ms']:.0f}ms")
        print(f"🔄 Total agent invocations: {summary['total_calls']}")
        
        # Agent-specific breakdown
        print("\n" + "-" * 60)
        print("AGENT BREAKDOWN:")
        print("-" * 60)
        
        for agent in summary['agents']:
            avg_cost = agent['total_cost'] / agent['total_calls'] if agent['total_calls'] > 0 else 0
            print(f"• {agent['agent_name']:30}")
            print(f"  Calls: {agent['total_calls']:3} | Avg Cost: ${avg_cost:.6f} | Avg Time: {agent['avg_response_time_ms']:.0f}ms")
        
        print("=" * 60)


async def test_concurrent_execution():
    """Test that agents actually run concurrently"""
    
    print("\n" + "=" * 80)
    print("CONCURRENT EXECUTION TEST")
    print("=" * 80)
    
    # Load environment
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found")
        return
    
    llm_client = AnthropicLLMClient(api_key=api_key)
    workflow = QueryPreprocessingWorkflow(llm_client=llm_client)
    
    query = "Show me Tesco groceries over £50 last month"
    
    print(f"\nTesting concurrent execution with query: \"{query}\"")
    print("-" * 60)
    
    # Time the workflow
    import time
    start = time.perf_counter()
    
    result = await workflow.process(query)
    
    end = time.perf_counter()
    workflow_time = (end - start) * 1000
    
    # Calculate theoretical sequential time (sum of all agent times)
    sequential_time = sum(m.response_time_ms for m in result.metrics.values())
    
    print(f"✅ Workflow completed successfully")
    print(f"\n⏱️  Timing Analysis:")
    print(f"   • Actual workflow time: {workflow_time:.0f}ms")
    print(f"   • Sum of agent times: {sequential_time:.0f}ms")
    print(f"   • Time saved by concurrency: {sequential_time - workflow_time:.0f}ms")
    print(f"   • Speedup factor: {sequential_time/workflow_time:.1f}x")
    
    print(f"\n📊 Agent Execution Times:")
    for agent_name, metrics in result.metrics.items():
        print(f"   • {agent_name:30} {metrics.response_time_ms:6.0f}ms")
    
    if workflow_time < sequential_time * 0.8:  # Allow some overhead
        print("\n✅ CONFIRMED: Agents are running concurrently!")
    else:
        print("\n⚠️  WARNING: Agents may not be running concurrently")
    
    print("=" * 80)


async def test_workflow_summary():
    """Test the workflow summary formatting"""
    
    print("\n" + "=" * 80)
    print("WORKFLOW SUMMARY TEST")
    print("=" * 80)
    
    # Load environment
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found")
        return
    
    llm_client = AnthropicLLMClient(api_key=api_key)
    workflow = QueryPreprocessingWorkflow(llm_client=llm_client)
    
    query = "How much did I spend on groceries and transport last month?"
    
    print(f"\nProcessing query: \"{query}\"")
    print("-" * 60)
    
    try:
        result = await workflow.process(query)
        
        # Display the formatted summary
        summary = workflow.get_workflow_summary(result)
        print("\n" + summary)
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print("\n" + "=" * 80)


async def main():
    """Run all workflow tests"""
    
    print("\n🔬 Query Preprocessing Workflow Test Suite\n")
    
    # Run main test suite
    await test_workflow()
    
    # Run concurrent execution test
    await test_concurrent_execution()
    
    # Run summary formatting test
    await test_workflow_summary()
    
    print("\n✅ All workflow tests completed!\n")


if __name__ == "__main__":
    asyncio.run(main())