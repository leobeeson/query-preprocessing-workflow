#!/usr/bin/env python3
"""
Unit tests for QueryCharacteristicsExtractionAgent

These tests focus on the parse_response() method and its helpers,
using the XML examples from the specification (05_query_characteristics_efficient.md).
"""

import pytest
from typing import List

from src.workflow_nodes.query_preprocessing.query_characteristics_extraction_agent import QueryCharacteristicsExtractionAgent
from src.models.query_characteristics_models import QueryCharacteristicsOutput


class TestQueryCharacteristicsParseResponse:
    """Test the parse_response() method with specification examples"""

    def test_simple_aggregation(self):
        """Test parsing simple aggregation query (spec 5.1)"""
        xml_response = """<response>
  <sql_feasible>true</sql_feasible>
  <confidence>0.95</confidence>
  <patterns>
    <pattern>AGGREGATION</pattern>
  </patterns>
  <operations>
    <aggregation function="SUM" column="amount" alias="total_spend"/>
    <filter column="category_code" operator="ILIKE"/>
    <filter column="transaction_booking_timestamp" operator="BETWEEN"/>
  </operations>
  <explanation>Sum of grocery transactions for previous calendar month</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.sql_feasible is True
        assert result.confidence == 0.95
        assert result.patterns == ["AGGREGATION"]
        assert result.sql_operations is not None
        assert len(result.sql_operations.aggregations) == 1
        assert result.sql_operations.aggregations[0].function == "SUM"
        assert result.sql_operations.aggregations[0].column == "amount"
        assert result.sql_operations.aggregations[0].alias == "total_spend"
        assert len(result.sql_operations.filters) == 2
        assert result.sql_operations.filters[0].column == "category_code"
        assert result.sql_operations.filters[0].operator == "ILIKE"
        assert result.sql_operations.group_by == []
        assert result.sql_operations.order_by == []
        assert result.sql_operations.limit is None
        assert result.sql_operations.joins is None
        assert result.advanced_sql is not None
        assert result.advanced_sql.cte_required is False
        assert result.advanced_sql.window_functions == []
        assert result.missing_requirements == []
        assert "Sum of grocery transactions" in result.explanation

    def test_ranking_query(self):
        """Test parsing ranking query with multiple patterns (spec 5.2)"""
        xml_response = """<response>
  <sql_feasible>true</sql_feasible>
  <confidence>0.92</confidence>
  <patterns>
    <pattern>GROUPED_AGGREGATION</pattern>
    <pattern>RANKING</pattern>
  </patterns>
  <operations>
    <aggregation function="SUM" column="amount" alias="total_spend"/>
    <filter column="transaction_booking_timestamp" operator="BETWEEN"/>
    <group_by>category_code</group_by>
    <order_by column="total_spend" direction="DESC"/>
    <limit>5</limit>
  </operations>
  <explanation>Groups by category, sums spending for last month, returns top 5</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.sql_feasible is True
        assert result.confidence == 0.92
        assert result.patterns == ["GROUPED_AGGREGATION", "RANKING"]
        assert result.sql_operations.group_by == ["category_code"]
        assert len(result.sql_operations.order_by) == 1
        assert result.sql_operations.order_by[0].column == "total_spend"
        assert result.sql_operations.order_by[0].direction == "DESC"
        assert result.sql_operations.limit == 5

    def test_complex_comparison_with_cte(self):
        """Test parsing complex query with CTE and CASE (spec 5.3)"""
        xml_response = """<response>
  <sql_feasible>true</sql_feasible>
  <confidence>0.93</confidence>
  <patterns>
    <pattern>COMPARISON</pattern>
    <pattern>AGGREGATION</pattern>
  </patterns>
  <operations>
    <aggregation function="SUM" column="amount" alias="yearly_total"/>
    <filter column="category_code" operator="ILIKE"/>
    <filter column="transaction_booking_timestamp" operator="BETWEEN"/>
    <group_by>transaction_booking_timestamp</group_by>
    <requires_cte>true</requires_cte>
    <cte_purpose>Aggregate by year then pivot for comparison</cte_purpose>
    <case_statement purpose="Pivot years to columns"/>
  </operations>
  <explanation>Compares grocery spending between 2024 and 2025 using CTE and CASE for pivoting</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.sql_feasible is True
        assert result.confidence == 0.93
        assert result.patterns == ["COMPARISON", "AGGREGATION"]
        assert result.advanced_sql.cte_required is True
        assert result.advanced_sql.cte_purpose == "Aggregate by year then pivot for comparison"
        assert len(result.advanced_sql.case_statements) == 1
        assert result.advanced_sql.case_statements[0] == "Pivot years to columns"

    def test_infeasible_query(self):
        """Test parsing infeasible query with missing requirements (spec 5.4)"""
        xml_response = """<response>
  <sql_feasible>false</sql_feasible>
  <confidence>0.25</confidence>
  <patterns>
    <pattern>LISTING</pattern>
  </patterns>
  <missing_requirements>
    <missing_requirement>
      <type>amount_threshold</type>
      <description>Cannot determine numeric threshold for 'big purchases'</description>
      <severity>critical</severity>
      <resolutions>
        <resolution>Request specific amount from user</resolution>
        <resolution>Use 90th percentile of transaction history</resolution>
        <resolution>Apply default threshold of £100</resolution>
      </resolutions>
    </missing_requirement>
  </missing_requirements>
  <explanation>Cannot generate SQL without defining what constitutes a 'big' purchase</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.sql_feasible is False
        assert result.confidence == 0.25
        assert result.patterns == ["LISTING"]
        assert result.sql_operations is None
        assert result.advanced_sql is None
        assert len(result.missing_requirements) == 1
        assert result.missing_requirements[0].type == "amount_threshold"
        assert result.missing_requirements[0].severity == "critical"
        assert len(result.missing_requirements[0].possible_resolutions) == 3
        assert "Request specific amount" in result.missing_requirements[0].possible_resolutions[0]

    def test_budget_query_with_join(self):
        """Test parsing budget query with join and CASE (spec 5.5)"""
        xml_response = """<response>
  <sql_feasible>true</sql_feasible>
  <confidence>0.90</confidence>
  <patterns>
    <pattern>BUDGET_QUERY</pattern>
    <pattern>COMPARISON</pattern>
  </patterns>
  <operations>
    <aggregation function="SUM" column="amount" alias="actual_spend"/>
    <filter column="category_code" operator="ILIKE"/>
    <filter column="transaction_booking_timestamp" operator=">="/>
    <group_by>category_code</group_by>
    <join table="budgets" on="category_code"/>
    <case_statement purpose="Compare actual to budget amount"/>
  </operations>
  <explanation>Joins transactions with budgets, sums current month grocery spending, compares to budget</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.sql_feasible is True
        assert result.patterns == ["BUDGET_QUERY", "COMPARISON"]
        assert result.sql_operations.joins is not None
        assert result.sql_operations.joins.table == "budgets"
        assert result.sql_operations.joins.on == "category_code"
        assert len(result.advanced_sql.case_statements) == 1

    def test_multiple_missing_requirements(self):
        """Test parsing query with multiple missing requirements"""
        xml_response = """<response>
  <sql_feasible>false</sql_feasible>
  <confidence>0.15</confidence>
  <patterns>
    <pattern>LISTING</pattern>
  </patterns>
  <missing_requirements>
    <missing_requirement>
      <type>amount_threshold</type>
      <description>Cannot determine what constitutes 'large' purchases</description>
      <severity>critical</severity>
      <resolutions>
        <resolution>Request specific amount threshold from user</resolution>
      </resolutions>
    </missing_requirement>
    <missing_requirement>
      <type>payment_method</type>
      <description>Payment method data not available in transaction schema</description>
      <severity>critical</severity>
      <resolutions>
        <resolution>Cannot filter by payment method</resolution>
      </resolutions>
    </missing_requirement>
    <missing_requirement>
      <type>geographic_location</type>
      <description>Transaction location data not available in schema</description>
      <severity>critical</severity>
      <resolutions>
        <resolution>Cannot filter by geographic location</resolution>
      </resolutions>
    </missing_requirement>
  </missing_requirements>
  <explanation>Multiple critical data elements missing for this query</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.sql_feasible is False
        assert len(result.missing_requirements) == 3
        assert result.missing_requirements[0].type == "amount_threshold"
        assert result.missing_requirements[1].type == "payment_method"
        assert result.missing_requirements[2].type == "geographic_location"


