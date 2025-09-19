"""
Evaluation cases for ProcessableEntityExtractionAgent using decorator pattern.
"""

from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact, Substring
from src.workflow_nodes.query_preprocessing.processable_entity_extraction_agent import ProcessableEntityExtractionAgent
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import ProcessableEntityExtractionOutput, ProcessableEntity as Entity


# ========== Basic Functionality Tests (7) ==========

@eval_case(
    name="basic_merchant",
    agent_class=ProcessableEntityExtractionAgent,
    description="Simple merchant extraction",
    tags=["merchant", "basic"]
)
def eval_basic_merchant():
    return {
        "input": QueryInput(query="Tesco transactions"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="merchant", value="Tesco")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="Tesco")}
        ])
    }
    }


@eval_case(
    name="amount_threshold",
    agent_class=ProcessableEntityExtractionAgent,
    description="Amount threshold with temporal",
    tags=["amount", "temporal", "basic"]
)
def eval_amount_threshold():
    return {
        "input": QueryInput(query="Transactions above £100 today"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="above £100"),
                Entity(type="temporal", value="today")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="amount"), "value": Exact(value="above £100")},
            {"type": Exact(value="temporal"), "value": Exact(value="today")}
        ])
    }
    }


@eval_case(
    name="category_temporal",
    agent_class=ProcessableEntityExtractionAgent,
    description="Category with specific month/year",
    tags=["category", "temporal", "basic"]
)
def eval_category_temporal():
    return {
        "input": QueryInput(query="What's my spending on entertainment in March 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="entertainment"),
                Entity(type="temporal", value="March 2024")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Exact(value="entertainment")},
            {"type": Exact(value="temporal"), "value": Exact(value="March 2024")}
        ])
    }
    }


@eval_case(
    name="ignore_aggregation",
    agent_class=ProcessableEntityExtractionAgent,
    description="Should not extract aggregation operations",
    tags=["category", "negative"]
)
def eval_ignore_aggregation():
    from evals.field_validators import ListMatches, Exact, Substring
    return {
        "input": QueryInput(query="Calculate the sum of transport expenses"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="category", value="transport")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="transport")}
            ])
        }
    }


@eval_case(
    name="amount_range",
    agent_class=ProcessableEntityExtractionAgent,
    description="Amount range extraction",
    tags=["amount", "basic"]
)
def eval_amount_range():
    return {
        "input": QueryInput(query="Purchases between £10 and £30"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="amount", value="between £10 and £30")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="amount"), "value": Substring(value="£10 and £30")}
        ])
    }
    }


@eval_case(
    name="simple_merchant",
    agent_class=ProcessableEntityExtractionAgent,
    description="Simple merchant extraction",
    tags=["merchant", "basic"]
)
def eval_simple_merchant():
    return {
        "input": QueryInput(query="ASDA transactions"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="merchant", value="ASDA")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="ASDA")}
        ])
    }
    }


@eval_case(
    name="no_entities",
    agent_class=ProcessableEntityExtractionAgent,
    description="Query with no processable entities",
    tags=["negative", "basic"]
)
def eval_no_entities():
    return {
        "input": QueryInput(query="What should I do next?"),
        "expected": ProcessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


# ========== Temporal Extraction Tests (6) ==========

@eval_case(
    name="relative_temporal",
    agent_class=ProcessableEntityExtractionAgent,
    description="Relative temporal period",
    tags=["temporal", "relative"]
)
def eval_relative_temporal():
    return {
        "input": QueryInput(query="Spending over the last 6 months"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="temporal", value="last 6 months")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
        ])
    }
    }


@eval_case(
    name="multiple_temporal",
    agent_class=ProcessableEntityExtractionAgent,
    description="Multiple temporal entities",
    tags=["temporal", "multiple"]
)
def eval_multiple_temporal():
    return {
        "input": QueryInput(query="Show weekday versus weekend purchases"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="weekday"),
                Entity(type="temporal", value="weekend")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="temporal"), "value": Exact(value="weekday")},
            {"type": Exact(value="temporal"), "value": Exact(value="weekend")}
        ])
    }
    }


@eval_case(
    name="holiday_period",
    agent_class=ProcessableEntityExtractionAgent,
    description="Named holiday period",
    tags=["merchant", "temporal", "holiday"]
)
def eval_holiday_period():
    return {
        "input": QueryInput(query="Spending at John Lewis during Black Friday"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="John Lewis"),
                Entity(type="temporal", value="Black Friday")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="John Lewis")},
            {"type": Exact(value="temporal"), "value": Exact(value="Black Friday")}
        ])
    }
    }


