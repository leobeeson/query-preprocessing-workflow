"""
Test cases for SentimentAnalysisAgent demonstrating semantic criteria evaluation.
"""

from evals.decorators import eval_case
from evals.field_validators import Exact, OneOf, Criteria
from src.workflow_nodes.scratchpad.sentiment_analysis_agent import SentimentAnalysisAgent
from src.models.scratchpad_models import TextInput, SentimentAnalysisOutput


# ========== Basic Field Validation Tests ==========

@eval_case(
    name="clear_positive",
    agent_class=SentimentAnalysisAgent,
    description="Clear positive sentiment with field validation",
    tags=["basic", "positive", "field-validation"]
)
def eval_clear_positive():
    return {
        "input": TextInput(text="I absolutely love this product! It's amazing and exceeded all my expectations."),
        "expected": SentimentAnalysisOutput(
            sentiment="positive",
            reasoning="The text expresses strong positive emotions with words like 'absolutely love', 'amazing', and 'exceeded all my expectations'."
        ),
        "field_validations": {
            "sentiment": Exact(value="positive")
        }
    }


@eval_case(
    name="clear_negative",
    agent_class=SentimentAnalysisAgent,
    description="Clear negative sentiment with field validation",
    tags=["basic", "negative", "field-validation"]
)
def eval_clear_negative():
    return {
        "input": TextInput(text="This is terrible. I'm extremely disappointed and frustrated with this service."),
        "expected": SentimentAnalysisOutput(
            sentiment="negative",
            reasoning="The text contains strong negative expressions like 'terrible', 'extremely disappointed', and 'frustrated'."
        ),
        "field_validations": {
            "sentiment": Exact(value="negative")
        }
    }


@eval_case(
    name="neutral_statement",
    agent_class=SentimentAnalysisAgent,
    description="Neutral factual statement",
    tags=["basic", "neutral", "field-validation"]
)
def eval_neutral_statement():
    return {
        "input": TextInput(text="The meeting is scheduled for 3 PM tomorrow in conference room B."),
        "expected": SentimentAnalysisOutput(
            sentiment="neutral",
            reasoning="This is a factual statement about scheduling with no emotional content."
        ),
        "field_validations": {
            "sentiment": Exact(value="neutral")
        }
    }


# ========== Semantic Criteria Tests (LLM-as-Judge) ==========

@eval_case(
    name="sarcasm_with_semantic",
    agent_class=SentimentAnalysisAgent,
    description="Sarcastic text requiring semantic evaluation of reasoning",
    tags=["advanced", "sarcasm", "semantic"]
)
def eval_sarcasm_with_semantic():
    return {
        "input": TextInput(text="Oh great, another software update that breaks everything. Just what I needed today!"),
        "expected": SentimentAnalysisOutput(
            sentiment="negative",
            reasoning="Sarcastic negative sentiment"
        ),
        "field_validations": {
            "sentiment": Exact(value="negative"),
            "reasoning": Criteria(criteria=[
                "The reasoning must identify the sarcastic tone of the text",
                "The reasoning must explain why this is negative despite words like 'great' and 'needed'",
                "The reasoning must reference specific phrases that indicate frustration"
            ])
        }
    }


@eval_case(
    name="mixed_sentiment_semantic",
    agent_class=SentimentAnalysisAgent,
    description="Mixed sentiment requiring nuanced reasoning",
    tags=["advanced", "mixed", "semantic"]
)
def eval_mixed_sentiment_semantic():
    return {
        "input": TextInput(text="The food was excellent but the service was painfully slow and the staff seemed uninterested."),
        "expected": SentimentAnalysisOutput(
            sentiment="negative",
            reasoning="Mixed sentiment with negative overall"
        ),
        "field_validations": {
            "sentiment": OneOf(values=["negative", "neutral"]),
            "reasoning": Criteria(criteria=[
                "The reasoning must acknowledge both positive and negative aspects",
                "The reasoning must explain how the overall sentiment was determined",
                "The reasoning must cite specific positive elements (food) and negative elements (service, staff)"
            ])
        }
    }


@eval_case(
    name="subtle_positive_semantic",
    agent_class=SentimentAnalysisAgent,
    description="Subtle positive sentiment with semantic evaluation",
    tags=["advanced", "positive", "semantic"]
)
def eval_subtle_positive_semantic():
    return {
        "input": TextInput(text="I wasn't sure at first, but this has really grown on me. I find myself using it every day now."),
        "expected": SentimentAnalysisOutput(
            sentiment="positive",
            reasoning="Positive progression over time"
        ),
        "field_validations": {
            "sentiment": Exact(value="positive"),
            "reasoning": Criteria(criteria=[
                "The reasoning must identify the progression from uncertainty to appreciation",
                "The reasoning must explain why the overall sentiment is positive despite initial doubt",
                "The reasoning must reference the key indicator 'using it every day'"
            ])
        }
    }


# ========== Field Validation with Complex Cases ==========

@eval_case(
    name="emotional_positive_field",
    agent_class=SentimentAnalysisAgent,
    description="Emotional text with field validation for sentiment",
    tags=["field", "positive", "emotional"]
)
def eval_emotional_positive_field():
    return {
        "input": TextInput(text="I can't stop smiling! This news has made my entire week. I'm over the moon!"),
        "expected": SentimentAnalysisOutput(
            sentiment="positive",
            reasoning="Extremely positive emotions expressed"
        ),
        "field_validations": {
            "sentiment": Exact(value="positive")
        }
    }


