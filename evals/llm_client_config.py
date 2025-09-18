"""
Centralized LLM client configuration for evaluation tests.

This module provides a single place to configure the LLM client
used across all evaluation tests.
"""

import os
from typing import Optional
from dotenv import load_dotenv

from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.clients.llm_clients.anthropic_llm_client import AnthropicLLMClient


# Load environment variables
load_dotenv()


def get_llm_client() -> Optional[LLMClientInterface]:
    """
    Get configured LLM client for evaluations.

    This is the single place to configure which LLM client to use.
    When moving to another project, only this function needs to be modified.

    Returns:
        Configured LLM client or None if not configured
    """
    # Get API key from environment
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("Please set it with: export ANTHROPIC_API_KEY='your-api-key'")
        print("Or add it to your .env file")
        return None

    # Return configured client
    # When integrating with another project, replace this with your LLM client
    return AnthropicLLMClient(api_key=api_key)


def get_llm_client_or_exit() -> LLMClientInterface:
    """
    Get configured LLM client or exit with error message.

    Returns:
        Configured LLM client

    Raises:
        SystemExit: If LLM client is not configured
    """
    client = get_llm_client()
    if not client:
        import sys
        sys.exit(1)
    return client