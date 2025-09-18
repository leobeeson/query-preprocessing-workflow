"""
Registry for managing evaluation cases.
"""

import importlib
import inspect
import os
from pathlib import Path
from typing import Type, List, Dict, Any, Optional, Callable

from pydantic import BaseModel
from evals.core import EvalCase
from evals.decorators import get_eval_case, get_registry


class EvalRegistry:
    """
    Registry for managing and discovering evaluation cases.
    """

    def __init__(self, agent_class: Type, input_type: Type[BaseModel], output_type: Type[BaseModel]):
        """
        Initialize registry for a specific agent.

        Args:
            agent_class: The agent class to find cases for
            input_type: Input type for the agent
            output_type: Output type for the agent
        """
        self.agent_class = agent_class
        self.agent_name = agent_class.__name__
        self.input_type = input_type
        self.output_type = output_type
        self._cases: Dict[str, EvalCase] = {}
        self._functions: Dict[str, Callable] = {}

    @classmethod
    def for_agent(
        cls,
        agent_class: Type,
        input_type: Type[BaseModel],
        output_type: Type[BaseModel]
    ) -> 'EvalRegistry':
        """
        Create a registry for a specific agent and load its cases.

        Args:
            agent_class: The agent class
            input_type: Input type for the agent
            output_type: Output type for the agent

        Returns:
            EvalRegistry with loaded cases
        """
        registry = cls(agent_class, input_type, output_type)
        registry.load_cases()
        return registry

    def load_cases(self):
        """Load all evaluation cases for this agent from the decorator registry."""
        global_registry = get_registry()

        # Get cases for this specific agent
        if self.agent_name in global_registry:
            agent_cases = global_registry[self.agent_name]
            for name, func in agent_cases.items():
                self._functions[name] = func
                # Convert to EvalCase
                eval_case = get_eval_case(func, self.input_type, self.output_type)
                self._cases[name] = eval_case

    def auto_discover(self, path: Optional[Path] = None):
        """
        Auto-discover evaluation cases from files.

        Args:
            path: Path to search for evaluation files (defaults to evals/cases/)
        """
        if path is None:
            # Default to evals/cases/ directory
            path = Path(__file__).parent / "cases"

        if not path.exists():
            return

        # Find all Python files in the directory
        for file_path in path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue  # Skip private files

            # Import the module
            module_name = file_path.stem
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # The import will trigger decorator registration
                # Now check if any new cases were added
                self.load_cases()

    def get_case(self, name: str) -> Optional[EvalCase]:
        """Get a specific evaluation case by name."""
        return self._cases.get(name)

    def get_cases(
        self,
        names: Optional[List[str]] = None,
        tags: Optional[List[str]] = None,
        priority_min: Optional[int] = None
    ) -> List[EvalCase]:
        """
        Get evaluation cases with optional filtering.

        Args:
            names: Specific case names to get
            tags: Filter by tags (cases must have at least one matching tag)
            priority_min: Minimum priority level

        Returns:
            List of matching evaluation cases
        """
        cases = []

        for name, case in self._cases.items():
            # Filter by name
            if names and name not in names:
                continue

            # Get metadata from function
            func = self._functions.get(name)
            if not func:
                continue

            metadata = getattr(func, "eval_metadata", {})

            # Filter by tags
            if tags:
                case_tags = metadata.get("tags", [])
                if not any(tag in case_tags for tag in tags):
                    continue

            # Filter by priority
            if priority_min is not None:
                priority = metadata.get("priority", 0)
                if priority < priority_min:
                    continue

            cases.append(case)

        return cases

    def get_all_cases(self) -> List[EvalCase]:
        """Get all evaluation cases."""
        return list(self._cases.values())

    def get_cases_by_tag(self, tag: str) -> List[EvalCase]:
        """Get all cases with a specific tag."""
        return self.get_cases(tags=[tag])

    def list_tags(self) -> List[str]:
        """List all unique tags used in evaluation cases."""
        tags = set()
        for func in self._functions.values():
            metadata = getattr(func, "eval_metadata", {})
            tags.update(metadata.get("tags", []))
        return sorted(list(tags))

    def list_case_names(self) -> List[str]:
        """List all case names."""
        return sorted(list(self._cases.keys()))

    def summary(self) -> Dict[str, Any]:
        """Get a summary of the registry."""
        return {
            "agent": self.agent_name,
            "total_cases": len(self._cases),
            "case_names": self.list_case_names(),
            "tags": self.list_tags()
        }