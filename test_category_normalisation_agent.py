#!/usr/bin/env python3
"""
Test script for CategoryNormalisationAgent
"""

import asyncio
import json
import os
from dotenv import load_dotenv

from src.clients.llm_clients.anthropic_llm_client import AnthropicLLMClient
from src.workflow_nodes.query_preprocessing.category_normalisation_agent import CategoryNormalisationAgent
from src.models.category_normalisation_models import (
    CategoryNormalisationInput,
    CategoryEntity
)


async def test_category_normalisation():
    """Test the CategoryNormalisationAgent with various category mappings"""
    
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
    agent = CategoryNormalisationAgent(llm_client=llm_client)
    
    # Test cases - 10 category normalisation scenarios
    # All different from prompt examples to test generalization
    test_cases = [
        # Tier 1 - Top level categories
        {
            "query": "Track all my income sources",
            "entities": [{"type": "category", "value": "income"}],
            "expected": ["income"],
            "description": "Tier 1: Top-level income"
        },
        
        # Tier 2 - Generic subcategories
        {
            "query": "Monthly housing costs analysis",
            "entities": [{"type": "category", "value": "housing costs"}],
            "expected": ["expenses:bills"],
            "description": "Tier 2: Housing to bills"
        },
        {
            "query": "Supermarket purchases this month",
            "entities": [{"type": "category", "value": "supermarket"}],
            "expected": ["expenses:groceries.supermarkets"],
            "description": "Tier 2: Supermarket to groceries"
        },
        {
            "query": "Restaurant spending patterns",
            "entities": [{"type": "category", "value": "restaurants"}],
            "expected": ["expenses:eating-out.restaurants"],
            "description": "Tier 2: Restaurants"
        },
        
        # Tier 3 - Specific categories
        {
            "query": "Analysis of rent payments",
            "entities": [{"type": "category", "value": "rent"}],
            "expected": ["expenses:bills.rent"],
            "description": "Tier 3: Rent payments"
        },
        {
            "query": "Spending at bars and pubs",
            "entities": [{"type": "category", "value": "bars"}],
            "expected": ["expenses:eating-out.bars"],
            "description": "Tier 3: Bars"
        },
        {
            "query": "Gas and heating bills",
            "entities": [{"type": "category", "value": "heating"}],
            "expected": ["expenses:bills.heating-fuels"],
            "description": "Tier 3: Heating fuels"
        },
        
        # Income categories
        {
            "query": "Investment returns this quarter",
            "entities": [{"type": "category", "value": "investments"}],
            "expected": ["income:investments"],
            "description": "Income: Investments"
        },
        
        # Multiple categories
        {
            "query": "Transport vs entertainment budget",
            "entities": [
                {"type": "category", "value": "transport"},
                {"type": "category", "value": "entertainment"}
            ],
            "expected": ["expenses:transport", "expenses:entertainment"],
            "description": "Multiple categories"
        },
        
        # Semantic mapping
        {
            "query": "Fitness club subscriptions",
            "entities": [{"type": "category", "value": "fitness"}],
            "expected": ["expenses:wellness.healthcare"],
            "description": "Semantic: Fitness to healthcare"
        }
    ]
    
    print("=" * 80)
    print("Testing CategoryNormalisationAgent")
    print("=" * 80)
    print(f"\nRunning {len(test_cases)} category normalisation tests...")
    print("=" * 80)
    
    success_count = 0
    results_summary = []
    
    for i, test_case in enumerate(test_cases, 1):
        query = test_case["query"]
        entities = test_case["entities"]
        expected = test_case["expected"]
        description = test_case["description"]
        
        print(f"\n[{i}/{len(test_cases)}] 📝 Query: {query}")
        print(f"   📋 Type: {description}")
        print(f"   📥 Input categories: {[e['value'] for e in entities]}")
        print(f"   🎯 Expected mappings: {expected}")
        print("-" * 40)
        
        try:
            # Create input model
            input_data = CategoryNormalisationInput(
                query=query,
                entities=[CategoryEntity(**e) for e in entities]
            )
            
            # Process the normalisation
            result = await agent.process(input_data)
            
            # Display results
            if result.entities:
                print(f"   ✅ Normalised {len(result.entities)} categories:")
                actual_mappings = []
                for entity in result.entities:
                    print(f"      '{entity.value}' → '{entity.canon}'")
                    actual_mappings.append(entity.canon)
                
                # Check if mappings match expected
                is_correct = actual_mappings == expected
                if is_correct:
                    print(f"   ✓ Correct normalisation!")
                    success_count += 1
                else:
                    print(f"   ✗ Incorrect normalisation!")
                    print(f"      Expected: {expected}")
                    print(f"      Got: {actual_mappings}")
            else:
                print("   ❌ No normalised entities returned")
                is_correct = False
            
            # Store result for summary
            results_summary.append({
                "query": query[:40] + "..." if len(query) > 40 else query,
                "description": description,
                "input": [e['value'] for e in entities],
                "expected": expected,
                "actual": [e.canon for e in result.entities] if result.entities else [],
                "correct": is_correct
            })
            
            # Serialize to JSON
            print(f"\n📄 JSON Output:")
            print(json.dumps(
                result.model_dump(exclude={'raw_response'}), 
                indent=2,
                ensure_ascii=False
            ))
                
        except Exception as e:
            print(f"❌ Error: {e}")
            results_summary.append({
                "query": query[:40] + "..." if len(query) > 40 else query,
                "description": description,
                "input": [e['value'] for e in entities],
                "expected": expected,
                "actual": [],
                "correct": False
            })
    
    # Summary
    print("\n" + "=" * 80)
    print("Test Summary")
    print("=" * 80)
    print(f"✅ Correct Normalisations: {success_count}/{len(test_cases)}")
    print(f"❌ Incorrect Normalisations: {len(test_cases) - success_count}/{len(test_cases)}")
    print(f"📊 Accuracy: {(success_count/len(test_cases))*100:.1f}%")
    
    # Category hierarchy coverage
    tier1_tests = sum(1 for r in results_summary if "Tier 1" in r["description"])
    tier2_tests = sum(1 for r in results_summary if "Tier 2" in r["description"])
    tier3_tests = sum(1 for r in results_summary if "Tier 3" in r["description"])
    
    print("\n" + "-" * 40)
    print("Category Hierarchy Coverage:")
    print(f"📁 Tier 1 (Top-level): {tier1_tests} tests")
    print(f"📁 Tier 2 (Subcategory): {tier2_tests} tests")
    print(f"📁 Tier 3 (Specific): {tier3_tests} tests")
    
    # Detailed results table
    print("\n" + "=" * 80)
    print("Detailed Results")
    print("=" * 80)
    for i, result in enumerate(results_summary, 1):
        status = "✓" if result["correct"] else "✗"
        print(f"\n{i:2}. [{status}] {result['description']}")
        print(f"     Query: {result['query']}")
        print(f"     Input: {result['input']}")
        print(f"     Expected: {result['expected']}")
        if not result["correct"]:
            print(f"     Got: {result['actual']}")
    
    print("=" * 80)


if __name__ == "__main__":
    print("\n🔬 CategoryNormalisationAgent Test Suite\n")
    print("📊 Testing category to canonical code mapping\n")
    asyncio.run(test_category_normalisation())