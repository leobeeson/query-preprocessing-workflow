"""
Pydantic models for Query Characteristics Extraction.

These models represent the input and output for the QueryCharacteristicsExtractionAgent,
which analyzes natural language queries to determine SQL structure and feasibility.

Note: Using str instead of Literal types for resilience against LLM variations.
Expected values are documented in Field descriptions.
"""

from typing import List, Optional
from pydantic import BaseModel, Field

from src.models.entity_extraction_models import ProcessableEntity


# ============================================================================
# INPUT MODELS
# ============================================================================

class QueryCharacteristicsInput(BaseModel):
    """
    Input model for QueryCharacteristicsExtractionAgent.
    Contains the user query and extracted processable entities.
    """
    query: str = Field(
        description="The user's natural language query"
    )
    processable_entities: List[ProcessableEntity] = Field(
        default_factory=list,
        description="List of processable entities extracted from the query"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "query": "How much did I spend on groceries last month?",
                "processable_entities": [
                    {"type": "category", "value": "groceries"},
                    {"type": "temporal", "value": "last month"}
                ]
            }
        }


# ============================================================================
# SQL OPERATIONS MODELS
# ============================================================================

class Aggregation(BaseModel):
    """Represents an aggregation function in SQL"""
    function: str = Field(
        description="Aggregation function: SUM, COUNT, AVG, MIN, MAX"
    )
    column: str = Field(
        description="Column to aggregate"
    )
    alias: str = Field(
        description="Alias for the aggregated result"
    )


class Filter(BaseModel):
    """Represents a WHERE clause filter"""
    column: str = Field(
        description="Column to filter on"
    )
    operator: str = Field(
        description="Filter operator: =, !=, >, <, >=, <=, ILIKE, IN, BETWEEN, IS NULL, IS NOT NULL"
    )


class OrderBy(BaseModel):
    """Represents an ORDER BY clause"""
    column: str = Field(
        description="Column or alias to order by"
    )
    direction: str = Field(
        description="Sort direction: ASC or DESC"
    )


class Join(BaseModel):
    """Represents a JOIN operation"""
    table: str = Field(
        description="Table to join: budgets"
    )
    on: str = Field(
        description="Column to join on"
    )


class SQLOperations(BaseModel):
    """
    Collection of SQL operations needed for the query.
    All fields initialized with defaults for complete structure.
    """
    aggregations: List[Aggregation] = Field(
        default_factory=list,
        description="List of aggregation functions needed"
    )
    filters: List[Filter] = Field(
        default_factory=list,
        description="List of WHERE clause filters"
    )
    group_by: List[str] = Field(
        default_factory=list,
        description="List of columns to group by"
    )
    order_by: List[OrderBy] = Field(
        default_factory=list,
        description="List of ORDER BY clauses"
    )
    limit: Optional[int] = Field(
        default=None,
        description="Row limit for the query"
    )
    joins: Optional[Join] = Field(
        default=None,
        description="Join operation if needed"
    )


# ============================================================================
# ADVANCED SQL MODELS
# ============================================================================

class WindowFunction(BaseModel):
    """Represents a window function operation"""
    function: str = Field(
        description="Window function: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD"
    )
    partition_by: List[str] = Field(
        default_factory=list,
        description="Columns to partition by"
    )
    order_by: List[str] = Field(
        default_factory=list,
        description="Columns to order by within partition"
    )


class AdvancedSQL(BaseModel):
    """
    Advanced SQL features that may be needed.
    All fields initialized with defaults for complete structure.
    """
    cte_required: bool = Field(
        default=False,
        description="Whether Common Table Expressions (CTEs) are needed"
    )
    cte_purpose: Optional[str] = Field(
        default=None,
        description="Purpose of the CTE if required (max 15 words)"
    )
    window_functions: List[WindowFunction] = Field(
        default_factory=list,
        description="List of window functions needed"
    )
    case_statements: List[str] = Field(
        default_factory=list,
        description="List of CASE statement purposes (max 15 words each)"
    )
    set_operations: Optional[str] = Field(
        default=None,
        description="Set operation if needed: UNION, UNION ALL, INTERSECT, EXCEPT"
    )
    subqueries: bool = Field(
        default=False,
        description="Whether subqueries are needed"
    )


# ============================================================================
# MISSING REQUIREMENTS MODELS
# ============================================================================

class MissingRequirement(BaseModel):
    """Represents a missing requirement that prevents SQL generation"""
    type: str = Field(
        description="Type of missing requirement (e.g., amount_threshold, geographic_location)"
    )
    description: str = Field(
        description="Clear explanation of what's missing (max 20 words)"
    )
    severity: str = Field(
        description="Severity level: critical or warning"
    )
    possible_resolutions: List[str] = Field(
        default_factory=list,
        description="List of possible ways to resolve this requirement (max 15 words each)"
    )


# ============================================================================
# OUTPUT MODEL
# ============================================================================

class QueryCharacteristicsOutput(BaseModel):
    """
    Complete output model for QueryCharacteristicsExtractionAgent.

    This model represents the complete, predictable JSON structure returned
    to clients after parsing the minimal XML from the LLM. All fields are
    always present with appropriate defaults.
    """
    sql_feasible: bool = Field(
        description="Whether the query can be translated into executable SQL"
    )
    confidence: float = Field(
        description="Confidence level in the analysis (0.0 to 1.0)"
    )
    patterns: List[str] = Field(
        default_factory=list,
        description="Query patterns: AGGREGATION, GROUPED_AGGREGATION, RANKING, LISTING, COMPARISON, TREND_ANALYSIS, BUDGET_QUERY, SNAPSHOT"
    )
    sql_operations: Optional[SQLOperations] = Field(
        default=None,
        description="SQL operations needed (null when sql_feasible=false)"
    )
    advanced_sql: Optional[AdvancedSQL] = Field(
        default=None,
        description="Advanced SQL features needed (null when sql_feasible=false)"
    )
    missing_requirements: List[MissingRequirement] = Field(
        default_factory=list,
        description="List of missing requirements (empty when sql_feasible=true)"
    )
    explanation: str = Field(
        description="Human-readable explanation of the analysis (max 20 words)"
    )
    raw_response: Optional[str] = Field(
        default=None,
        description="Raw LLM XML response for debugging"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "sql_feasible": True,
                "confidence": 0.95,
                "patterns": ["AGGREGATION"],
                "sql_operations": {
                    "aggregations": [
                        {"function": "SUM", "column": "amount", "alias": "total_spend"}
                    ],
                    "filters": [
                        {"column": "category_code", "operator": "ILIKE"},
                        {"column": "transaction_booking_timestamp", "operator": "BETWEEN"}
                    ],
                    "group_by": [],
                    "order_by": [],
                    "limit": None,
                    "joins": None
                },
                "advanced_sql": {
                    "cte_required": False,
                    "cte_purpose": None,
                    "window_functions": [],
                    "case_statements": [],
                    "set_operations": None,
                    "subqueries": False
                },
                "missing_requirements": [],
                "explanation": "Sum of grocery transactions for previous calendar month",
                "raw_response": "<response>...</response>"
            }
        }
