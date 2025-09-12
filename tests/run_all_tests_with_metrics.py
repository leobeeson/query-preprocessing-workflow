#!/usr/bin/env python3
"""
Run all agent tests with consolidated metrics reporting
"""

import asyncio
import os
from dotenv import load_dotenv

from src.clients.llm_clients.anthropic_llm_client import AnthropicLLMClient
from src.workflow_nodes.query_preprocessing.processable_entity_extraction_agent import ProcessableEntityExtractionAgent
from src.workflow_nodes.query_preprocessing.unprocessable_entity_extraction_agent import UnprocessableEntityExtractionAgent
from src.workflow_nodes.query_preprocessing.user_intent_validation_agent import UserIntentValidationAgent
from src.workflow_nodes.query_preprocessing.query_security_validation_agent import QuerySecurityValidationAgent
from src.workflow_nodes.query_preprocessing.category_normalisation_agent import CategoryNormalisationAgent
from src.models.category_normalisation_models import CategoryNormalisationInput, CategoryEntity
from src.core_nodes.metrics_aggregator import MetricsAggregator


async def run_quick_test_suite():
    """Run a quick test of each agent with metrics tracking"""
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables")
        return
    
    # Initialize
    llm_client = AnthropicLLMClient(api_key=api_key)
    metrics_aggregator = MetricsAggregator()
    
    print("=" * 80)
    print("AGENT PERFORMANCE & COST ANALYSIS")
    print("=" * 80)
    print("\nTesting all agents with sample queries...\n")
    
    # Test 1: ProcessableEntityExtractionAgent
    print("1️⃣  ProcessableEntityExtractionAgent")
    print("-" * 40)
    agent1 = ProcessableEntityExtractionAgent(llm_client=llm_client)
    query = "Show me Tesco groceries over £50 last month"
    print(f"Query: {query}")
    
    result = await agent1.process(query)
    metrics = agent1.get_last_metrics()
    if metrics:
        print(f"✅ Extracted {len(result.entities)} entities")
        print(f"⏱️  Time: {metrics.format_time()}")
        print(f"💰 Cost: {metrics.format_cost()}")
        print(f"📊 Tokens: {metrics.input_tokens} in / {metrics.output_tokens} out")
        metrics_aggregator.add_metrics("ProcessableEntityExtraction", metrics)
    print()
    
    # Test 2: UnprocessableEntityExtractionAgent
    print("2️⃣  UnprocessableEntityExtractionAgent")
    print("-" * 40)
    agent2 = UnprocessableEntityExtractionAgent(llm_client=llm_client)
    query = "Credit card transactions in London"
    print(f"Query: {query}")
    
    result = await agent2.process(query)
    metrics = agent2.get_last_metrics()
    if metrics:
        print(f"⚠️  Found {len(result.entities)} unprocessable entities")
        print(f"⏱️  Time: {metrics.format_time()}")
        print(f"💰 Cost: {metrics.format_cost()}")
        print(f"📊 Tokens: {metrics.input_tokens} in / {metrics.output_tokens} out")
        metrics_aggregator.add_metrics("UnprocessableEntityExtraction", metrics)
    print()
    
    # Test 3: UserIntentValidationAgent
    print("3️⃣  UserIntentValidationAgent")
    print("-" * 40)
    agent3 = UserIntentValidationAgent(llm_client=llm_client)
    query = "How much did I spend on groceries?"
    print(f"Query: {query}")
    
    result = await agent3.process(query)
    metrics = agent3.get_last_metrics()
    if metrics:
        print(f"{'✅ Valid' if result.valid else '❌ Invalid'}: {result.justification}")
        print(f"⏱️  Time: {metrics.format_time()}")
        print(f"💰 Cost: {metrics.format_cost()}")
        print(f"📊 Tokens: {metrics.input_tokens} in / {metrics.output_tokens} out")
        metrics_aggregator.add_metrics("UserIntentValidation", metrics)
    print()
    
    # Test 4: QuerySecurityValidationAgent
    print("4️⃣  QuerySecurityValidationAgent")
    print("-" * 40)
    agent4 = QuerySecurityValidationAgent(llm_client=llm_client)
    query = "Show me my spending at Tesco"
    print(f"Query: {query}")
    
    result = await agent4.process(query)
    metrics = agent4.get_last_metrics()
    if metrics:
        print(f"{'✅ Safe' if result.valid else '⚠️  Unsafe'}: {result.justification}")
        print(f"⏱️  Time: {metrics.format_time()}")
        print(f"💰 Cost: {metrics.format_cost()}")
        print(f"📊 Tokens: {metrics.input_tokens} in / {metrics.output_tokens} out")
        metrics_aggregator.add_metrics("QuerySecurityValidation", metrics)
    print()
    
    # Test 5: CategoryNormalisationAgent
    print("5️⃣  CategoryNormalisationAgent")
    print("-" * 40)
    agent5 = CategoryNormalisationAgent(llm_client=llm_client)
    input_data = CategoryNormalisationInput(
        query="How much on groceries and transport?",
        entities=[
            CategoryEntity(type="category", value="groceries"),
            CategoryEntity(type="category", value="transport")
        ]
    )
    print(f"Query: {input_data.query}")
    print(f"Categories: {[e.value for e in input_data.entities]}")
    
    result = await agent5.process(input_data)
    metrics = agent5.get_last_metrics()
    if metrics:
        print(f"📁 Normalised to: {[e.canon for e in result.entities]}")
        print(f"⏱️  Time: {metrics.format_time()}")
        print(f"💰 Cost: {metrics.format_cost()}")
        print(f"📊 Tokens: {metrics.input_tokens} in / {metrics.output_tokens} out")
        metrics_aggregator.add_metrics("CategoryNormalisation", metrics)
    print()
    
    # Display comprehensive metrics
    print(metrics_aggregator.format_summary())
    
    # Cost breakdown
    summary = metrics_aggregator.get_summary()
    print("\n" + "=" * 60)
    print("COST & PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    # Overall averages
    avg_cost_per_call = summary['total_cost']/summary['total_calls'] if summary['total_calls'] > 0 else 0
    avg_response_time = summary['avg_response_time_ms']
    
    print(f"📊 Total API Calls: {summary['total_calls']}")
    print(f"💵 Average Cost per Call: ${avg_cost_per_call:.6f}")
    print(f"⚡ Average Response Time: {avg_response_time:.0f}ms ({avg_response_time/1000:.2f}s)")
    print(f"💰 Total Cost (all calls): ${summary['total_cost']:.6f}")
    
    print("\n" + "-" * 60)
    print("PER-AGENT AVERAGES:")
    print("-" * 60)
    
    # Calculate per-agent averages
    agent_stats = []
    for agent in summary["agents"]:
        avg_cost = agent["total_cost"] / agent["total_calls"] if agent["total_calls"] > 0 else 0
        avg_time = agent["avg_response_time_ms"]
        agent_stats.append({
            "name": agent["agent_name"],
            "avg_cost": avg_cost,
            "avg_time": avg_time,
            "calls": agent["total_calls"]
        })
    
    # Sort by average cost (most expensive first)
    agent_stats.sort(key=lambda x: x["avg_cost"], reverse=True)
    
    print("\nBy Average Cost (per call):")
    for i, stats in enumerate(agent_stats, 1):
        print(f"  {i}. {stats['name']:30} ${stats['avg_cost']:.6f} ({stats['avg_time']:.0f}ms)")
    
    # Sort by average response time (slowest first)
    agent_stats.sort(key=lambda x: x["avg_time"], reverse=True)
    
    print("\nBy Average Response Time:")
    for i, stats in enumerate(agent_stats, 1):
        time_str = f"{stats['avg_time']:.0f}ms" if stats['avg_time'] < 1000 else f"{stats['avg_time']/1000:.2f}s"
        print(f"  {i}. {stats['name']:30} {time_str:>8} (${stats['avg_cost']:.6f})")
    
    print("=" * 60)


if __name__ == "__main__":
    print("\n🔬 Agent Performance & Cost Testing Suite\n")
    asyncio.run(run_quick_test_suite())