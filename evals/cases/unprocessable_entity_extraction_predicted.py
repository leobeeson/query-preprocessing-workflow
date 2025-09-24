"""
Evaluation cases for UnprocessableEntityExtractionAgent from predicted user intents.
Generated from predicted_user_intent_1.csv - mirroring processable_entity_extraction_predicted.py
"""

from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact, Substring
from src.workflow_nodes.query_preprocessing.unprocessable_entity_extraction_agent import UnprocessableEntityExtractionAgent
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import UnprocessableEntityExtractionOutput, UnprocessableEntity as Entity


# ========== Predicted User Intent Cases (260) ==========
@eval_case(
    name="predicted_intent_001",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I receive any cashbacks or refunds from groceries or Amazon in 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_001():
    return {
        "input": QueryInput(query="Did I receive any cashbacks or refunds from groceries or Amazon in 2023 and 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_002",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was the day in 2024 when my combined spending on groceries and Amazon was the highest?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_002():
    return {
        "input": QueryInput(query="What was the day in 2024 when my combined spending on groceries and Amazon was the highest?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_003",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which restaurants did I spend $150 on dining out last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_003():
    return {
        "input": QueryInput(query="Which restaurants did I spend $150 on dining out last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_004",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my total spending on groceries and dining out in the last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_004():
    return {
        "input": QueryInput(query="What was my total spending on groceries and dining out in the last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_005",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending in the last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_005():
    return {
        "input": QueryInput(query="What is my total spending in the last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_006",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my payments to Amzn past 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_006():
    return {
        "input": QueryInput(query="my payments to Amzn past 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_007",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Where did I spend cash in the Entertainment category last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_007():
    return {
        "input": QueryInput(query="Where did I spend cash in the Entertainment category last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="payment_method", value="cash", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Exact(value="cash"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_008",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Was RetailMart the store where I spent the most last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_008():
    return {
        "input": QueryInput(query="Was RetailMart the store where I spent the most last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_009",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times did I eat out last month and at which place did I eat out the most?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_009():
    return {
        "input": QueryInput(query="How many times did I eat out last month and at which place did I eat out the most?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_010",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much of my Dining and Groceries spending last month were online payments?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_010():
    return {
        "input": QueryInput(query="How much of my Dining and Groceries spending last month were online payments?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="transaction_channel", value="online", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Exact(value="online"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_011",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times did I spend more than 100 dollars at Starbucks in 2022 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_011():
    return {
        "input": QueryInput(query="How many times did I spend more than 100 dollars at Starbucks in 2022 2023 and 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_012",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When was my most recent visit to Starbucks?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_012():
    return {
        "input": QueryInput(query="When was my most recent visit to Starbucks?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_013",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I spend at Trader Joes in 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_013():
    return {
        "input": QueryInput(query="Did I spend at Trader Joes in 2022?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_014",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I exceed my grocery budget last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_014():
    return {
        "input": QueryInput(query="Did I exceed my grocery budget last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_015",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I exceed my grocery budget in the last year and how many times did that happen?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_015():
    return {
        "input": QueryInput(query="Did I exceed my grocery budget in the last year and how many times did that happen?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_016",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which hotel did I stay at in December 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_016():
    return {
        "input": QueryInput(query="Which hotel did I stay at in December 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_017",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which specific utility did I spend the most on in 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_017():
    return {
        "input": QueryInput(query="Which specific utility did I spend the most on in 2023 and 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_018",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did I start my tennis lessons last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_018():
    return {
        "input": QueryInput(query="When did I start my tennis lessons last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="tennis lessons", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="tennis lessons"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_019",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend in February and March this year compared to last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_019():
    return {
        "input": QueryInput(query="How much did I spend in February and March this year compared to last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_020",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I spend at Trader Joes in 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_020():
    return {
        "input": QueryInput(query="Did I spend at Trader Joes in 2022?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_021",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending at McDonald's last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_021():
    return {
        "input": QueryInput(query="What is my total spending at McDonald's last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_022",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I pay my bills this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_022():
    return {
        "input": QueryInput(query="Did I pay my bills this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_023",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my month on month spending at Walmart Whole Foods and Trader Joes for groceries in 2023",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_023():
    return {
        "input": QueryInput(query="What is my month on month spending at Walmart Whole Foods and Trader Joes for groceries in 2023"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_024",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I spent on train and bus this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_024():
    return {
        "input": QueryInput(query="How much have I spent on train and bus this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_025",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which of my direct debit merchants Netflix Spotify Amazon or Disney Plus has the highest subscription...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_025():
    return {
        "input": QueryInput(query="Which of my direct debit merchants Netflix Spotify Amazon or Disney Plus has the highest subscription..."),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_026",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did I change my Netflix direct debit plan from 20 dollars to 37 dollars?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_026():
    return {
        "input": QueryInput(query="When did I change my Netflix direct debit plan from 20 dollars to 37 dollars?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_027",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which airlines have I flown with in the past year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_027():
    return {
        "input": QueryInput(query="Which airlines have I flown with in the past year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_028",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was the total amount of direct debits from my account in February 2025?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_028():
    return {
        "input": QueryInput(query="What was the total amount of direct debits from my account in February 2025?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_029",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend on Entertainment in August 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_029():
    return {
        "input": QueryInput(query="How much did I spend on Entertainment in August 2023?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_030",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total amount spent at Amazon in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_030():
    return {
        "input": QueryInput(query="What is my total amount spent at Amazon in the last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_031",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount I received from my savings account each month in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_031():
    return {
        "input": QueryInput(query="What is the total amount I received from my savings account each month in 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="savings account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_032",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What are my recurring payments over 50 dollars in the past three months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_032():
    return {
        "input": QueryInput(query="What are my recurring payments over 50 dollars in the past three months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_033",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much of my grocery budget is left for this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_033():
    return {
        "input": QueryInput(query="How much of my grocery budget is left for this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_034",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did I receive a refund from Tesco and what was the amount?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_034():
    return {
        "input": QueryInput(query="When did I receive a refund from Tesco and what was the amount?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_035",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my average amount spent per transaction in September",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_035():
    return {
        "input": QueryInput(query="What is my average amount spent per transaction in September"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_036",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my biggest outgoing transaction in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_036():
    return {
        "input": QueryInput(query="What is my biggest outgoing transaction in 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_037",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my spending at Burger King this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_037():
    return {
        "input": QueryInput(query="What is my spending at Burger King this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_038",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which subscription between TV Sky and Netflix had more frequent payments over the last 2 years",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_038():
    return {
        "input": QueryInput(query="Which subscription between TV Sky and Netflix had more frequent payments over the last 2 years"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_039",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times did I order from Zomato in July?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_039():
    return {
        "input": QueryInput(query="How many times did I order from Zomato in July?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_040",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my account balance after sending $200 to Phil on 15th October?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_040():
    return {
        "input": QueryInput(query="What was my account balance after sending $200 to Phil on 15th October?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="Phil", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="Phil"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_041",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which month did I receive the lowest rent income this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_041():
    return {
        "input": QueryInput(query="Which month did I receive the lowest rent income this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_042",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which month in the past year did I transfer the maximum amount to my savings account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_042():
    return {
        "input": QueryInput(query="Which month in the past year did I transfer the maximum amount to my savings account?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="savings account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_043",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many transactions contributed to the 450 dollars spent at Cliveland Cafe in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_043():
    return {
        "input": QueryInput(query="How many transactions contributed to the 450 dollars spent at Cliveland Cafe in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_044",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Why is there a transaction for Cliveland Cafe in my dining expenses if I never went there?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_044():
    return {
        "input": QueryInput(query="Why is there a transaction for Cliveland Cafe in my dining expenses if I never went there?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_045",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you review my spending from last weekend and provide a breakdown to verify the total amount spent?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_045():
    return {
        "input": QueryInput(query="Can you review my spending from last weekend and provide a breakdown to verify the total amount spent?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_046",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you recheck how much I spent last weekend?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_046():
    return {
        "input": QueryInput(query="Can you recheck how much I spent last weekend?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_047",
    agent_class=UnprocessableEntityExtractionAgent,
    description="can you help me with my bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_047():
    return {
        "input": QueryInput(query="can you help me with my bills?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_048",
    agent_class=UnprocessableEntityExtractionAgent,
    description="how do I pay my electricity bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_048():
    return {
        "input": QueryInput(query="how do I pay my electricity bills?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_049",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you find any payments made to Avis car hire in the last month, the last 6 months, and in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_049():
    return {
        "input": QueryInput(query="Can you find any payments made to Avis car hire in the last month, the last 6 months, and in 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_050",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my average amount spent per store for food during Xmas 2022 at Walmart Whole Foods and Trader...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_050():
    return {
        "input": QueryInput(query="What was my average amount spent per store for food during Xmas 2022 at Walmart Whole Foods and Trader..."),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_051",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which months did I have round up savings this year till now?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_051():
    return {
        "input": QueryInput(query="Which months did I have round up savings this year till now?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_052",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much of my grocery budget is left for this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_052():
    return {
        "input": QueryInput(query="How much of my grocery budget is left for this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_053",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend in total in the first quarter of the year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_053():
    return {
        "input": QueryInput(query="How much did I spend in total in the first quarter of the year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_054",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Were there any refunds among my biggest transactions last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_054():
    return {
        "input": QueryInput(query="Were there any refunds among my biggest transactions last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_055",
    agent_class=UnprocessableEntityExtractionAgent,
    description="In which category or at which merchant did I spend the most in March June September October and December...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_055():
    return {
        "input": QueryInput(query="In which category or at which merchant did I spend the most in March June September October and December..."),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_056",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Who were my most frequently used travel vendors in July?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_056():
    return {
        "input": QueryInput(query="Who were my most frequently used travel vendors in July?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_057",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times did I dine out each month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_057():
    return {
        "input": QueryInput(query="How many times did I dine out each month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_058",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the month over month growth rate of my spending in each merchant subcategory",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_058():
    return {
        "input": QueryInput(query="What is the month over month growth rate of my spending in each merchant subcategory"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_059",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Compare my average daily spending in each expense area to the average daily spending in the previous month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_059():
    return {
        "input": QueryInput(query="Compare my average daily spending in each expense area to the average daily spending in the previous month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_060",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What were my bottom 3 spending categories last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_060():
    return {
        "input": QueryInput(query="What were my bottom 3 spending categories last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_061",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount I spent at Amazon and Starbucks in the last six months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_061():
    return {
        "input": QueryInput(query="What is the total amount I spent at Amazon and Starbucks in the last six months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_062",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times did I visit Starbucks in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_062():
    return {
        "input": QueryInput(query="How many times did I visit Starbucks in 2023?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_063",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many transactions did I make on Amazon and eBay in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_063():
    return {
        "input": QueryInput(query="How many transactions did I make on Amazon and eBay in 2023?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_064",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How does my spending on Amazon in 2023 compare to my spending on Amazon in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_064():
    return {
        "input": QueryInput(query="How does my spending on Amazon in 2023 compare to my spending on Amazon in 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_065",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending on sports this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_065():
    return {
        "input": QueryInput(query="What is my total spending on sports this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_066",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which airline was my second highest in terms of spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_066():
    return {
        "input": QueryInput(query="Which airline was my second highest in terms of spending in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_067",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend on fuel in 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_067():
    return {
        "input": QueryInput(query="How much did I spend on fuel in 2022?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_068",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times was I overdrawn in March?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_068():
    return {
        "input": QueryInput(query="How many times was I overdrawn in March?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_069",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I receive any refunds from McDonalds last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_069():
    return {
        "input": QueryInput(query="Did I receive any refunds from McDonalds last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_070",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total water bill for this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_070():
    return {
        "input": QueryInput(query="What is my total water bill for this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_071",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I pay my bills this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_071():
    return {
        "input": QueryInput(query="Did I pay my bills this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_072",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the highest amount I spent on subscriptions in any month this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_072():
    return {
        "input": QueryInput(query="What is the highest amount I spent on subscriptions in any month this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_073",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you list all the merchants I purchased from for groceries in 2023",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_073():
    return {
        "input": QueryInput(query="Can you list all the merchants I purchased from for groceries in 2023"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_074",
    agent_class=UnprocessableEntityExtractionAgent,
    description="List the stores where I purchased groceries in 2023",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_074():
    return {
        "input": QueryInput(query="List the stores where I purchased groceries in 2023"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_075",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my total earning on rent?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_075():
    return {
        "input": QueryInput(query="my total earning on rent?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_076",
    agent_class=UnprocessableEntityExtractionAgent,
    description="how much I spend in rent?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_076():
    return {
        "input": QueryInput(query="how much I spend in rent?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_077",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my total medical bills at drugstores",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_077():
    return {
        "input": QueryInput(query="my total medical bills at drugstores"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_078",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my total medical bills at hospital",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_078():
    return {
        "input": QueryInput(query="my total medical bills at hospital"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_079",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What refunds did I receive last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_079():
    return {
        "input": QueryInput(query="What refunds did I receive last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_080",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What items did I purchase in my $300 transaction at Costco last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_080():
    return {
        "input": QueryInput(query="What items did I purchase in my $300 transaction at Costco last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="items", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Exact(value="items"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_081",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did I last pay my Costco membership fee",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_081():
    return {
        "input": QueryInput(query="When did I last pay my Costco membership fee"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="membership fee", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="membership fee"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_082",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did I make my first mortgage payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_082():
    return {
        "input": QueryInput(query="When did I make my first mortgage payment?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_083",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount I have paid towards my mortgage payments?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_083():
    return {
        "input": QueryInput(query="What is the total amount I have paid towards my mortgage payments?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_084",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When is my next car insurance payment due to Geico?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_084():
    return {
        "input": QueryInput(query="When is my next car insurance payment due to Geico?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_085",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount received from the DWP in the last 6 months including both fortnightly Wednesday...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_085():
    return {
        "input": QueryInput(query="What is the total amount received from the DWP in the last 6 months including both fortnightly Wednesday..."),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_086",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How does my total savings in both my savings and checking accounts this year compare to last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_086():
    return {
        "input": QueryInput(query="How does my total savings in both my savings and checking accounts this year compare to last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings", critical=True),
                Entity(type="account", value="checking accounts", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Exact(value="savings"), "critical": Exact(value=True)},
                {"type": Exact(value="account"), "value": Substring(value="checking accounts"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_087",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my cloth purchases",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_087():
    return {
        "input": QueryInput(query="my cloth purchases"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_088",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my earning in last 6 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_088():
    return {
        "input": QueryInput(query="my earning in last 6 months"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_089",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did I receive my Chb?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_089():
    return {
        "input": QueryInput(query="When did I receive my Chb?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_090",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my total spending at Amazon last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_090():
    return {
        "input": QueryInput(query="What was my total spending at Amazon last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_091",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much do I get in child benefits?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_091():
    return {
        "input": QueryInput(query="How much do I get in child benefits?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_092",
    agent_class=UnprocessableEntityExtractionAgent,
    description="show the bills",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_092():
    return {
        "input": QueryInput(query="show the bills"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_093",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I send that money to X?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_093():
    return {
        "input": QueryInput(query="Did I send that money to X?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="X", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="X"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_094",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did John send me the 200 dollars they owed me?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_094():
    return {
        "input": QueryInput(query="When did John send me the 200 dollars they owed me?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="John", critical=True),
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="John"), "critical": Exact(value=True)},
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_095",
    agent_class=UnprocessableEntityExtractionAgent,
    description="did John pay me, if yes , how much",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_095():
    return {
        "input": QueryInput(query="did John pay me, if yes , how much"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="John", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="John"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_096",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my total electricity spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_096():
    return {
        "input": QueryInput(query="What was my total electricity spending in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_097",
    agent_class=UnprocessableEntityExtractionAgent,
    description="how much refund did Adibas pay me",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_097():
    return {
        "input": QueryInput(query="how much refund did Adibas pay me"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_098",
    agent_class=UnprocessableEntityExtractionAgent,
    description="how much money john helped me with",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_098():
    return {
        "input": QueryInput(query="how much money john helped me with"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="john", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="john"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_099",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the smallest transaction I have made to John since August?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_099():
    return {
        "input": QueryInput(query="What is the smallest transaction I have made to John since August?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="John", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="John"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_100",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my average monthly spending on groceries in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_100():
    return {
        "input": QueryInput(query="What is my average monthly spending on groceries in 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_101",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total balance in my savings account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_101():
    return {
        "input": QueryInput(query="What is my total balance in my savings account?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="savings account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_102",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my total depoists last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_102():
    return {
        "input": QueryInput(query="my total depoists last year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_103",
    agent_class=UnprocessableEntityExtractionAgent,
    description="what cheque depoists I made?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_103():
    return {
        "input": QueryInput(query="what cheque depoists I made?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="payment_method", value="cheque", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Exact(value="cheque"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_104",
    agent_class=UnprocessableEntityExtractionAgent,
    description="did I pay my tennis classes fee last month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_104():
    return {
        "input": QueryInput(query="did I pay my tennis classes fee last month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="tennis classes", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="tennis classes"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_105",
    agent_class=UnprocessableEntityExtractionAgent,
    description="show my spend at swimming session in last 6 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_105():
    return {
        "input": QueryInput(query="show my spend at swimming session in last 6 months"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="swimming session", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="swimming session"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_106",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What days am I most likely to order a takeaway?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_106():
    return {
        "input": QueryInput(query="What days am I most likely to order a takeaway?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_107",
    agent_class=UnprocessableEntityExtractionAgent,
    description="store I order most of my takeaways?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_107():
    return {
        "input": QueryInput(query="store I order most of my takeaways?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_108",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which stores did I order takeaway from on Mondays?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_108():
    return {
        "input": QueryInput(query="Which stores did I order takeaway from on Mondays?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_109",
    agent_class=UnprocessableEntityExtractionAgent,
    description="show my top 3 recurring spending places in a month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_109():
    return {
        "input": QueryInput(query="show my top 3 recurring spending places in a month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_110",
    agent_class=UnprocessableEntityExtractionAgent,
    description="total payements to supermarkets this vs last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_110():
    return {
        "input": QueryInput(query="total payements to supermarkets this vs last year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_111",
    agent_class=UnprocessableEntityExtractionAgent,
    description="total money transferred to my savings account this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_111():
    return {
        "input": QueryInput(query="total money transferred to my savings account this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="savings account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_112",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times have I made purchases at Starbucks in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_112():
    return {
        "input": QueryInput(query="How many times have I made purchases at Starbucks in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_113",
    agent_class=UnprocessableEntityExtractionAgent,
    description="In which categories did I exceed my budget last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_113():
    return {
        "input": QueryInput(query="In which categories did I exceed my budget last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_114",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Whats the damage this month on my spending?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_114():
    return {
        "input": QueryInput(query="Whats the damage this month on my spending?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_115",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my top 3 subscription services by spending",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_115():
    return {
        "input": QueryInput(query="my top 3 subscription services by spending"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_116",
    agent_class=UnprocessableEntityExtractionAgent,
    description="At which merchant did I spend the most and during which time period in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_116():
    return {
        "input": QueryInput(query="At which merchant did I spend the most and during which time period in the last 6 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_117",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Why was my messages bill higher last month compared to August?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_117():
    return {
        "input": QueryInput(query="Why was my messages bill higher last month compared to August?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_118",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I spend more on dining out last month compared to this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_118():
    return {
        "input": QueryInput(query="Did I spend more on dining out last month compared to this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_119",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many transactions did I make last weekend?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_119():
    return {
        "input": QueryInput(query="How many transactions did I make last weekend?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_120",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I make any payments to Avis car hire in February this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_120():
    return {
        "input": QueryInput(query="Did I make any payments to Avis car hire in February this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_121",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Have there been any changes in the amounts paid to Netflix, Spotify, and Amazon through standing orders over the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_121():
    return {
        "input": QueryInput(query="Have there been any changes in the amounts paid to Netflix, Spotify, and Amazon through standing orders over the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_122",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I spent on my dog's vet bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_122():
    return {
        "input": QueryInput(query="How much have I spent on my dog's vet bills?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="dog's vet bills", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="dog's vet bills"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_123",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I spent on dog food in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_123():
    return {
        "input": QueryInput(query="How much have I spent on dog food in the last 6 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="dog food", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="dog food"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_124",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I spent at Apollo hospital this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_124():
    return {
        "input": QueryInput(query="How much have I spent at Apollo hospital this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_125",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was the amount of the last overdraft fee charged on my account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_125():
    return {
        "input": QueryInput(query="What was the amount of the last overdraft fee charged on my account?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="overdraft fee", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Substring(value="overdraft fee"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_126",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount of my Amazon bill for next month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_126():
    return {
        "input": QueryInput(query="What is the total amount of my Amazon bill for next month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_127",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I spend more than 1000 dollars on medical bills in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_127():
    return {
        "input": QueryInput(query="Did I spend more than 1000 dollars on medical bills in the last 6 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_128",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending on travel in August and September 2025?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_128():
    return {
        "input": QueryInput(query="What is my total spending on travel in August and September 2025?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_129",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Are there any rent refunds greater than 250 dollars this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_129():
    return {
        "input": QueryInput(query="Are there any rent refunds greater than 250 dollars this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_130",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my average order value for takeaway spending this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_130():
    return {
        "input": QueryInput(query="What is my average order value for takeaway spending this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_131",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount I have spent on my subscriptions in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_131():
    return {
        "input": QueryInput(query="What is the total amount I have spent on my subscriptions in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_132",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you break down my total spend of 1200 dollars in Spain last month by category or merchant?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_132():
    return {
        "input": QueryInput(query="Can you break down my total spend of 1200 dollars in Spain last month by category or merchant?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True),
                Entity(type="geographic", value="Spain", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)},
                {"type": Exact(value="geographic"), "value": Exact(value="Spain"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_133",
    agent_class=UnprocessableEntityExtractionAgent,
    description="how can i get my budget back on track",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_133():
    return {
        "input": QueryInput(query="how can i get my budget back on track"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_134",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What one time payments do I have coming up?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_134():
    return {
        "input": QueryInput(query="What one time payments do I have coming up?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_135",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Are there any other unusual transactions in my account from last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_135():
    return {
        "input": QueryInput(query="Are there any other unusual transactions in my account from last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_136",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Were there any refunds in my transactions from last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_136():
    return {
        "input": QueryInput(query="Were there any refunds in my transactions from last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_137",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend on food in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_137():
    return {
        "input": QueryInput(query="How much did I spend on food in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_138",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much money will I have left at the end of the month based on my current balance expected income and upcoming expenses?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_138():
    return {
        "input": QueryInput(query="How much money will I have left at the end of the month based on my current balance expected income and upcoming expenses?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="current balance", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="current balance"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_139",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I spent on groceries this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_139():
    return {
        "input": QueryInput(query="How much have I spent on groceries this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_140",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend at Walmart on groceries?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_140():
    return {
        "input": QueryInput(query="How much did I spend at Walmart on groceries?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_141",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my current bank account balance?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_141():
    return {
        "input": QueryInput(query="What is my current bank account balance?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="current bank account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="current bank account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_142",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_142():
    return {
        "input": QueryInput(query="What is my total spending this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_143",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend at McDonalds in May?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_143():
    return {
        "input": QueryInput(query="How much did I spend at McDonalds in May?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_144",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I pay for my utility bill in January?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_144():
    return {
        "input": QueryInput(query="How much did I pay for my utility bill in January?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_145",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Are there any refunds expected in my predicted expenses for next month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_145():
    return {
        "input": QueryInput(query="Are there any refunds expected in my predicted expenses for next month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_146",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total estimated spending for groceries dining out and online shopping in the next 7 days?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_146():
    return {
        "input": QueryInput(query="What is my total estimated spending for groceries dining out and online shopping in the next 7 days?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="transaction_channel", value="online shopping", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Substring(value="online shopping"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_147",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my forecasted spending on travel for the next 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_147():
    return {
        "input": QueryInput(query="What is my forecasted spending on travel for the next 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_148",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my estimated yearly spending on Amazon based on the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_148():
    return {
        "input": QueryInput(query="What is my estimated yearly spending on Amazon based on the last 6 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_149",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you track my spending on food and bills for this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_149():
    return {
        "input": QueryInput(query="Can you track my spending on food and bills for this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_150",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How would cutting down on eating out affect my ability to save £500 this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_150():
    return {
        "input": QueryInput(query="How would cutting down on eating out affect my ability to save £500 this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_151",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend at The Italian Place last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_151():
    return {
        "input": QueryInput(query="How much did I spend at The Italian Place last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_152",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many transactions have I made this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_152():
    return {
        "input": QueryInput(query="How many transactions have I made this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_153",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much would I save if I reduce my travel expenses by 20 percent in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_153():
    return {
        "input": QueryInput(query="How much would I save if I reduce my travel expenses by 20 percent in the last 6 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_154",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my biggest expense last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_154():
    return {
        "input": QueryInput(query="What was my biggest expense last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_155",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How can I avoid early withdrawal fees on my savings account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_155():
    return {
        "input": QueryInput(query="How can I avoid early withdrawal fees on my savings account?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings account", critical=True),
                Entity(type="financial_product", value="withdrawal fees", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="savings account"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Substring(value="withdrawal fees"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_156",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much money will I have left each month after accounting for my car loan payment, travel spending, and monthly bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_156():
    return {
        "input": QueryInput(query="How much money will I have left each month after accounting for my car loan payment, travel spending, and monthly bills?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="car loan", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Substring(value="car loan"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_157",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total interest I will pay if I pay an extra 400 pounds monthly on my 50000 pound loan at 4 percent interest over 10 years?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_157():
    return {
        "input": QueryInput(query="What is the total interest I will pay if I pay an extra 400 pounds monthly on my 50000 pound loan at 4 percent interest over 10 years?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="loan", critical=True),
                Entity(type="financial_product", value="interest", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Exact(value="loan"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Exact(value="interest"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_158",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend at Starbucks in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_158():
    return {
        "input": QueryInput(query="How much did I spend at Starbucks in the last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_159",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much total interest will I pay if I make monthly payments of 100 pounds on my 3000 pound credit card balance with an 18 percent APR?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_159():
    return {
        "input": QueryInput(query="How much total interest will I pay if I make monthly payments of 100 pounds on my 3000 pound credit card balance with an 18 percent APR?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="credit card", critical=True),
                Entity(type="financial_product", value="interest", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Substring(value="credit card"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Exact(value="interest"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_160",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What will happen to my ability to afford a £250 monthly direct debit for a new car if my income decreases?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_160():
    return {
        "input": QueryInput(query="What will happen to my ability to afford a £250 monthly direct debit for a new car if my income decreases?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_161",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount I will pay over 5 years for a £25000 loan with a 6.9 percent interest rate if I pay an extra £100 each month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_161():
    return {
        "input": QueryInput(query="What is the total amount I will pay over 5 years for a £25000 loan with a 6.9 percent interest rate if I pay an extra £100 each month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="loan", critical=True),
                Entity(type="financial_product", value="interest rate", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Exact(value="loan"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Substring(value="interest rate"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_162",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much do I spend monthly on Spotify?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_162():
    return {
        "input": QueryInput(query="How much do I spend monthly on Spotify?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_163",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the exact amount I spent on Netflix in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_163():
    return {
        "input": QueryInput(query="What is the exact amount I spent on Netflix in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_164",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How do I start investing in index funds?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_164():
    return {
        "input": QueryInput(query="How do I start investing in index funds?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="index funds", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Substring(value="index funds"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_165",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much should I allocate for travel and dining out each month based on my current budget and savings goal?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_165():
    return {
        "input": QueryInput(query="How much should I allocate for travel and dining out each month based on my current budget and savings goal?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_166",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I save in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_166():
    return {
        "input": QueryInput(query="How much did I save in 2023?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_167",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you help me set a budget for dining out and groceries for next month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_167():
    return {
        "input": QueryInput(query="Can you help me set a budget for dining out and groceries for next month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_168",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When will my delayed Pension Credit payment of 500 dollars be credited to my bank account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_168():
    return {
        "input": QueryInput(query="When will my delayed Pension Credit payment of 500 dollars be credited to my bank account?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="currency", value="dollars", critical=True),
                Entity(type="account", value="bank account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)},
                {"type": Exact(value="account"), "value": Substring(value="bank account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_169",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was the $50 Amazon transaction on the 5th of this month for?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_169():
    return {
        "input": QueryInput(query="What was the $50 Amazon transaction on the 5th of this month for?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_170",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_170():
    return {
        "input": QueryInput(query="What is my total spending in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_171",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I paid in interest on my credit card this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_171():
    return {
        "input": QueryInput(query="How much have I paid in interest on my credit card this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="credit card", critical=True),
                Entity(type="financial_product", value="interest", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Substring(value="credit card"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Exact(value="interest"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_172",
    agent_class=UnprocessableEntityExtractionAgent,
    description="If I cancel my streaming subscriptions how much would I save monthly",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_172():
    return {
        "input": QueryInput(query="If I cancel my streaming subscriptions how much would I save monthly"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_173",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Was my last payment to John Smith a regular or recurring payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_173():
    return {
        "input": QueryInput(query="Was my last payment to John Smith a regular or recurring payment?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="John Smith", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Substring(value="John Smith"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_174",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Has John Smith paid me the 200 dollars that was due last week?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_174():
    return {
        "input": QueryInput(query="Has John Smith paid me the 200 dollars that was due last week?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="John Smith", critical=True),
                Entity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Substring(value="John Smith"), "critical": Exact(value=True)},
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_175",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When is the next subscription payment due?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_175():
    return {
        "input": QueryInput(query="When is the next subscription payment due?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_176",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What are my roundup savings for the last two months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_176():
    return {
        "input": QueryInput(query="What are my roundup savings for the last two months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_177",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Why did I pay less credit card interest in 2023 compared to 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_177():
    return {
        "input": QueryInput(query="Why did I pay less credit card interest in 2023 compared to 2022?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="credit card", critical=True),
                Entity(type="financial_product", value="interest", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Substring(value="credit card"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Exact(value="interest"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_178",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much more do I need to add to my current account balance to qualify for the discount on the account fee?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_178():
    return {
        "input": QueryInput(query="How much more do I need to add to my current account balance to qualify for the discount on the account fee?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="current account", critical=True),
                Entity(type="financial_product", value="account fee", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="current account"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Substring(value="account fee"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_179",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What are my total charges including fees and interest in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_179():
    return {
        "input": QueryInput(query="What are my total charges including fees and interest in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="fees", critical=True),
                Entity(type="financial_product", value="interest", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Exact(value="fees"), "critical": Exact(value=True)},
                {"type": Exact(value="financial_product"), "value": Exact(value="interest"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_180",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much money do I have left in my shopping budget for this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_180():
    return {
        "input": QueryInput(query="How much money do I have left in my shopping budget for this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_181",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend on Amazon in 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_181():
    return {
        "input": QueryInput(query="How much did I spend on Amazon in 2023 and 2024?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_182",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_182():
    return {
        "input": QueryInput(query="What is my total spending in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_183",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my smallest grocery transaction in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_183():
    return {
        "input": QueryInput(query="What is my smallest grocery transaction in the last 3 months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_184",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_184():
    return {
        "input": QueryInput(query="What is my total spending in the last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_185",
    agent_class=UnprocessableEntityExtractionAgent,
    description="my total spend in travel in 6 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_185():
    return {
        "input": QueryInput(query="my total spend in travel in 6 months"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_186",
    agent_class=UnprocessableEntityExtractionAgent,
    description="show my travel cost",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_186():
    return {
        "input": QueryInput(query="show my travel cost"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_187",
    agent_class=UnprocessableEntityExtractionAgent,
    description="show bill",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_187():
    return {
        "input": QueryInput(query="show bill"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_188",
    agent_class=UnprocessableEntityExtractionAgent,
    description="spend mrch and feb",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_188():
    return {
        "input": QueryInput(query="spend mrch and feb"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_189",
    agent_class=UnprocessableEntityExtractionAgent,
    description="what refunds",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_189():
    return {
        "input": QueryInput(query="what refunds"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_190",
    agent_class=UnprocessableEntityExtractionAgent,
    description="spend in nike and adidas",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_190():
    return {
        "input": QueryInput(query="spend in nike and adidas"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_191",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What did I spend on bills and travel?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_191():
    return {
        "input": QueryInput(query="What did I spend on bills and travel?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_192",
    agent_class=UnprocessableEntityExtractionAgent,
    description="total bills",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_192():
    return {
        "input": QueryInput(query="total bills"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_193",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending in the last six months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_193():
    return {
        "input": QueryInput(query="What is my total spending in the last six months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_194",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending across all merchants in the last six months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_194():
    return {
        "input": QueryInput(query="What is my total spending across all merchants in the last six months?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_195",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total loan payment in the last 2 years?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_195():
    return {
        "input": QueryInput(query="What is my total loan payment in the last 2 years?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="loan", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Exact(value="loan"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_196",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the total amount I have paid towards my loans in the last 2 years?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_196():
    return {
        "input": QueryInput(query="What is the total amount I have paid towards my loans in the last 2 years?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="loans", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Exact(value="loans"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_197",
    agent_class=UnprocessableEntityExtractionAgent,
    description="spending in bus tickets?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_197():
    return {
        "input": QueryInput(query="spending in bus tickets?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="bus tickets", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="bus tickets"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_198",
    agent_class=UnprocessableEntityExtractionAgent,
    description="spending in bus tickets in the last 3 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_198():
    return {
        "input": QueryInput(query="spending in bus tickets in the last 3 months"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="product_service", value="bus tickets", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="bus tickets"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_199",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many transactions did I make in Scotland versus England in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_199():
    return {
        "input": QueryInput(query="How many transactions did I make in Scotland versus England in the last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="geographic", value="Scotland", critical=True),
                Entity(type="geographic", value="England", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Exact(value="Scotland"), "critical": Exact(value=True)},
                {"type": Exact(value="geographic"), "value": Exact(value="England"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_200",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much do I have left at the end of each month in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_200():
    return {
        "input": QueryInput(query="How much do I have left at the end of each month in 2023?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_201",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you show me a summary of my recent transactions?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_201():
    return {
        "input": QueryInput(query="Can you show me a summary of my recent transactions?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_202",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you show me a breakdown of my expenses for the past three months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_202():
    return {
        "input": QueryInput(query="Can you show me a breakdown of my expenses for the past three months"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_203",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Can you show me a list of my biggest transactions this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_203():
    return {
        "input": QueryInput(query="Can you show me a list of my biggest transactions this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_204",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many times has my account balance dropped below 2000 pounds in the last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_204():
    return {
        "input": QueryInput(query="How many times has my account balance dropped below 2000 pounds in the last year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="account balance", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="account balance"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_205",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the trend of my monthly spending on Entertainment merchant category in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_205():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending on Entertainment merchant category in 2023?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_206",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the correlation between my account balance and my total monthly spending",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_206():
    return {
        "input": QueryInput(query="What is the correlation between my account balance and my total monthly spending"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="account balance", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="account balance"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_207",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the month over month growth rate of my spending in each merchant subcategory",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_207():
    return {
        "input": QueryInput(query="What is the month over month growth rate of my spending in each merchant subcategory"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_208",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the percentage of my total spending that each merchant category represents and how has this percentage changed month over month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_208():
    return {
        "input": QueryInput(query="What is the percentage of my total spending that each merchant category represents and how has this percentage changed month over month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_209",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the trend of my monthly spending in each merchant category over the past year and how does this compare to the trend of my overall monthly spending",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_209():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending in each merchant category over the past year and how does this compare to the trend of my overall monthly spending"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_210",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my account balance at the end of 2023 and how much did I spend on online shopping?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_210():
    return {
        "input": QueryInput(query="What was my account balance at the end of 2023 and how much did I spend on online shopping?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="account balance", critical=True),
                Entity(type="transaction_channel", value="online shopping", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="account balance"), "critical": Exact(value=True)},
                {"type": Exact(value="transaction_channel"), "value": Substring(value="online shopping"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_211",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Am I spending more or less a month than I did last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_211():
    return {
        "input": QueryInput(query="Am I spending more or less a month than I did last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_212",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my biggest outgoing?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_212():
    return {
        "input": QueryInput(query="What is my biggest outgoing?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_213",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many days was I overdrawn last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_213():
    return {
        "input": QueryInput(query="How many days was I overdrawn last year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="overdrawn", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Exact(value="overdrawn"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_214",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What percentage of my total expenses was spent on subscriptions this year and how has that changed each month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_214():
    return {
        "input": QueryInput(query="What percentage of my total expenses was spent on subscriptions this year and how has that changed each month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_215",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my total spending on food last year compared to this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_215():
    return {
        "input": QueryInput(query="What was my total spending on food last year compared to this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_216",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When is my car insurance due for renewal?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_216():
    return {
        "input": QueryInput(query="When is my car insurance due for renewal?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_217",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Details of fortnightly Wednesday payments also monthly Monday payments from the DWP",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_217():
    return {
        "input": QueryInput(query="Details of fortnightly Wednesday payments also monthly Monday payments from the DWP"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_218",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I saved this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_218():
    return {
        "input": QueryInput(query="How much have I saved this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_219",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I send that money to X",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_219():
    return {
        "input": QueryInput(query="Did I send that money to X"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="X", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="X"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_220",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Has X sent me the money they owe me",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_220():
    return {
        "input": QueryInput(query="Has X sent me the money they owe me"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="X", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="X"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_221",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much money have I sent to John since August?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_221():
    return {
        "input": QueryInput(query="How much money have I sent to John since August?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="John", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="John"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_222",
    agent_class=UnprocessableEntityExtractionAgent,
    description="I have got a payment to aspire teaching can you tell me what this is please",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_222():
    return {
        "input": QueryInput(query="I have got a payment to aspire teaching can you tell me what this is please"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_223",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Where is most of my cash going?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_223():
    return {
        "input": QueryInput(query="Where is most of my cash going?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="payment_method", value="cash", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Exact(value="cash"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_224",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Am I spending more than usual?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_224():
    return {
        "input": QueryInput(query="Am I spending more than usual?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_225",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I stay within my budget?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_225():
    return {
        "input": QueryInput(query="Did I stay within my budget?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_226",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Was there a spike in spending recently?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_226():
    return {
        "input": QueryInput(query="Was there a spike in spending recently?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_227",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend when I was out last weekend",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_227():
    return {
        "input": QueryInput(query="How much did I spend when I was out last weekend"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_228",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much was my last insurance payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_228():
    return {
        "input": QueryInput(query="How much was my last insurance payment?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_229",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I save through round ups last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_229():
    return {
        "input": QueryInput(query="How much did I save through round ups last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_230",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Did I pay any overdraft fees this year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_230():
    return {
        "input": QueryInput(query="Did I pay any overdraft fees this year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="overdraft fees", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Substring(value="overdraft fees"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_231",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much do I typically spend between 8pm and 1am on Fridays?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_231():
    return {
        "input": QueryInput(query="How much do I typically spend between 8pm and 1am on Fridays?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_232",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my budget for Groceries?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_232():
    return {
        "input": QueryInput(query="What is my budget for Groceries?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_233",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I spent at Amazon in the last month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_233():
    return {
        "input": QueryInput(query="How much have I spent at Amazon in the last month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_234",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much did I spend on my night out last night",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_234():
    return {
        "input": QueryInput(query="How much did I spend on my night out last night"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_235",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What was my total spend whilst on holiday",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_235():
    return {
        "input": QueryInput(query="What was my total spend whilst on holiday"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_236",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many roundups did I save last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_236():
    return {
        "input": QueryInput(query="How many roundups did I save last year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_237",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What's the fee for my account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_237():
    return {
        "input": QueryInput(query="What's the fee for my account?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="financial_product", value="fee", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="financial_product"), "value": Exact(value="fee"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_238",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Am I on track to stay within my shopping budget this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_238():
    return {
        "input": QueryInput(query="Am I on track to stay within my shopping budget this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_239",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much money did I receive from my savings account",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_239():
    return {
        "input": QueryInput(query="How much money did I receive from my savings account"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="savings account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_240",
    agent_class=UnprocessableEntityExtractionAgent,
    description="what was my account balance at the end of 2023, and how much did i spend on online shopping?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_240():
    return {
        "input": QueryInput(query="what was my account balance at the end of 2023, and how much did i spend on online shopping?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="account balance", critical=True),
                Entity(type="transaction_channel", value="online shopping", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="account balance"), "critical": Exact(value=True)},
                {"type": Exact(value="transaction_channel"), "value": Substring(value="online shopping"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_241",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the trend of my monthly spending on 'Entertainment' merchant category in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_241():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending on 'Entertainment' merchant category in 2023?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_242",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the correlation between my account balance and my total monthly spending?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_242():
    return {
        "input": QueryInput(query="What is the correlation between my account balance and my total monthly spending?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="account balance", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="account balance"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_243",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Which merchant subcategories have seen the most significant increase in my spending over the past year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_243():
    return {
        "input": QueryInput(query="Which merchant subcategories have seen the most significant increase in my spending over the past year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_244",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the month-over-month growth rate of my spending in each merchant subcategory?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_244():
    return {
        "input": QueryInput(query="What is the month-over-month growth rate of my spending in each merchant subcategory?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_245",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How does my average daily spending in each merchant category compare to the average daily spending in the previous month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_245():
    return {
        "input": QueryInput(query="How does my average daily spending in each merchant category compare to the average daily spending in the previous month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_246",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the percentage of my total spending that each merchant category represents, and how has this percentage changed month-over-month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_246():
    return {
        "input": QueryInput(query="What is the percentage of my total spending that each merchant category represents, and how has this percentage changed month-over-month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_247",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is the trend of my monthly spending in each merchant category over the past year, and how does this compare to the trend of my overall monthly spending?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_247():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending in each merchant category over the past year, and how does this compare to the trend of my overall monthly spending?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_248",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What are the top 3 merchant names where my spending has decreased the most in the last six months, and what is the percentage decrease for each?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_248():
    return {
        "input": QueryInput(query="What are the top 3 merchant names where my spending has decreased the most in the last six months, and what is the percentage decrease for each?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_249",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What percentage of my total expenses was spent on subscriptions this year, and how has that changed monthly?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_249():
    return {
        "input": QueryInput(query="What percentage of my total expenses was spent on subscriptions this year, and how has that changed monthly?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_250",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When did I make my first mortgage payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_250():
    return {
        "input": QueryInput(query="When did I make my first mortgage payment?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_251",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much have I saved this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_251():
    return {
        "input": QueryInput(query="How much have I saved this year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_252",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When do I get my Chb?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_252():
    return {
        "input": QueryInput(query="When do I get my Chb?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_253",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What days am I most likely to order a takeaway?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_253():
    return {
        "input": QueryInput(query="What days am I most likely to order a takeaway?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_254",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much money  have I transferred to my savings account this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_254():
    return {
        "input": QueryInput(query="How much money  have I transferred to my savings account this month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="account", value="savings account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="savings account"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_255",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Am I spending more than usual?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_255():
    return {
        "input": QueryInput(query="Am I spending more than usual?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_256",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How much round ups did I save last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_256():
    return {
        "input": QueryInput(query="How much round ups did I save last year?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_257",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Show me a breakdown of next month's predicted expenses by category.",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_257():
    return {
        "input": QueryInput(query="Show me a breakdown of next month's predicted expenses by category."),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_258",
    agent_class=UnprocessableEntityExtractionAgent,
    description="When was my last payment to John Smith?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_258():
    return {
        "input": QueryInput(query="When was my last payment to John Smith?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                Entity(type="person_recipient", value="John Smith", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Substring(value="John Smith"), "critical": Exact(value=True)}
            ])
        }
    }
@eval_case(
    name="predicted_intent_259",
    agent_class=UnprocessableEntityExtractionAgent,
    description="How many roundups did I save last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_259():
    return {
        "input": QueryInput(query="How many roundups did I save last year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
@eval_case(
    name="predicted_intent_260",
    agent_class=UnprocessableEntityExtractionAgent,
    description="What is my total spending in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_260():
    return {
        "input": QueryInput(query="What is my total spending in the last month?"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }