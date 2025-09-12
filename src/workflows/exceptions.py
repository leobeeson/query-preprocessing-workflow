"""
Custom exceptions for query preprocessing workflow
"""

from typing import Optional, List


class WorkflowError(Exception):
    """Base exception for workflow errors"""
    pass


class InsecureQueryError(WorkflowError):
    """Raised when query fails security validation"""
    def __init__(self, message: str = "Query failed security validation", justification: Optional[str] = None):
        self.justification = justification
        if justification:
            message = f"{message}: {justification}"
        super().__init__(message)


class InvalidQueryError(WorkflowError):
    """Raised when query fails intent validation"""
    def __init__(self, message: str = "Query is invalid for banking domain", justification: Optional[str] = None):
        self.justification = justification
        if justification:
            message = f"{message}: {justification}"
        super().__init__(message)


class UnprocessableEntityError(WorkflowError):
    """Raised when query contains critical unprocessable entities or no processable entities"""
    def __init__(self, message: str = "Query contains unprocessable entities", entities: Optional[List] = None):
        self.entities = entities or []
        if entities:
            critical_entities = [e for e in entities if hasattr(e, 'critical') and e.critical]
            if critical_entities:
                entity_types = [e.type for e in critical_entities]
                message = f"{message}: {', '.join(entity_types)}"
        super().__init__(message)


class NoProcessableEntitiesError(UnprocessableEntityError):
    """Raised when no processable entities are found"""
    def __init__(self):
        super().__init__("No processable entities found in query")