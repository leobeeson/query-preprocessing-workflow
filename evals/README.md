# Simplified LLM Evaluation Framework

A lightweight, easy-to-use framework for evaluating LLM agent nodes without the complexity of the existing framework.

## Features

- **Simple and Clean**: ~400 lines vs 1000+ lines of the original framework
- **Multiple Validation Methods**: String, multi-choice, boolean, and criteria-based validation
- **LLM-as-a-Judge**: Semantic evaluation using LLM for complex criteria
- **No AWS Dependencies**: Works with any LLM client implementing the simple interface
- **Clear Reporting**: Easy-to-understand pass/fail results with detailed failure reasons

## Installation

No installation required. Just import from the `scratchpad/evals` directory:

```python
from scratchpad.evals import EvalCase, EvalRunner
```

## Quick Start

### 1. Define Your Agent Node

Your agent node should follow this pattern:

```python
class MyAgentNode:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.node_name = "MyAgentNode"
    
    async def process(self, context):
        # Your agent logic here
        query = context.query
        
        # Call LLM
        response = await self.llm_client.generate(
            system_prompt="You are a classifier",
            user_prompt=f"Classify: {query}"
        )
        
        # Store output in context
        context.update_workflow_node(
            self.node_name,
            classification=response
        )
        
        return context
```

### 2. Create Test Cases

```python
from scratchpad.evals import EvalCase

test_cases = [
    # String validation
    EvalCase(
        name="simple_classification",
        input_data={"query": "What is VAT?"},
        expected_output="CONCEPTUAL"
    ),
    
    # Multi-choice validation (for ambiguous cases)
    EvalCase(
        name="ambiguous_query",
        input_data={"query": "How do I use this?"},
        expected_output=["PROCEDURAL", "CAPABILITY"]
    ),
    
    # Boolean validation
    EvalCase(
        name="validity_check",
        input_data={"query": "Is this valid?"},
        expected_output=True
    ),
    
    # Criteria-based validation (LLM-as-a-Judge)
    EvalCase(
        name="quality_check",
        input_data={"query": "Explain quantum computing"},
        criteria=[
            "The explanation is technically accurate",
            "The explanation is accessible to non-experts",
            "Key concepts are clearly defined"
        ]
    )
]
```

### 3. Run Evaluations

```python
import asyncio
from scratchpad.evals import EvalRunner

async def run_evaluation():
    # Initialize runner
    runner = EvalRunner(
        agent_class=MyAgentNode,
        llm_client=my_llm_client,
        default_field_name="classification"  # Field to extract from output
    )
    
    # Run all test cases
    results = await runner.run_batch(test_cases)
    
    # Print summary
    runner.print_summary(results)
    
    return results

# Run
results = asyncio.run(run_evaluation())
```

## Validation Methods

### String Validation

For exact string matching:

```python
EvalCase(
    name="exact_match",
    input_data={"query": "input"},
    expected_output="expected_string"
)
```

### Multi-Choice Validation

For cases where multiple outputs are valid:

```python
EvalCase(
    name="multiple_valid",
    input_data={"query": "input"},
    expected_output=["option1", "option2", "option3"]
)
```

### Boolean Validation

For true/false outputs:

```python
EvalCase(
    name="boolean_check",
    input_data={"query": "input"},
    expected_output=True
)
```

### Criteria-Based Validation (LLM-as-a-Judge)

For semantic evaluation against criteria:

```python
EvalCase(
    name="semantic_check",
    input_data={"query": "input"},
    criteria=[
        "Output contains specific information",
        "Tone is professional",
        "No hallucinated content"
    ]
)
```

## Output Format

The framework provides clear, actionable output:

```
============================================================
EVALUATION SUMMARY
============================================================
Total tests: 10
Passed: 8
Failed: 2
Pass rate: 80.0%

Failures by validation method:
  string: 1
  criteria: 1

============================================================
FAILED CASES (2)
============================================================

❌ classification_error
   Reason: Expected 'PROCEDURAL', got 'CONCEPTUAL'
   Expected: PROCEDURAL
   Actual: {'classification': 'CONCEPTUAL'}

❌ quality_check
   Reason: The explanation lacks technical depth and key concepts are not defined
   Expected: None
   Actual: {'response': 'Quantum computing uses quantum bits...'}

============================================================
```

## Advanced Usage

### Custom Field Extraction

Specify which field to extract from the output:

```python
runner = EvalRunner(
    agent_class=MyAgentNode,
    llm_client=llm_client,
    default_field_name="my_output_field"
)
```

### Sequential vs Parallel Execution

```python
# Sequential (useful for debugging)
results = await runner.run_batch(test_cases, parallel=False)

# Parallel with custom batch size
results = await runner.run_batch(test_cases, parallel=True, batch_size=5)
```

### Custom LLM Models

If your agent supports model override:

```python
runner = EvalRunner(
    agent_class=MyAgentNode,
    llm_client=llm_client,
    model_name="claude-3-5-sonnet-20241022"
)
```

## Comparison with Original Framework

| Feature | Original Framework | Simplified Framework |
|---------|-------------------|---------------------|
| Lines of Code | 1000+ | ~400 |
| AWS Dependencies | Required | None |
| Setup Complexity | High | Low |
| Multi-model Testing | Built-in | Simple parameter |
| Cost Tracking | Extensive | None (not needed) |
| Response Time Tracking | Detailed metrics | None (not needed) |
| Pytest Integration | Deep integration | Framework-agnostic |
| JSONL Logging | Built-in | None (add if needed) |
| Core Functionality | ✅ | ✅ |
| LLM-as-a-Judge | ✅ | ✅ |
| Clear Error Messages | ✅ | ✅ |

## Design Philosophy

This framework follows these principles:

1. **Simplicity First**: Only include what's necessary for evaluation
2. **Clear Abstractions**: Each component has a single, clear purpose
3. **Easy to Extend**: Add new validators or features without modifying core
4. **Framework Agnostic**: Works with any test runner (pytest, unittest, standalone)
5. **Minimal Dependencies**: Only requires the LLM client interface

## Migration from Original Framework

To migrate from the original framework:

1. Replace `MockConversationContext` with `ConversationContext`
2. Replace complex `EvalCase` with simplified version
3. Replace `AgentEvalRunner` with `EvalRunner`
4. Remove AWS-specific initialization
5. Simplify test decorators and fixtures

Example migration:

```python
# Old
from tests.api.workflows.evals.framework import (
    AgentEvalRunner, EvalCase, MockConversationContext
)

class MyEvalRunner(AgentEvalRunner[MyNode]):
    async def run_node(self, input_data):
        # Complex setup...
        
# New
from scratchpad.evals import EvalRunner

runner = EvalRunner(
    agent_class=MyNode,
    llm_client=llm_client
)
```

## Contributing

To add new features:

1. **New Validators**: Inherit from `Validator` class in `validators.py`
2. **New Output Formats**: Add functions to `utils.py`
3. **New Context Features**: Extend `ConversationContext` in `context.py`

## License

This is a simplified implementation for evaluation purposes.