class TestQueryCharacteristicsEdgeCases:
    """Test edge cases and error handling"""

    def test_minimal_xml_with_defaults(self):
        """Test that defaults are populated when minimal XML provided"""
        xml_response = """<response>
  <sql_feasible>true</sql_feasible>
  <confidence>0.80</confidence>
  <patterns>
    <pattern>LISTING</pattern>
  </patterns>
  <operations>
    <filter column="merchant_brand_name" operator="ILIKE"/>
  </operations>
  <explanation>Simple merchant filter query</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.sql_operations.aggregations == []
        assert result.sql_operations.group_by == []
        assert result.sql_operations.order_by == []
        assert result.sql_operations.limit is None
        assert result.sql_operations.joins is None
        assert result.advanced_sql.cte_required is False
        assert result.advanced_sql.cte_purpose is None
        assert result.advanced_sql.window_functions == []
        assert result.advanced_sql.case_statements == []
        assert result.advanced_sql.set_operations is None
        assert result.advanced_sql.subqueries is False

    def test_missing_confidence_uses_default(self):
        """Test that missing confidence field defaults to 0.0"""
        xml_response = """<response>
  <sql_feasible>false</sql_feasible>
  <patterns>
    <pattern>LISTING</pattern>
  </patterns>
  <missing_requirements>
    <missing_requirement>
      <type>missing_data</type>
      <description>Data not available</description>
      <severity>critical</severity>
      <resolutions>
        <resolution>Cannot process</resolution>
      </resolutions>
    </missing_requirement>
  </missing_requirements>
  <explanation>Missing data</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.confidence == 0.0

    def test_empty_patterns_list(self):
        """Test query with no patterns"""
        xml_response = """<response>
  <sql_feasible>false</sql_feasible>
  <confidence>0.10</confidence>
  <patterns>
  </patterns>
  <missing_requirements>
    <missing_requirement>
      <type>unclear_intent</type>
      <description>Query intent unclear</description>
      <severity>critical</severity>
      <resolutions>
        <resolution>Request clarification</resolution>
      </resolutions>
    </missing_requirement>
  </missing_requirements>
  <explanation>Cannot determine query intent</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert result.patterns == []

    def test_window_function_with_optional_attributes(self):
        """Test parsing window function with missing partition_by or order_by"""
        xml_response = """<response>
  <sql_feasible>true</sql_feasible>
  <confidence>0.88</confidence>
  <patterns>
    <pattern>RANKING</pattern>
  </patterns>
  <operations>
    <aggregation function="SUM" column="amount" alias="total"/>
    <window_function type="ROW_NUMBER" order_by="amount"/>
  </operations>
  <explanation>Ranking without partitioning</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert len(result.advanced_sql.window_functions) == 1
        assert result.advanced_sql.window_functions[0].function == "ROW_NUMBER"
        assert result.advanced_sql.window_functions[0].partition_by == []
        assert result.advanced_sql.window_functions[0].order_by == ["amount"]

    def test_multiple_aggregations_and_filters(self):
        """Test parsing multiple repeated elements"""
        xml_response = """<response>
  <sql_feasible>true</sql_feasible>
  <confidence>0.90</confidence>
  <patterns>
    <pattern>GROUPED_AGGREGATION</pattern>
  </patterns>
  <operations>
    <aggregation function="SUM" column="amount" alias="total_spend"/>
    <aggregation function="COUNT" column="external_transaction_id" alias="transaction_count"/>
    <aggregation function="AVG" column="amount" alias="avg_spend"/>
    <filter column="category_code" operator="ILIKE"/>
    <filter column="transaction_booking_timestamp" operator="BETWEEN"/>
    <filter column="amount" operator=">"/>
    <group_by>category_code</group_by>
    <group_by>transaction_booking_timestamp</group_by>
  </operations>
  <explanation>Multi-metric aggregation</explanation>
</response>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        result = agent.parse_response(xml_response)

        assert len(result.sql_operations.aggregations) == 3
        assert result.sql_operations.aggregations[0].function == "SUM"
        assert result.sql_operations.aggregations[1].function == "COUNT"
        assert result.sql_operations.aggregations[2].function == "AVG"
        assert len(result.sql_operations.filters) == 3
        assert len(result.sql_operations.group_by) == 2


class TestQueryCharacteristicsHelperMethods:
    """Test individual helper parsing methods"""

    def test_parse_aggregations_helper(self):
        """Test _parse_aggregations helper method"""
        operations_xml = """
    <aggregation function="SUM" column="amount" alias="total_spend"/>
    <aggregation function="COUNT" column="external_transaction_id" alias="count"/>
