#!/usr/bin/env python3
"""
Test script for ProcessableEntityExtractionAgent
"""

import asyncio
import json
import os
from dotenv import load_dotenv

from src.clients.llm_clients.anthropic_llm_client import AnthropicLLMClient
from src.workflow_nodes.query_preprocessing.processable_entity_extraction_agent import ProcessableEntityExtractionAgent
from src.core_nodes.metrics_aggregator import MetricsAggregator


async def test_processable_entity_extraction():
    """Test the ProcessableEntityExtractionAgent with various queries"""
    
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not found in environment variables")
        print("Please create a .env file with your API key")
        return
    
    # Initialize the LLM client
    llm_client = AnthropicLLMClient(api_key=api_key)
    
    # Initialize the agent
    agent = ProcessableEntityExtractionAgent(llm_client=llm_client)
    
    # Test queries - 10 cases covering all processable entity types
    test_queries = [
        # Temporal entity
        "Show me transactions last month",
        
        # Category entity
        "How much on groceries this year?",
        
        # Merchant entity
        "Netflix and Spotify subscriptions",
        
        # Amount entity
        "All purchases over £50",
        
        # Environmental entity
        "What's my carbon footprint from transport?",
        
        # Mixed entities (multiple types)
        "Tesco groceries over £50 last month",
        
        # Entity class reference
        "Group by category and sort by amount",
        
        # Complex temporal
        "Weekend spending vs weekday patterns",
        
        # Amount range
        "Transactions between £20 and £100",
        
        # Edge case - no entities
        "How much did I spend?",
    ]
    
    print("=" * 80)
    print("Testing ProcessableEntityExtractionAgent")
    print("=" * 80)
    print(f"\nRunning {len(test_queries)} test queries...")
    print("=" * 80)
    
    success_count = 0
    failure_count = 0
    metrics_aggregator = MetricsAggregator()
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[{i}/{len(test_queries)}] 📝 Query: {query}")
        print("-" * 40)
        
        try:
            # Process the query (returns Pydantic model)
            result = await agent.process(query)
            
            # Display extracted entities from Pydantic model
            if result.entities:
                print(f"✅ Extracted {len(result.entities)} entities:")
                for entity in result.entities:
                    print(f"   • Type: {entity.type:15} | Value: '{entity.value}'")
            else:
                print("⚪ No entities extracted")
            
            # Serialize to JSON (compact format for testing)
            entities_dict = [{"type": e.type, "value": e.value} for e in result.entities]
            print(f"\n📄 JSON: {json.dumps(entities_dict, ensure_ascii=False)}")
            
            # Get and display metrics
            metrics = agent.get_last_metrics()
            if metrics:
                print(f"\n⏱️  Response Time: {metrics.format_time()}")
                print(f"💰 Cost: {metrics.format_cost()} ({metrics.input_tokens} in / {metrics.output_tokens} out tokens)")
                metrics_aggregator.add_metrics("ProcessableEntityExtraction", metrics)
            
            success_count += 1
                
        except Exception as e:
            print(f"❌ Error: {e}")
            failure_count += 1
    
    # Summary
    print("\n" + "=" * 80)
    print("Test Summary")
    print("=" * 80)
    print(f"✅ Successful: {success_count}/{len(test_queries)}")
    if failure_count > 0:
        print(f"❌ Failed: {failure_count}/{len(test_queries)}")
    print(f"📊 Success Rate: {(success_count/len(test_queries))*100:.1f}%")
    print("=" * 80)
    
    # Display metrics summary
    print("\n" + metrics_aggregator.format_summary())
    
    # Show averages
    summary = metrics_aggregator.get_summary()
    if summary['total_calls'] > 0:
        print("\n" + "=" * 60)
        print("AVERAGE METRICS")
        print("=" * 60)
        print(f"💵 Average Cost per Query: ${summary['total_cost']/summary['total_calls']:.6f}")
        print(f"⚡ Average Response Time: {summary['avg_response_time_ms']:.0f}ms ({summary['avg_response_time_ms']/1000:.2f}s)")
        print(f"📊 Average Tokens per Query: {summary['total_tokens']/summary['total_calls']:.0f}")
        print("=" * 60)


if __name__ == "__main__":
    print("\n🔬 ProcessableEntityExtractionAgent Test Suite\n")
    asyncio.run(test_processable_entity_extraction())