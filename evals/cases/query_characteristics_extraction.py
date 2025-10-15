"""
Evaluation cases for QueryCharacteristicsExtractionAgent using decorator pattern.

Each case mirrors a prompt example but uses different content to test generalization.
"""

from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact, Substring, Contains
from src.workflow_nodes.query_preprocessing.query_characteristics_extraction_agent import QueryCharacteristicsExtractionAgent
from src.models.query_characteristics_models import (
    QueryCharacteristicsInput,
    QueryCharacteristicsOutput,
    SQLOperations,
    AdvancedSQL,
    Aggregation,
    Filter,
    OrderBy,
    Join,
    WindowFunction,
    MissingRequirement
)
from src.models.entity_extraction_models import ProcessableEntity


# ========== Feasible Query Tests (9 cases) ==========

@eval_case(
    name="simple_aggregation_transport",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Simple aggregation on transport category (mirrors: groceries 2024)",
    tags=["aggregation", "feasible", "basic", "dev_cases"]
)
def eval_simple_aggregation_transport():
    """
    Mirrors prompt example: 'How much did I spend on groceries in 2024?'
    Tests: Simple SUM aggregation with category and temporal filters
    """
    return {
        "input": QueryCharacteristicsInput(
            query="How much did I spend on transport last year?",
            processable_entities=[
                ProcessableEntity(type="category", value="transport"),
                ProcessableEntity(type="temporal", value="last year")
            ]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.95,
            patterns=["AGGREGATION"],
            sql_operations=SQLOperations(
                aggregations=[
                    Aggregation(function="SUM", column="amount", alias="total_spend")
                ],
                filters=[
                    Filter(column="category_code", operator="ILIKE"),
                    Filter(column="transaction_booking_timestamp", operator="BETWEEN")
                ],
                group_by=[],
                order_by=[],
                limit=None,
                joins=None
            ),
            advanced_sql=AdvancedSQL(
                cte_required=False,
                cte_purpose=None,
                window_functions=[],
                case_statements=[],
                set_operations=None,
                subqueries=False
            ),
            missing_requirements=[],
            explanation="Sum of transport transactions for previous year"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["AGGREGATION"]),
            "sql_operations.aggregations": ListMatches(items=[
                {"function": Exact(value="SUM"), "column": Exact(value="amount")}
            ]),
            "sql_operations.filters": ListMatches(items=[
                {"column": Exact(value="category_code"), "operator": Exact(value="ILIKE")},
                {"column": Exact(value="transaction_booking_timestamp"), "operator": Substring(value="BETWEEN")}
            ]),
            "advanced_sql.cte_required": Exact(value=False)
        }
    }


@eval_case(
    name="grouped_ranking_merchants",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Grouped aggregation with ranking for merchants (mirrors: top 5 categories)",
    tags=["aggregation", "ranking", "grouped", "feasible", "dev_cases"]
)
def eval_grouped_ranking_merchants():
    """Mirrors prompt example: 'Top 5 spending categories last month'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Show me my top 10 merchants by spending this month",
            processable_entities=[
                ProcessableEntity(type="merchant", value="merchant"),
                ProcessableEntity(type="temporal", value="this month")
            ]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.92,
            patterns=["GROUPED_AGGREGATION", "RANKING"],
            sql_operations=SQLOperations(
                aggregations=[Aggregation(function="SUM", column="amount", alias="total_spend")],
                filters=[Filter(column="transaction_booking_timestamp", operator="BETWEEN")],
                group_by=["merchant_brand_name"],
                order_by=[OrderBy(column="total_spend", direction="DESC")],
                limit=10,
                joins=None
            ),
            advanced_sql=AdvancedSQL(cte_required=False),
            missing_requirements=[],
            explanation="Groups by merchant, sums spending, returns top 10"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["GROUPED_AGGREGATION", "RANKING"]),
            "sql_operations.aggregations": ListMatches(items=[{"function": Exact(value="SUM"), "column": Exact(value="amount")}]),
            "sql_operations.group_by": Contains(values=["merchant_brand_name"]),
            "sql_operations.order_by": ListMatches(items=[{"column": Substring(value="total"), "direction": Exact(value="DESC")}]),
            "sql_operations.limit": Exact(value=10)
        }
    }


@eval_case(
    name="comparison_months",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Month-over-month comparison (mirrors: year-over-year comparison)",
    tags=["comparison", "aggregation", "cte", "feasible", "dev_cases"]
)
def eval_comparison_months():
    """Mirrors prompt example: 'Percentage change in total grocery spend in 2025 compared to 2024'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Compare my dining spending between January and February",
            processable_entities=[
                ProcessableEntity(type="category", value="dining"),
                ProcessableEntity(type="temporal", value="January"),
                ProcessableEntity(type="temporal", value="February")
            ]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.93,
            patterns=["COMPARISON", "AGGREGATION"],
            sql_operations=SQLOperations(
                aggregations=[Aggregation(function="SUM", column="amount", alias="monthly_total")],
                filters=[Filter(column="category_code", operator="ILIKE"), Filter(column="transaction_booking_timestamp", operator="BETWEEN")],
                group_by=["transaction_booking_timestamp"],
                order_by=[],
                limit=None,
                joins=None
            ),
            advanced_sql=AdvancedSQL(cte_required=True, cte_purpose="Aggregate by month then pivot for comparison", window_functions=[], case_statements=["Pivot months to columns for comparison"]),
            missing_requirements=[],
            explanation="Compares dining spending between January and February using CTE and CASE"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["COMPARISON", "AGGREGATION"]),
            "sql_operations.aggregations": ListMatches(items=[{"function": Exact(value="SUM"), "column": Exact(value="amount")}]),
            "sql_operations.filters": ListMatches(items=[{"column": Exact(value="category_code"), "operator": Exact(value="ILIKE")}]),
            "advanced_sql.cte_required": Exact(value=True)
        }
    }


