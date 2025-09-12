#!/usr/bin/env python3
"""
Test script for UnprocessableEntityExtractionAgent
"""

import asyncio
import json
import os
from dotenv import load_dotenv

from src.clients.llm_clients.anthropic_llm_client import AnthropicLLMClient
from src.workflow_nodes.query_preprocessing.unprocessable_entity_extraction_agent import UnprocessableEntityExtractionAgent


async def test_unprocessable_entity_extraction():
    """Test the UnprocessableEntityExtractionAgent with various queries"""
    
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
    agent = UnprocessableEntityExtractionAgent(llm_client=llm_client)
    
    # Test queries - 10 cases covering key unprocessable entity types
    test_queries = [
        # Fully processable (no unprocessable entities)
        "Show me transactions at Tesco last month",
        
        # Geographic entity (critical)
        "Transactions in London last week",
        
        # Payment method entity (critical)
        "Credit card transactions yesterday",
        
        # Person recipient entity (critical)
        "Money sent to John Smith",
        
        # Transaction channel entity (critical)
        "Online purchases at Amazon",
        
        # Product/service entity (may be critical)
        "How much on coffee at Starbucks?",
        
        # Financial product entity (critical)
        "My mortgage payments",
        
        # Transaction status entity (critical)
        "Show pending transactions",
        
        # Account entity (critical)
        "Transfers from my savings account",
        
        # Complex with multiple unprocessable entities
        "Credit card transactions in London for petrol",
    ]
    
    print("=" * 80)
    print("Testing UnprocessableEntityExtractionAgent")
    print("=" * 80)
    print(f"\nRunning {len(test_queries)} test queries...")
    print("=" * 80)
    
    success_count = 0
    failure_count = 0
    queries_with_critical = 0
    queries_fully_processable = 0
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n[{i}/{len(test_queries)}] 📝 Query: {query}")
        print("-" * 40)
        
        try:
            # Process the query (returns Pydantic model)
            result = await agent.process(query)
            
            # Display extracted entities from Pydantic model
            if result.entities:
                has_critical = any(e.critical for e in result.entities)
                if has_critical:
                    queries_with_critical += 1
                    print(f"⚠️  Found {len(result.entities)} unprocessable entities (CRITICAL):")
                else:
                    print(f"🟡 Found {len(result.entities)} unprocessable entities (non-critical):")
                
                for entity in result.entities:
                    critical_marker = "🔴" if entity.critical else "🟡"
                    print(f"   {critical_marker} Type: {entity.type:20} | Value: '{entity.value}'")
                    
                # Serialize to JSON (compact format)
                entities_dict = [
                    {"type": e.type, "value": e.value, "critical": e.critical} 
                    for e in result.entities
                ]
                print(f"\n📄 JSON: {json.dumps(entities_dict, ensure_ascii=False)}")
            else:
                queries_fully_processable += 1
                print("✅ No unprocessable entities (query is fully processable)")
            
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
    print("-" * 40)
    print(f"🟢 Fully processable queries: {queries_fully_processable}")
    print(f"🔴 Queries with critical entities: {queries_with_critical}")
    print(f"🟡 Queries with only non-critical entities: {success_count - queries_fully_processable - queries_with_critical}")
    print("=" * 80)


if __name__ == "__main__":
    print("\n🔬 UnprocessableEntityExtractionAgent Test Suite\n")
    asyncio.run(test_unprocessable_entity_extraction())