@eval_case(
    name="fiscal_period",
    agent_class=ProcessableEntityExtractionAgent,
    description="Fiscal quarter period",
    tags=["category", "temporal", "fiscal"]
)
def eval_fiscal_period():
    return {
        "input": QueryInput(query="Bills in Q2 2023"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="Bills"),
                Entity(type="temporal", value="Q2 2023")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Exact(value="Bills")},
            {"type": Exact(value="temporal"), "value": Exact(value="Q2 2023")}
        ])
    }
    }


@eval_case(
    name="time_of_day",
    agent_class=ProcessableEntityExtractionAgent,
    description="Time of day with day of week",
    tags=["temporal", "time"]
)
def eval_time_of_day():
    return {
        "input": QueryInput(query="Purchases between 6am and 9am on Mondays"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="between 6am and 9am"),
                Entity(type="temporal", value="Mondays")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="temporal"), "value": Substring(value="6am and 9am")},  # "between" is optional
            {"type": Exact(value="temporal"), "value": Exact(value="Mondays")}
        ])
    }
    }


@eval_case(
    name="weekend_temporal",
    agent_class=ProcessableEntityExtractionAgent,
    description="Weekday/weekend temporal reference",
    tags=["temporal", "category", "weekend"]
)
def eval_weekend_temporal():
    return {
        "input": QueryInput(query="Weekday dining at restaurants"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="Weekday"),
                Entity(type="category", value="dining"),
                Entity(type="category", value="restaurants")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="temporal"), "value": Exact(value="Weekday")},
            {"type": Exact(value="category"), "value": Exact(value="restaurants")}
        ])
    }
    }


# ========== Merchant Extraction Tests (5) ==========

@eval_case(
    name="merchant_typo",
    agent_class=ProcessableEntityExtractionAgent,
    description="Merchant with typo should be preserved",
    tags=["merchant", "typo"]
)
def eval_merchant_typo():
    return {
        "input": QueryInput(query="Transactions at Amazn yesterday"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazn"),
                Entity(type="temporal", value="yesterday")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="Amazn")},
            {"type": Exact(value="temporal"), "value": Exact(value="yesterday")}
        ])
    }
    }


@eval_case(
    name="merchant_possessive",
    agent_class=ProcessableEntityExtractionAgent,
    description="Merchant with possessive apostrophe",
    tags=["merchant", "possessive"]
)
def eval_merchant_possessive():
    return {
        "input": QueryInput(query="Sainsbury's spending last year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Sainsbury's"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="Sainsbury's")},
            {"type": Exact(value="temporal"), "value": Exact(value="last year")}
        ])
    }
    }


@eval_case(
    name="merchant_location",
    agent_class=ProcessableEntityExtractionAgent,
    description="Merchant with location suffix",
    tags=["merchant", "location"]
)
def eval_merchant_location():
    return {
        "input": QueryInput(query="ASDA Leeds yesterday"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="ASDA Leeds"),
                Entity(type="temporal", value="yesterday")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Substring(value="ASDA")},  # "Leeds" location suffix is optional
            {"type": Exact(value="temporal"), "value": Exact(value="yesterday")}
        ])
    }
    }


@eval_case(
    name="multiple_merchants",
    agent_class=ProcessableEntityExtractionAgent,
    description="Multiple merchant entities",
    tags=["merchant", "multiple"]
)
def eval_multiple_merchants():
    return {
        "input": QueryInput(query="Amazon and eBay purchases"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="merchant", value="eBay")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
            {"type": Exact(value="merchant"), "value": Exact(value="eBay")}
        ])
    }
    }


@eval_case(
    name="complex_multiple",
    agent_class=ProcessableEntityExtractionAgent,
    description="Complex query with multiple entity types",
    tags=["merchant", "amount", "temporal", "complex"]
)
def eval_complex_multiple():
    return {
        "input": QueryInput(query="Disney+ and Prime subscriptions under £20 since March"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Disney+"),
                Entity(type="merchant", value="Prime"),
                Entity(type="amount", value="under £20"),
                Entity(type="temporal", value="since March")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="Disney+")},
            {"type": Exact(value="merchant"), "value": Exact(value="Prime")},
            {"type": Exact(value="amount"), "value": Exact(value="under £20")},
            {"type": Exact(value="temporal"), "value": Exact(value="since March")}
        ])
    }
    }


# ========== Category Extraction Tests (4) ==========

