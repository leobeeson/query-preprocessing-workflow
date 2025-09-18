"""
Simple sentiment analysis agent for testing semantic criteria evaluation.
"""

from typing import Type
from src.core_nodes.agent_node_base import AgentNodeBase
from src.clients.llm_clients.llm_client_interface import LLMClientInterface
from src.models.scratchpad_models import TextInput, SentimentAnalysisOutput


class SentimentAnalysisAgent(AgentNodeBase[TextInput, SentimentAnalysisOutput]):
    """
    A simple agent for sentiment analysis to test semantic evaluation.
    Uses inline prompts for simplicity.
    """

    def __init__(self, llm_client: LLMClientInterface):
        super().__init__(
            llm_client=llm_client,
            temperature=0.3,
            max_tokens=200
        )
        # Inline system prompt
        self.system_prompt = """You are a sentiment analysis expert. Your task is to analyze the sentiment of text and provide clear reasoning.

For each text, you must:
1. Classify the sentiment as: positive, negative, or neutral
2. Provide clear reasoning that explains your classification
3. Reference specific words or phrases that support your classification

Output format:
<sentiment>[positive|negative|neutral]</sentiment>
<reasoning>Your explanation here</reasoning>"""

    def parse_response(self, llm_response: str) -> SentimentAnalysisOutput:
        """Parse the LLM response to extract sentiment and reasoning."""
        # Extract sentiment
        sentiment = "neutral"  # default
        if "<sentiment>" in llm_response and "</sentiment>" in llm_response:
            start = llm_response.find("<sentiment>") + len("<sentiment>")
            end = llm_response.find("</sentiment>")
            sentiment = llm_response[start:end].strip().lower()

        # Extract reasoning
        reasoning = "No reasoning provided"  # default
        if "<reasoning>" in llm_response and "</reasoning>" in llm_response:
            start = llm_response.find("<reasoning>") + len("<reasoning>")
            end = llm_response.find("</reasoning>")
            reasoning = llm_response[start:end].strip()

        return SentimentAnalysisOutput(
            sentiment=sentiment,
            reasoning=reasoning,
            raw_response=llm_response
        )

    def get_input_model(self) -> Type[TextInput]:
        """Return the input model class."""
        return TextInput

    def get_output_model(self) -> Type[SentimentAnalysisOutput]:
        """Return the output model class."""
        return SentimentAnalysisOutput

    def format_user_prompt(self, input_data: TextInput) -> str:
        """Format the input into a user prompt."""
        return f"Analyze the sentiment of the following text:\n\n{input_data.text}"