@eval_case(
    name="budget_snapshot",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Simple budget query (mirrors: grocery budget)",
    tags=["budget", "snapshot", "feasible", "dev_cases"]
)
def eval_budget_snapshot():
    """Mirrors prompt example: 'What's my grocery budget?'"""
    return {
        "input": QueryCharacteristicsInput(
            query="What's my entertainment budget?",
            processable_entities=[
                ProcessableEntity(type="category", value="entertainment"),
                ProcessableEntity(type="budget", value="budget")
            ]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.98,
            patterns=["BUDGET_QUERY", "SNAPSHOT"],
            sql_operations=SQLOperations(aggregations=[], filters=[Filter(column="category_tier_2", operator="ILIKE")], group_by=[], order_by=[], limit=None, joins=None),
            advanced_sql=AdvancedSQL(cte_required=False),
            missing_requirements=[],
            explanation="Retrieves budget amount for entertainment category from budgets table"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["BUDGET_QUERY", "SNAPSHOT"]),
            "sql_operations.filters": ListMatches(items=[{"column": Substring(value="category")}])
        }
    }


@eval_case(
    name="budget_comparison_transport",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Budget comparison with join (mirrors: over budget on groceries)",
    tags=["budget", "comparison", "join", "feasible", "dev_cases"]
)
def eval_budget_comparison_transport():
    """Mirrors prompt example: 'Am I over budget on groceries this month?'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Am I over budget on transport this week?",
            processable_entities=[
                ProcessableEntity(type="category", value="transport"),
                ProcessableEntity(type="temporal", value="this week"),
                ProcessableEntity(type="budget", value="budget")
            ]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.90,
            patterns=["BUDGET_QUERY", "COMPARISON", "AGGREGATION"],
            sql_operations=SQLOperations(
                aggregations=[Aggregation(function="SUM", column="amount", alias="actual_spend")],
                filters=[Filter(column="category_code", operator="ILIKE"), Filter(column="transaction_booking_timestamp", operator=">=")],
                group_by=["category_code"],
                order_by=[],
                limit=None,
                joins=Join(table="budgets", on="category_code")
            ),
            advanced_sql=AdvancedSQL(cte_required=False, window_functions=[], case_statements=["Compare actual spending to budget amount"]),
            missing_requirements=[],
            explanation="Joins with budgets, sums transport spending, compares to budget"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["BUDGET_QUERY", "COMPARISON", "AGGREGATION"]),
            "sql_operations.aggregations": ListMatches(items=[{"function": Exact(value="SUM"), "column": Exact(value="amount")}]),
            "sql_operations.joins.table": Exact(value="budgets"),
            "sql_operations.joins.on": Exact(value="category_code")
        }
    }


@eval_case(
    name="listing_merchant",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Transaction listing query (mirrors: Tesco transactions)",
    tags=["listing", "merchant", "feasible", "dev_cases"]
)
def eval_listing_merchant():
    """Mirrors prompt example: 'Show my recent transactions at Tesco'"""
    return {
        "input": QueryCharacteristicsInput(
            query="List my Amazon transactions",
            processable_entities=[ProcessableEntity(type="merchant", value="Amazon")]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.94,
            patterns=["LISTING"],
            sql_operations=SQLOperations(
                aggregations=[],
                filters=[Filter(column="merchant_brand_name", operator="ILIKE")],
                group_by=[],
                order_by=[OrderBy(column="transaction_booking_timestamp", direction="DESC")],
                limit=50,
                joins=None
            ),
            advanced_sql=AdvancedSQL(cte_required=False),
            missing_requirements=[],
            explanation="Lists Amazon transactions ordered by date with default limit"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["LISTING"]),
            "sql_operations.filters": ListMatches(items=[{"column": Substring(value="merchant"), "operator": Exact(value="ILIKE")}]),
            "sql_operations.order_by": ListMatches(items=[{"column": Substring(value="timestamp"), "direction": Exact(value="DESC")}])
        }
    }


@eval_case(
    name="trend_analysis_weekly",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Trend analysis query (mirrors: monthly spending trend)",
    tags=["trend", "aggregation", "grouped", "feasible", "dev_cases"]
)
def eval_trend_analysis_weekly():
    """Mirrors prompt example: 'Show my monthly spending trend for this year'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Show my weekly spending pattern for the last 3 months",
            processable_entities=[ProcessableEntity(type="temporal", value="last 3 months")]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.91,
            patterns=["TREND_ANALYSIS", "GROUPED_AGGREGATION"],
            sql_operations=SQLOperations(
                aggregations=[Aggregation(function="SUM", column="amount", alias="weekly_spend")],
                filters=[Filter(column="transaction_booking_timestamp", operator=">=")],
                group_by=["transaction_booking_timestamp"],
                order_by=[OrderBy(column="transaction_booking_timestamp", direction="ASC")],
                limit=None,
                joins=None
            ),
            advanced_sql=AdvancedSQL(cte_required=False),
            missing_requirements=[],
            explanation="Aggregates spending by week for last 3 months to show pattern"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["TREND_ANALYSIS", "GROUPED_AGGREGATION"]),
            "sql_operations.aggregations": ListMatches(items=[{"function": Exact(value="SUM"), "column": Exact(value="amount")}]),
            "sql_operations.group_by": Contains(values=["transaction_booking_timestamp"]),
            "sql_operations.order_by": ListMatches(items=[{"direction": Exact(value="ASC")}])
        }
    }