"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        aggregations = agent._parse_aggregations(operations_xml)

        assert len(aggregations) == 2
        assert aggregations[0].function == "SUM"
        assert aggregations[0].column == "amount"
        assert aggregations[0].alias == "total_spend"
        assert aggregations[1].function == "COUNT"

    def test_parse_filters_helper(self):
        """Test _parse_filters helper method"""
        operations_xml = """
    <filter column="category_code" operator="ILIKE"/>
    <filter column="amount" operator=">="/>
"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        filters = agent._parse_filters(operations_xml)

        assert len(filters) == 2
        assert filters[0].column == "category_code"
        assert filters[0].operator == "ILIKE"
        assert filters[1].column == "amount"
        assert filters[1].operator == ">="

    def test_parse_order_by_helper(self):
        """Test _parse_order_by helper method"""
        operations_xml = """
    <order_by column="total_spend" direction="DESC"/>
    <order_by column="transaction_booking_timestamp" direction="ASC"/>
"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        order_by = agent._parse_order_by(operations_xml)

        assert len(order_by) == 2
        assert order_by[0].column == "total_spend"
        assert order_by[0].direction == "DESC"
        assert order_by[1].direction == "ASC"

    def test_parse_join_helper(self):
        """Test _parse_join helper method"""
        operations_xml = """<join table="budgets" on="category_code"/>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        join = agent._parse_join(operations_xml)

        assert join is not None
        assert join.table == "budgets"
        assert join.on == "category_code"

    def test_parse_join_helper_no_join(self):
        """Test _parse_join returns None when no join present"""
        operations_xml = """<filter column="amount" operator=">"/>"""

        agent = QueryCharacteristicsExtractionAgent(llm_client=None)
        join = agent._parse_join(operations_xml)

        assert join is None


if __name__ == "__main__":
    print("\n🧪 Running QueryCharacteristicsExtractionAgent Unit Tests\n")
    pytest.main([__file__, "-v"])
