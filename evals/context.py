"""
Simple conversation context for agent nodes.
"""

from typing import Any, Dict, Optional


class ConversationContext:
    """
    Minimal conversation context for testing agent nodes.
    
    This provides the interface that agent nodes expect without
    requiring complex dependencies like DynamoDB or S3.
    """
    
    def __init__(
        self,
        query: str,
        previous_node_output: Optional[Dict[str, Any]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the conversation context.
        
        Args:
            query: The user query to process
            previous_node_output: Output from the previous node in the workflow
            metadata: Optional metadata for the conversation
        """
        self.query: str = query
        self.working_query: str = query  # Some nodes may modify this
        self.previous_node_output: Dict[str, Any] = previous_node_output or {}
        self.metadata: Dict[str, Any] = metadata or {}
        self.workflow_nodes: Dict[str, Any] = {}
        self.workflow_path: list[str] = []
    
    
    def add_workflow_step(self, node_name: str) -> None:
        """
        Track workflow step execution.
        
        Args:
            node_name: Name of the node being executed
        """
        self.workflow_path.append(node_name)
    
    
    def update_workflow_node(self, node_name: str, **kwargs: Any) -> None:
        """
        Store node results in workflow tracking.
        
        Args:
            node_name: Name of the node
            **kwargs: Node output data to store
        """
        if node_name not in self.workflow_nodes:
            self.workflow_nodes[node_name] = {}
        self.workflow_nodes[node_name].update(kwargs)
    
    
    def get_node_output(self, node_name: str) -> Dict[str, Any]:
        """
        Get the output from a specific node.
        
        Args:
            node_name: Name of the node
            
        Returns:
            Node output data or empty dict if not found
        """
        return self.workflow_nodes.get(node_name, {})