@eval_case(
    name="professional_critique_semantic",
    agent_class=SentimentAnalysisAgent,
    description="Professional critique with semantic validation of reasoning",
    tags=["semantic", "negative", "professional"]
)
def eval_professional_critique_semantic():
    return {
        "input": TextInput(text="While the concept shows promise, the execution falls short in several critical areas, particularly in terms of scalability and performance optimization."),
        "expected": SentimentAnalysisOutput(
            sentiment="negative",
            reasoning="Professional critique with negative assessment"
        ),
        "field_validations": {
            "sentiment": OneOf(values=["negative", "neutral"]),
            "reasoning": Criteria(criteria=[
                "The reasoning must identify the professional and measured tone",
                "The reasoning must explain the balance between acknowledging promise and identifying shortcomings",
                "The reasoning must note specific criticisms mentioned (scalability, performance)"
            ])
        }
    }


@eval_case(
    name="customer_feedback_semantic",
    agent_class=SentimentAnalysisAgent,
    description="Customer feedback with semantic reasoning validation",
    tags=["semantic", "feedback", "detailed"]
)
def eval_customer_feedback_semantic():
    return {
        "input": TextInput(text="The product quality is outstanding and worth every penny, though I wish the shipping had been faster."),
        "expected": SentimentAnalysisOutput(
            sentiment="positive",
            reasoning="Positive feedback with minor complaint"
        ),
        "field_validations": {
            "sentiment": Exact(value="positive"),
            "reasoning": Criteria(criteria=[
                "The reasoning must identify that positive aspects outweigh the negative",
                "The reasoning must mention both the compliment about quality and the shipping complaint",
                "The reasoning must explain why the overall sentiment is still positive"
            ])
        }
    }


# ========== Edge Cases ==========

@eval_case(
    name="empty_text_edge",
    agent_class=SentimentAnalysisAgent,
    description="Edge case with empty or minimal text",
    tags=["edge", "minimal", "field"]
)
def eval_empty_text_edge():
    return {
        "input": TextInput(text="..."),
        "expected": SentimentAnalysisOutput(
            sentiment="neutral",
            reasoning="No meaningful content to analyze"
        ),
        "field_validations": {
            "sentiment": Exact(value="neutral")
        }
    }


@eval_case(
    name="contradiction_semantic",
    agent_class=SentimentAnalysisAgent,
    description="Self-contradicting statement",
    tags=["edge", "contradiction", "semantic"]
)
def eval_contradiction_semantic():
    return {
        "input": TextInput(text="I love how much I hate this."),
        "expected": SentimentAnalysisOutput(
            sentiment="negative",
            reasoning="Contradictory statement"
        ),
        "field_validations": {
            "sentiment": OneOf(values=["negative", "neutral", "positive"]),  # Any could be valid
            "reasoning": Criteria(criteria=[
                "The reasoning must identify the contradictory nature of the statement",
                "The reasoning must explain the challenge in determining sentiment",
                "The reasoning must provide justification for the chosen classification"
            ])
        }
    }


# ========== More Field Validation Tests ==========

@eval_case(
    name="ambiguous_sentiment_field",
    agent_class=SentimentAnalysisAgent,
    description="Ambiguous text with flexible field validation",
    tags=["field", "ambiguous"]
)
def eval_ambiguous_sentiment_field():
    return {
        "input": TextInput(text="The meeting was... interesting. I'm not sure what to make of it."),
        "expected": SentimentAnalysisOutput(
            sentiment="neutral",
            reasoning="Ambiguous sentiment"
        ),
        "field_validations": {
            "sentiment": OneOf(values=["neutral", "negative"])
        }
    }


# ========== Testing Reasoning Quality with Semantic Criteria ==========

@eval_case(
    name="reasoning_quality_test",
    agent_class=SentimentAnalysisAgent,
    description="Focus on reasoning quality rather than sentiment accuracy",
    tags=["reasoning", "quality", "semantic"]
)
def eval_reasoning_quality():
    return {
        "input": TextInput(text="The new policy changes are interesting. Some aspects will help efficiency, but others might create new challenges."),
        "expected": SentimentAnalysisOutput(
            sentiment="neutral",
            reasoning="Balanced view of policy changes"
        ),
        "field_validations": {
            "sentiment": OneOf(values=["neutral", "positive"]),
            "reasoning": Criteria(criteria=[
                "The reasoning must demonstrate analytical thinking",
                "The reasoning must avoid oversimplification",
                "The reasoning must consider multiple perspectives",
                "The reasoning must be coherent and well-structured"
            ])
        }
    }


@eval_case(
    name="technical_sentiment_semantic",
    agent_class=SentimentAnalysisAgent,
    description="Technical text with semantic validation of understanding",
    tags=["technical", "semantic"]
)
def eval_technical_sentiment_semantic():
    return {
        "input": TextInput(text="The API response time has degraded from 50ms to 500ms after the latest deployment."),
        "expected": SentimentAnalysisOutput(
            sentiment="negative",
            reasoning="Performance degradation is a negative issue"
        ),
        "field_validations": {
            "sentiment": Exact(value="negative"),
            "reasoning": Criteria(criteria=[
                "The reasoning must recognize that degraded performance is negative",
                "The reasoning must reference the specific metrics (50ms to 500ms)",
                "The reasoning must explain why this technical change represents a negative development"
            ])
        }
    }