@eval_case(
    name="subscription_aggregation",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Subscription query (mirrors: subscriptions 2024)",
    tags=["subscription", "aggregation", "feasible", "dev_cases"]
)
def eval_subscription_aggregation():
    """Mirrors prompt example: 'How much did I spend on subscriptions in 2024?'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Total subscription spend in Q1 2025",
            processable_entities=[ProcessableEntity(type="temporal", value="Q1 2025")]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.96,
            patterns=["AGGREGATION"],
            sql_operations=SQLOperations(
                aggregations=[Aggregation(function="SUM", column="amount", alias="subscription_total")],
                filters=[Filter(column="recurring_payment_id", operator="IS NOT NULL"), Filter(column="transaction_booking_timestamp", operator="BETWEEN")],
                group_by=[],
                order_by=[],
                limit=None,
                joins=None
            ),
            advanced_sql=AdvancedSQL(cte_required=False),
            missing_requirements=[],
            explanation="Sums subscription transactions for Q1 2025"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["AGGREGATION"]),
            "sql_operations.aggregations": ListMatches(items=[{"function": Exact(value="SUM"), "column": Exact(value="amount")}]),
            "sql_operations.filters": ListMatches(items=[{"column": Exact(value="recurring_payment_id"), "operator": Exact(value="IS NOT NULL")}])
        }
    }


@eval_case(
    name="complex_multidimension",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Complex multi-dimension query (mirrors: year-over-year daily average)",
    tags=["complex", "comparison", "aggregation", "cte", "window", "feasible", "dev_cases"]
)
def eval_complex_multidimension():
    """Mirrors prompt example: 'Year-over-year average daily spend by category'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Month-over-month average transaction size by merchant",
            processable_entities=[ProcessableEntity(type="merchant", value="merchant")]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=True,
            confidence=0.88,
            patterns=["COMPARISON", "GROUPED_AGGREGATION", "TREND_ANALYSIS"],
            sql_operations=SQLOperations(
                aggregations=[Aggregation(function="AVG", column="amount", alias="avg_transaction")],
                filters=[],
                group_by=["transaction_booking_timestamp", "merchant_brand_name"],
                order_by=[],
                limit=None,
                joins=None
            ),
            advanced_sql=AdvancedSQL(
                cte_required=True,
                cte_purpose="Calculate monthly averages first, then compare across months",
                window_functions=[WindowFunction(function="ROW_NUMBER", partition_by=["merchant_brand_name"], order_by=[])],
                case_statements=["Calculate percentage change between months"]
            ),
            missing_requirements=[],
            explanation="Complex calculation comparing average transaction size by merchant across months"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=True),
            "patterns": Contains(values=["COMPARISON", "GROUPED_AGGREGATION", "TREND_ANALYSIS"]),
            "sql_operations.aggregations": ListMatches(items=[{"function": Exact(value="AVG"), "column": Exact(value="amount")}]),
            "advanced_sql.cte_required": Exact(value=True),
            "advanced_sql.window_functions": ListMatches(items=[{"function": Substring(value="ROW_NUMBER")}])
        }
    }


