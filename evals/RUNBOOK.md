# Evaluation Framework Runbook

This runbook provides instructions for running and managing the evaluation framework.

## Quick Start

### Running All Tests for an Agent

#### CategoryNormalisationAgent

```bash
# Run all CategoryNormalisationAgent tests
python evals/tests/test_eval_decorated_category_normalisation.py

# Run tests with specific tags
python evals/tests/test_eval_decorated_category_normalisation.py --tags valid

# Run specific cases by name
python evals/tests/test_eval_decorated_category_normalisation.py --cases case_name_1 case_name_2
```

#### ProcessableEntityExtractionAgent

```bash
# Run all ProcessableEntityExtractionAgent tests
python evals/tests/test_eval_decorated_processable_entity_extraction.py

# Run tests with specific tags
python evals/tests/test_eval_decorated_processable_entity_extraction.py --tags category

# Run tests with multiple tags (AND logic - must have ALL tags)
python evals/tests/test_eval_decorated_processable_entity_extraction.py --tags category temporal

# Run specific cases by name
python evals/tests/test_eval_decorated_processable_entity_extraction.py --cases test_budget_query test_transfer_query
```

#### QueryCharacteristicsExtractionAgent

```bash
# Run all QueryCharacteristicsExtractionAgent tests
python evals/tests/test_eval_decorated_query_characteristics_extraction.py

# Run tests with specific tags
python evals/tests/test_eval_decorated_query_characteristics_extraction.py --tags simple

# Run specific cases by name
python evals/tests/test_eval_decorated_query_characteristics_extraction.py --cases case_name_1 case_name_2
```

#### QuerySecurityValidationAgent

```bash
# Run all QuerySecurityValidationAgent tests
python evals/tests/test_eval_decorated_query_security_validation.py

# Run tests with specific tags
python evals/tests/test_eval_decorated_query_security_validation.py --tags invalid

# Run tests with multiple tags (AND logic - must have ALL tags)
python evals/tests/test_eval_decorated_query_security_validation.py --tags invalid sql_injection

# Run specific cases by name
python evals/tests/test_eval_decorated_query_security_validation.py --cases clean_spending_query sql_injection_drop
```

#### UnprocessableEntityExtractionAgent

```bash
# Run all UnprocessableEntityExtractionAgent tests
python evals/tests/test_eval_decorated_unprocessable_entity_extraction.py

# Run tests with specific tags
python evals/tests/test_eval_decorated_unprocessable_entity_extraction.py --tags clarification

# Run specific cases by name
python evals/tests/test_eval_decorated_unprocessable_entity_extraction.py --cases case_name_1 case_name_2
```

#### UserIntentValidationAgent

```bash
# Run all UserIntentValidationAgent tests
python evals/tests/test_eval_decorated_user_intent_validation.py

# Run tests with specific tags
python evals/tests/test_eval_decorated_user_intent_validation.py --tags valid

# Run specific cases by name
python evals/tests/test_eval_decorated_user_intent_validation.py --cases case_name_1 case_name_2
```

### Running with pytest (alternative approach)

**Note:** The evaluation test files are standalone Python scripts with custom argument parsers (`--tags` and `--cases`). However, you can also run them via pytest using the `-k` flag for pattern matching on test/case names (not tags).

```bash
# Run all evaluation tests
pytest evals/tests/ -v

# Run specific test file
pytest evals/tests/test_eval_decorated_processable_entity_extraction.py -v

# Run tests matching pattern by name (uses pytest -k flag, NOT the same as --tags)
pytest evals/tests/ -k "budget" -v

# Run with coverage report
pytest evals/tests/ --cov=src --cov-report=html

# Run in parallel (if pytest-xdist installed)
pytest evals/tests/ -n auto
```

**Important distinction:**
- **Standalone mode** (recommended): `python evals/tests/test_file.py --tags tag_name` - Uses custom argparse with `--tags` for tag filtering and `--cases` for case name filtering
- **Pytest mode**: `pytest evals/tests/ -k "pattern"` - Uses pytest's `-k` flag for pattern matching on test names only (cannot filter by tags)

## Test Organization

### Current Test Files

1. **`test_eval_decorated_category_normalisation.py`**
   ```bash
   python evals/tests/test_eval_decorated_category_normalisation.py
   ```

2. **`test_eval_decorated_processable_entity_extraction.py`**
   ```bash
   python evals/tests/test_eval_decorated_processable_entity_extraction.py
   ```

3. **`test_eval_decorated_query_characteristics_extraction.py`**
   ```bash
   python evals/tests/test_eval_decorated_query_characteristics_extraction.py
   ```

