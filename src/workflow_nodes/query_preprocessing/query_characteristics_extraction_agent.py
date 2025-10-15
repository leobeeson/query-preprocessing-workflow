"""
Query Characteristics Extraction Agent

Analyzes natural language queries to determine:
- SQL feasibility
- Required SQL operations
- Advanced SQL features needed
- Missing requirements

Implements a dual-schema approach:
- LLM generates minimal XML (token efficient)
- Agent parses to complete JSON (predictable structure)
"""

import re
from typing import Type, List, Optional

from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
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
from src.parsers.xml_tag_parser import (
    get_xml_tag_content,
    parse_list_of_elements,
    parse_boolean_tag,
    parse_numeric_tag
)
from src.prompts.query_characteristics_extraction_prompt import get_instructions, get_task


class QueryCharacteristicsExtractionAgent(
    AgentNodeBase[QueryCharacteristicsInput, QueryCharacteristicsOutput]
):
    """
    Agent that analyzes query characteristics and determines SQL structure.

    Parses minimal XML from LLM and transforms it into a complete JSON structure
    with all defaults populated for predictable client consumption.
    """

    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.1,
            max_tokens=1500
        )
        self.system_prompt = get_instructions()

    def parse_response(self, llm_response: str) -> QueryCharacteristicsOutput:
        """
        Parse the minimal XML response from LLM into complete JSON structure.

        Handles two main branches:
        1. sql_feasible=true: Parse SQL operations and advanced features
        2. sql_feasible=false: Parse missing requirements

        All fields are populated with defaults for predictable structure.
        """
        # Extract top-level fields
        sql_feasible = parse_boolean_tag(llm_response, "sql_feasible")
        confidence = parse_numeric_tag(llm_response, "confidence", default=0.0)
        patterns = parse_list_of_elements(llm_response, "patterns", "pattern")
        explanation = get_xml_tag_content(llm_response, "explanation")

        # Branch based on feasibility
        if sql_feasible:
            sql_operations = self._parse_sql_operations(llm_response)
            advanced_sql = self._parse_advanced_sql(llm_response)
            missing_requirements = []
        else:
            sql_operations = None
            advanced_sql = None
            missing_requirements = self._parse_missing_requirements(llm_response)

        return QueryCharacteristicsOutput(
            sql_feasible=sql_feasible,
            confidence=confidence,
            patterns=patterns,
            sql_operations=sql_operations,
            advanced_sql=advanced_sql,
            missing_requirements=missing_requirements,
            explanation=explanation,
            raw_response=llm_response
        )

    def _parse_sql_operations(self, llm_response: str) -> SQLOperations:
        """
        Parse SQL operations from the <operations> container.

        Returns SQLOperations with all fields initialized to defaults,
        overriding with values found in XML.
        """
        operations_content = get_xml_tag_content(llm_response, "operations")

        # Parse all operation types
        aggregations = self._parse_aggregations(operations_content)
        filters = self._parse_filters(operations_content)
        group_by = parse_list_of_elements(operations_content, "operations", "group_by")
        order_by = self._parse_order_by(operations_content)

        # Parse limit
        limit_str = get_xml_tag_content(operations_content, "limit")
        limit = int(limit_str) if limit_str else None

        # Parse join
        joins = self._parse_join(operations_content)

        return SQLOperations(
            aggregations=aggregations,
            filters=filters,
            group_by=group_by,
            order_by=order_by,
            limit=limit,
            joins=joins
        )

    def _parse_advanced_sql(self, llm_response: str) -> AdvancedSQL:
        """
        Parse advanced SQL features from the <operations> container.

        Returns AdvancedSQL with all fields initialized to defaults,
        overriding with values found in XML.
        """
        operations_content = get_xml_tag_content(llm_response, "operations")

        # Parse CTE flags
        cte_required_content = get_xml_tag_content(operations_content, "requires_cte")
        cte_required = bool(cte_required_content)
        cte_purpose = get_xml_tag_content(operations_content, "cte_purpose") or None

        # Parse subquery flag
        subquery_content = get_xml_tag_content(operations_content, "requires_subquery")
        subqueries = bool(subquery_content)

        # Parse case statements
        case_statements = self._parse_case_statements(operations_content)

        # Parse set operations
        set_operations = get_xml_tag_content(operations_content, "set_operation") or None

        # Parse window functions
        window_functions = self._parse_window_functions(operations_content)

        return AdvancedSQL(
            cte_required=cte_required,
            cte_purpose=cte_purpose,
            window_functions=window_functions,
            case_statements=case_statements,
            set_operations=set_operations,
            subqueries=subqueries
        )

    def _parse_missing_requirements(self, llm_response: str) -> List[MissingRequirement]:
        """
        Parse missing requirements from nested structure.

        Structure:
        <missing_requirements>
          <missing_requirement>
            <type>...</type>
            <description>...</description>
            <severity>...</severity>
            <resolutions>
              <resolution>...</resolution>
              <resolution>...</resolution>
            </resolutions>
          </missing_requirement>
        </missing_requirements>
        """
        mr_container = get_xml_tag_content(llm_response, "missing_requirements")

        if not mr_container:
            return []

        # Find all missing_requirement blocks
        mr_blocks = re.findall(
            r'<missing_requirement>(.*?)</missing_requirement>',
            mr_container,
            re.DOTALL
        )

        requirements = []
        for block in mr_blocks:
            type_val = get_xml_tag_content(block, "type")
            description = get_xml_tag_content(block, "description")
            severity = get_xml_tag_content(block, "severity")

            # Extract resolutions from nested container
            resolutions_content = get_xml_tag_content(block, "resolutions")
            resolutions = re.findall(
                r'<resolution>(.*?)</resolution>',
                resolutions_content,
                re.DOTALL
            )
            resolutions = [r.strip() for r in resolutions]

            requirements.append(MissingRequirement(
                type=type_val,
                description=description,
                severity=severity,
                possible_resolutions=resolutions
            ))

        return requirements

    # ========================================================================
    # HELPER METHODS FOR PARSING SPECIFIC OPERATION TYPES
    # ========================================================================

    def _parse_aggregations(self, operations_xml: str) -> List[Aggregation]:
        """
        Parse aggregation elements with attributes.

        Pattern: <aggregation function="SUM" column="amount" alias="total"/>
        """
        pattern = r'<aggregation\s+function="([^"]+)"\s+column="([^"]+)"\s+alias="([^"]+)"\s*/>'
        matches = re.findall(pattern, operations_xml)

        return [
            Aggregation(function=func, column=col, alias=alias)
            for func, col, alias in matches
        ]

    def _parse_filters(self, operations_xml: str) -> List[Filter]:
        """
        Parse filter elements with attributes.

        Pattern: <filter column="category_code" operator="ILIKE"/>
        """
        pattern = r'<filter\s+column="([^"]+)"\s+operator="([^"]+)"\s*/>'
        matches = re.findall(pattern, operations_xml)

        return [
            Filter(column=col, operator=op)
            for col, op in matches
        ]

    def _parse_order_by(self, operations_xml: str) -> List[OrderBy]:
        """
        Parse order_by elements with attributes.

        Pattern: <order_by column="total_spend" direction="DESC"/>
        """
        pattern = r'<order_by\s+column="([^"]+)"\s+direction="([^"]+)"\s*/>'
        matches = re.findall(pattern, operations_xml)

        return [
            OrderBy(column=col, direction=direction)
            for col, direction in matches
        ]

    def _parse_join(self, operations_xml: str) -> Optional[Join]:
        """
        Parse join element with attributes.

        Pattern: <join table="budgets" on="category_code"/>
        Returns None if no join found.
        """
        pattern = r'<join\s+table="([^"]+)"\s+on="([^"]+)"\s*/>'
        match = re.search(pattern, operations_xml)

        if match:
            return Join(table=match.group(1), on=match.group(2))
        return None

    def _parse_case_statements(self, operations_xml: str) -> List[str]:
        """
        Parse case_statement elements with purpose attribute.

        Pattern: <case_statement purpose="Pivot years to columns"/>
        Returns list of purpose strings.
        """
        pattern = r'<case_statement\s+purpose="([^"]+)"\s*/>'
        matches = re.findall(pattern, operations_xml)
        return matches

    def _parse_window_functions(self, operations_xml: str) -> List[WindowFunction]:
        """
        Parse window_function elements with attributes.

        Pattern: <window_function type="ROW_NUMBER" partition_by="category" order_by="amount"/>
        Note: partition_by and order_by are optional attributes.
        """
        # Pattern handles optional attributes
        pattern = r'<window_function\s+type="([^"]+)"(?:\s+partition_by="([^"]*)")?(?:\s+order_by="([^"]*)")?\s*/>'
        matches = re.findall(pattern, operations_xml)

        window_funcs = []
        for match in matches:
            func_type, partition, order = match

            # Convert comma-separated strings to lists, handling empty strings
            partition_by = [partition] if partition else []
            order_by = [order] if order else []

            window_funcs.append(WindowFunction(
                function=func_type,
                partition_by=partition_by,
                order_by=order_by
            ))

        return window_funcs

    # ========================================================================
    # REQUIRED INTERFACE METHODS
    # ========================================================================

    def get_input_model(self) -> Type[QueryCharacteristicsInput]:
        """Return the Pydantic model class for the input"""
        return QueryCharacteristicsInput

    def get_output_model(self) -> Type[QueryCharacteristicsOutput]:
        """Return the Pydantic model class for the output"""
        return QueryCharacteristicsOutput

    def format_user_prompt(self, input_data: QueryCharacteristicsInput) -> str:
        """Format the input data into a user prompt for the LLM"""
        return get_task(input_data.query, input_data.processable_entities)