@eval_case(
    name="compound_category",
    agent_class=ProcessableEntityExtractionAgent,
    description="Compound category phrase",
    tags=["category", "compound"]
)
def eval_compound_category():
    return {
        "input": QueryInput(query="Spending on eating out last week"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="eating out"),
                Entity(type="temporal", value="last week")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Exact(value="eating out")},
            {"type": Exact(value="temporal"), "value": Exact(value="last week")}
        ])
    }
    }


@eval_case(
    name="utilities_category",
    agent_class=ProcessableEntityExtractionAgent,
    description="Utilities category",
    tags=["category", "utilities"]
)
def eval_utilities_category():
    return {
        "input": QueryInput(query="Council tax payments in 2024"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="Council tax"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Substring(value="Council tax")},
            {"type": Exact(value="temporal"), "value": Exact(value="2024")}
        ])
    }
    }


@eval_case(
    name="entertainment_category",
    agent_class=ProcessableEntityExtractionAgent,
    description="Entertainment category variant",
    tags=["category", "entertainment"]
)
def eval_entertainment_category():
    return {
        "input": QueryInput(query="Fun & leisure costs last month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="Fun & leisure"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Exact(value="Fun & leisure")},
            {"type": Exact(value="temporal"), "value": Exact(value="last month")}
        ])
    }
    }


@eval_case(
    name="simple_category",
    agent_class=ProcessableEntityExtractionAgent,
    description="Simple category extraction",
    tags=["category", "basic"]
)
def eval_simple_category():
    return {
        "input": QueryInput(query="Transport spending"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="category", value="Transport")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Exact(value="Transport")}
        ])
    }
    }


# ========== Amount Extraction Tests (4) ==========

@eval_case(
    name="amount_with_symbol",
    agent_class=ProcessableEntityExtractionAgent,
    description="Amount with pound symbol",
    tags=["amount", "currency"]
)
def eval_amount_with_symbol():
    return {
        "input": QueryInput(query="Items below £15 at shops"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="below £15"),
                Entity(type="category", value="shops")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="amount"), "value": Exact(value="below £15")},
            {"type": Exact(value="category"), "value": Exact(value="shops")}
        ])
    }
    }


@eval_case(
    name="amount_without_symbol",
    agent_class=ProcessableEntityExtractionAgent,
    description="Amount without currency symbol",
    tags=["amount"]
)
def eval_amount_without_symbol():
    return {
        "input": QueryInput(query="Purchases above 50 pounds"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="amount", value="above 50 pounds")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="amount"), "value": Exact(value="above 50 pounds")}
        ])
    }
    }


@eval_case(
    name="exact_decimal",
    agent_class=ProcessableEntityExtractionAgent,
    description="Exact decimal amount",
    tags=["amount", "decimal"]
)
def eval_exact_decimal():
    return {
        "input": QueryInput(query="Payments of precisely £29.95"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="amount", value="precisely £29.95")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="amount"), "value": Substring(value="£29.95")}  # "precisely" modifier is optional
        ])
    }
    }


@eval_case(
    name="amount_at_threshold",
    agent_class=ProcessableEntityExtractionAgent,
    description="Amount at specific threshold",
    tags=["amount", "threshold"]
)
def eval_amount_at_threshold():
    return {
        "input": QueryInput(query="Transactions at £50"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="amount", value="at £50")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="amount"), "value": Substring(value="£50")}
        ])
    }
    }


# ========== Environmental Extraction Tests (2) ==========

@eval_case(
    name="carbon_footprint",
    agent_class=ProcessableEntityExtractionAgent,
    description="Carbon footprint extraction",
    tags=["environmental", "carbon"]
)
def eval_carbon_footprint():
    return {
        "input": QueryInput(query="Calculate carbon footprint from flights this year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="environmental", value="carbon footprint"),
                Entity(type="category", value="flights"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="environmental"), "value": Exact(value="carbon footprint")},
            {"type": Exact(value="category"), "value": Exact(value="flights")},
            {"type": Exact(value="temporal"), "value": Exact(value="this year")}
        ])
    }
    }


@eval_case(
    name="co2_emissions",
    agent_class=ProcessableEntityExtractionAgent,
    description="CO2 emissions extraction",
    tags=["environmental", "co2"]
)
def eval_co2_emissions():
    return {
        "input": QueryInput(query="CO2 emissions from purchases"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="environmental", value="CO2 emissions")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="environmental"), "value": Exact(value="CO2 emissions")}
        ])
    }
    }


# ========== Entity Class References Tests (3) ==========