# ========== Infeasible Query Tests (2 cases) ==========

@eval_case(
    name="missing_threshold_subscriptions",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Infeasible query missing threshold (mirrors: big purchases)",
    tags=["infeasible", "missing", "dev_cases"]
)
def eval_missing_threshold_subscriptions():
    """Mirrors prompt example: 'Show me my big purchases last month'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Show expensive subscriptions last quarter",
            processable_entities=[ProcessableEntity(type="temporal", value="last quarter")]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=False,
            confidence=0.25,
            patterns=["LISTING"],
            sql_operations=None,
            advanced_sql=None,
            missing_requirements=[
                MissingRequirement(
                    type="amount_threshold",
                    description="Cannot determine numeric threshold for 'expensive'",
                    severity="critical",
                    possible_resolutions=["Request specific amount from user", "Use 90th percentile of subscription amounts", "Apply default threshold"]
                )
            ],
            explanation="Cannot generate SQL without defining what constitutes 'expensive'"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=False),
            "patterns": Contains(values=["LISTING"]),
            "sql_operations": Exact(value=None),
            "advanced_sql": Exact(value=None),
            "missing_requirements": ListMatches(items=[{"type": Exact(value="amount_threshold"), "severity": Exact(value="critical")}])
        }
    }


@eval_case(
    name="multiple_missing_cash_location",
    agent_class=QueryCharacteristicsExtractionAgent,
    description="Infeasible query with multiple missing requirements (mirrors: credit card + London)",
    tags=["infeasible", "multiple_missing", "dev_cases"]
)
def eval_multiple_missing_cash_location():
    """Mirrors prompt example: 'Show me large credit card purchases in London'"""
    return {
        "input": QueryCharacteristicsInput(
            query="Show small cash purchases in Edinburgh",
            processable_entities=[]
        ),
        "expected": QueryCharacteristicsOutput(
            sql_feasible=False,
            confidence=0.15,
            patterns=["LISTING"],
            sql_operations=None,
            advanced_sql=None,
            missing_requirements=[
                MissingRequirement(type="amount_threshold", description="Cannot determine what constitutes 'small' purchases", severity="critical", possible_resolutions=["Request specific amount threshold from user"]),
                MissingRequirement(type="payment_method", description="Payment method data not available in schema", severity="critical", possible_resolutions=["Cannot filter by payment method"]),
                MissingRequirement(type="geographic_location", description="Transaction location data not available", severity="critical", possible_resolutions=["Cannot filter by geographic location"])
            ],
            explanation="Multiple critical data elements missing"
        ),
        "field_validations": {
            "sql_feasible": Exact(value=False),
            "sql_operations": Exact(value=None),
            "advanced_sql": Exact(value=None),
            "missing_requirements": ListMatches(items=[
                {"type": Exact(value="amount_threshold"), "severity": Exact(value="critical")},
                {"type": Exact(value="payment_method"), "severity": Exact(value="critical")},
                {"type": Exact(value="geographic_location"), "severity": Exact(value="critical")}
            ])
        }
    }