4. **`test_eval_decorated_query_security_validation.py`**
   ```bash
   python evals/tests/test_eval_decorated_query_security_validation.py
   ```

5. **`test_eval_decorated_unprocessable_entity_extraction.py`**
   ```bash
   python evals/tests/test_eval_decorated_unprocessable_entity_extraction.py
   ```

6. **`test_eval_decorated_user_intent_validation.py`**
   ```bash
   python evals/tests/test_eval_decorated_user_intent_validation.py
   ```

## Adding New Test Cases

### 1. Create a new test case in `evals/cases/`

```python
from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact

@eval_case(
    name="unique_test_name",
    agent_class=YourAgentClass,
    description="What this test validates",
    tags=["category", "feature"]
)
def eval_your_test():
    return {
        "input": YourInputModel(query="test query"),
        "expected": YourOutputModel(
            field="expected value"
        ),
        "field_validations": {
            "field": Exact(value="expected value")
        }
    }
```

### 2. Run the test

```bash
# The decorator automatically creates a test function
python evals/tests/test_eval_decorated_your_agent.py -k your_test
```

## Field Validators

Available validators for fine-grained validation:

- **`Exact`**: Field must exactly match value
- **`OneOf`**: Field must be one of provided values
- **`AllOf`**: List field must contain all values
- **`Contains`**: List field must contain at least these values
- **`Substring`**: String field must contain substring
- **`ListMatches`**: List items must match specification
- **`Criteria`**: LLM-as-Judge evaluation against criteria

Example:
```python
"field_validations": {
    "entities": ListMatches(items=[
        {"type": Exact(value="category"), "value": Substring(value="repair")}
    ])
}
```

## Debugging Failed Tests

### 1. Enable verbose output

```python
# In test file, set verbose=True
evaluator = Evaluator(agent=agent, verbose=True)
```

### 2. Check raw LLM responses

```python
# Add raw_response field to output model
class YourOutput(BaseModel):
    raw_response: Optional[str] = None
```

### 3. Run single test in isolation

```bash
python -m pytest evals/tests/test_file.py::test_specific_case -vvs
```

### 4. Check agent prompts

```bash
# Review prompts being used
cat src/prompts/your_agent_prompt.py
```

## Environment Setup

### Required Environment Variables

```bash
# Create .env file
ANTHROPIC_API_KEY=your_key_here
```

### Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# For parallel testing (optional)
pip install pytest-xdist  # Enables parallel test execution
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Run Evaluations
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - run: pip install -r requirements.txt
      - run: pytest evals/tests/ -v
```

## Performance Monitoring

### Track success rates

```bash
# Generate test report
pytest evals/tests/ --json-report --json-report-file=results.json

# View summary
python -c "import json; r=json.load(open('results.json')); print(f'Pass rate: {r[\"summary\"][\"passed\"]}/{r[\"summary\"][\"total\"]}')"
```

### Monitor LLM costs

Tests track token usage and costs. Check logs for:
- Tokens used per test
- Cost per agent invocation
- Total evaluation cost

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure you're in the project root
   ```bash
   cd /path/to/mii-scratchpad
   python evals/tests/test_file.py
   ```

2. **API rate limits**: Add delays between tests
   ```python
   import time
   time.sleep(1)  # Add between test cases
   ```

3. **Timeout errors**: Increase timeout in evaluator
   ```python
   evaluator = Evaluator(agent=agent, timeout=30)
   ```

4. **Field validation failures**: Check exact string matching
   ```python
   # Use Substring for partial matches instead of Exact
   "field": Substring(value="partial")
   ```

## Best Practices

1. **Tag tests appropriately** for easy filtering
2. **Use descriptive test names** that explain what's being tested
3. **Include both positive and negative cases**
4. **Test edge cases** (empty inputs, special characters, etc.)
5. **Document expected behavior** in test descriptions
6. **Keep test data realistic** to actual user queries
7. **Avoid overfitting** - don't use exact eval queries in prompts

## Reporting Results

Generate evaluation reports:

```bash
# HTML report
pytest evals/tests/ --html=report.html --self-contained-html

# JSON report for processing
pytest evals/tests/ --json-report --json-report-file=results.json

# Coverage report
pytest evals/tests/ --cov=src --cov-report=html
open htmlcov/index.html  # Opens coverage report in browser
```

## Future Enhancements

- [ ] Add benchmark suite for performance testing
- [ ] Implement regression detection
- [ ] Add cross-agent comparison tests
- [ ] Create evaluation dashboard
- [ ] Add automated prompt optimization based on results