@eval_case(
    name="category_class_reference",
    agent_class=ProcessableEntityExtractionAgent,
    description="Category as class reference",
    tags=["category", "class-reference"]
)
def eval_category_class_reference():
    return {
        "input": QueryInput(query="Break down spending by category"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="category", value="category")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Exact(value="category")}
        ])
    }
    }


@eval_case(
    name="merchant_class_reference",
    agent_class=ProcessableEntityExtractionAgent,
    description="Merchant as class reference",
    tags=["merchant", "class-reference"]
)
def eval_merchant_class_reference():
    return {
        "input": QueryInput(query="List transactions by merchant"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="merchant", value="merchant")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="merchant")}
        ])
    }
    }


@eval_case(
    name="temporal_class_reference",
    agent_class=ProcessableEntityExtractionAgent,
    description="Month as temporal class reference",
    tags=["temporal", "class-reference"]
)
def eval_temporal_class_reference():
    return {
        "input": QueryInput(query="Organize expenses by month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="temporal", value="month")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="temporal"), "value": Exact(value="month")}
        ])
    }
    }


# ========== Negative Cases - What NOT to Extract (4) ==========

@eval_case(
    name="ignore_geographic",
    agent_class=ProcessableEntityExtractionAgent,
    description="Should not extract geographic location",
    tags=["negative", "geographic"]
)
def eval_ignore_geographic():
    return {
        "input": QueryInput(query="Purchases in Manchester yesterday"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="temporal", value="yesterday")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="temporal"), "value": Exact(value="yesterday")}
        ])
    }
    }


@eval_case(
    name="ignore_payment_method",
    agent_class=ProcessableEntityExtractionAgent,
    description="Should not extract payment method",
    tags=["negative", "payment-method"]
)
def eval_ignore_payment_method():
    return {
        "input": QueryInput(query="Debit card purchases at Costa"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="merchant", value="Costa")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="merchant"), "value": Exact(value="Costa")}
        ])
    }
    }


@eval_case(
    name="ignore_person_names",
    agent_class=ProcessableEntityExtractionAgent,
    description="Should not extract person names",
    tags=["negative", "person-names"]
)
def eval_ignore_person_names():
    return {
        "input": QueryInput(query="Payment to Sarah Jones yesterday"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[Entity(type="temporal", value="yesterday")]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="temporal"), "value": Exact(value="yesterday")}
        ])
    }
    }


@eval_case(
    name="ignore_channel",
    agent_class=ProcessableEntityExtractionAgent,
    description="Should not extract transaction channel",
    tags=["negative", "channel"]
)
def eval_ignore_channel():
    return {
        "input": QueryInput(query="In-store shopping at Zara today"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="shopping"),
                Entity(type="merchant", value="Zara"),
                Entity(type="temporal", value="today")
            ]
        ),
        "field_validations": {
        "entities": ListMatches(items=[
            {"type": Exact(value="category"), "value": Exact(value="shopping")},
            {"type": Exact(value="merchant"), "value": Exact(value="Zara")},
            {"type": Exact(value="temporal"), "value": Exact(value="today")}
        ])
    }
    }


# ========== Budget Entity Tests (1) ==========

@eval_case(
    name="budget_query",
    agent_class=ProcessableEntityExtractionAgent,
    description="Extract budget entity and category",
    tags=["budget", "category"]
)
def eval_budget_query():
    return {
        "input": QueryInput(query="My expenses budget?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="expenses"),
                Entity(type="budget", value="budget")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="expenses")},
                {"type": Exact(value="budget"), "value": Exact(value="budget")}
            ])
        }
    }


# ========== Compound Entity Tests (1) ==========

@eval_case(
    name="home_repairs_category",
    agent_class=ProcessableEntityExtractionAgent,
    description="Extract compound category term 'home repairs'",
    tags=["category", "compound", "temporal"]
)
def eval_home_repairs_category():
    return {
        "input": QueryInput(query="How much I have spent on home repairs in 2025?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="home repairs"),
                Entity(type="temporal", value="2025")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="home repairs")},
                {"type": Exact(value="temporal"), "value": Exact(value="2025")}
            ])
        }
    }


# ========== Tiered Entity Tests (1) ==========

@eval_case(
    name="tier1_category_income",
    agent_class=ProcessableEntityExtractionAgent,
    description="Extract tier 1 category 'income'",
    tags=["category", "tier1"]
)
def eval_tier1_category_income():
    return {
        "input": QueryInput(query="Show me all income this year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="income"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="income")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }