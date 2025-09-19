"""
Evaluation cases for ProcessableEntityExtractionAgent from predicted user intents.
Generated from predicted_user_intent_1.csv
"""

from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact, Substring
from src.workflow_nodes.query_preprocessing.processable_entity_extraction_agent import ProcessableEntityExtractionAgent
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import ProcessableEntityExtractionOutput, ProcessableEntity as Entity


# ========== Predicted User Intent Cases (260) ==========

@eval_case(
    name="predicted_intent_001",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I receive any cashbacks or refunds from groceries or Amazon in 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_001():
    return {
        "input": QueryInput(query="Did I receive any cashbacks or refunds from groceries or Amazon in 2023 and 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="2023"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_002",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was the day in 2024 when my combined spending on groceries and Amazon was the highest?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_002():
    return {
        "input": QueryInput(query="What was the day in 2024 when my combined spending on groceries and Amazon was the highest?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="2024"),
                Entity(type="category", value="groceries"),
                Entity(type="merchant", value="Amazon")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="2024")},
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_003",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which restaurants did I spend $150 on dining out last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_003():
    return {
        "input": QueryInput(query="Which restaurants did I spend $150 on dining out last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="restaurants"),
                Entity(type="amount", value="$150"),
                Entity(type="category", value="dining out"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="restaurants")},
                {"type": Exact(value="amount"), "value": Exact(value="$150")},
                {"type": Exact(value="category"), "value": Exact(value="dining out")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_004",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my total spending on groceries and dining out in the last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_004():
    return {
        "input": QueryInput(query="What was my total spending on groceries and dining out in the last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="category", value="dining out"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="category"), "value": Exact(value="dining out")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_005",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending in the last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_005():
    return {
        "input": QueryInput(query="What is my total spending in the last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_006",
    agent_class=ProcessableEntityExtractionAgent,
    description="my payments to Amzn past 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_006():
    return {
        "input": QueryInput(query="my payments to Amzn past 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amzn"),
                Entity(type="temporal", value="past 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amzn")},
                {"type": Exact(value="temporal"), "value": Exact(value="past 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_007",
    agent_class=ProcessableEntityExtractionAgent,
    description="Where did I spend cash in the Entertainment category last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_007():
    return {
        "input": QueryInput(query="Where did I spend cash in the Entertainment category last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="Entertainment"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="Entertainment")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_008",
    agent_class=ProcessableEntityExtractionAgent,
    description="Was RetailMart the store where I spent the most last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_008():
    return {
        "input": QueryInput(query="Was RetailMart the store where I spent the most last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="RetailMart"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="RetailMart")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_009",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times did I eat out last month and at which place did I eat out the most?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_009():
    return {
        "input": QueryInput(query="How many times did I eat out last month and at which place did I eat out the most?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="eat out"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="eat")},  # Could be "eat out" or "eating out"
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_010",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much of my Dining and Groceries spending last month were online payments?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_010():
    return {
        "input": QueryInput(query="How much of my Dining and Groceries spending last month were online payments?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="Dining"),
                Entity(type="category", value="Groceries"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="Dining")},
                {"type": Exact(value="category"), "value": Exact(value="Groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


# Continue with queries 11-30
@eval_case(
    name="predicted_intent_011",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times did I spend more than 100 dollars at Starbucks in 2022 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_011():
    return {
        "input": QueryInput(query="How many times did I spend more than 100 dollars at Starbucks in 2022 2023 and 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="more than 100 dollars"),
                Entity(type="merchant", value="Starbucks"),
                Entity(type="temporal", value="2022"),
                Entity(type="temporal", value="2023"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Substring(value="100 dollars")},
                {"type": Exact(value="merchant"), "value": Exact(value="Starbucks")},
                {"type": Exact(value="temporal"), "value": Exact(value="2022")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


# Additional representative cases from the 260 queries
@eval_case(
    name="predicted_intent_012",
    agent_class=ProcessableEntityExtractionAgent,
    description="When was my most recent visit to Starbucks?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_012():
    return {
        "input": QueryInput(query="When was my most recent visit to Starbucks?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Starbucks")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Starbucks")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_022",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I spend at Trader Joes in 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_022():
    return {
        "input": QueryInput(query="Did I spend at Trader Joes in 2022?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Trader Joes"),
                Entity(type="temporal", value="2022")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Trader Joes")},
                {"type": Exact(value="temporal"), "value": Exact(value="2022")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_029",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I spend over my budget last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_029():
    return {
        "input": QueryInput(query="Did I spend over my budget last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="budget", value="budget"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_033",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend on Entertainment in August 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_033():
    return {
        "input": QueryInput(query="How much did I spend on Entertainment in August 2023?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="Entertainment"),
                Entity(type="temporal", value="August 2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="Entertainment")},
                {"type": Exact(value="temporal"), "value": Exact(value="August 2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_052",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much of my grocery budget is left for this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_052():
    return {
        "input": QueryInput(query="How much of my grocery budget is left for this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="grocery"),
                Entity(type="budget", value="budget"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="grocery")},
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_069",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending at McDonald's last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_069():
    return {
        "input": QueryInput(query="What is my total spending at McDonald's last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="McDonald's"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="McDonald's")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_072",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I pay my bills this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_072():
    return {
        "input": QueryInput(query="Did I pay my bills this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bills"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


# Continue adding missing queries to reach 260 total
@eval_case(
    name="predicted_intent_013",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending at Starbucks in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_013():
    return {
        "input": QueryInput(query="What is my total spending at Starbucks in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Starbucks"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Starbucks")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_014",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which stores do I usually shop at for groceries?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_014():
    return {
        "input": QueryInput(query="Which stores do I usually shop at for groceries?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_015",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I exceed my grocery budget last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_015():
    return {
        "input": QueryInput(query="Did I exceed my grocery budget last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="grocery"),
                Entity(type="budget", value="budget"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="grocery")},
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_016",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I exceed my grocery budget in the last year and how many times did that happen?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_016():
    return {
        "input": QueryInput(query="Did I exceed my grocery budget in the last year and how many times did that happen?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="grocery"),
                Entity(type="budget", value="budget"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="grocery")},
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_017",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which hotel did I stay at in December 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_017():
    return {
        "input": QueryInput(query="Which hotel did I stay at in December 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="December 2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="December 2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_018",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which specific utility did I spend the most on in 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_018():
    return {
        "input": QueryInput(query="Which specific utility did I spend the most on in 2023 and 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="2023"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="2023")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_019",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did I start my tennis lessons last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_019():
    return {
        "input": QueryInput(query="When did I start my tennis lessons last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_020",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend in February and March this year compared to last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_020():
    return {
        "input": QueryInput(query="How much did I spend in February and March this year compared to last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="February"),
                Entity(type="temporal", value="March"),
                Entity(type="temporal", value="this year"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="February")},
                {"type": Exact(value="temporal"), "value": Exact(value="March")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_021",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I spend at Trader Joes in 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_021():
    return {
        "input": QueryInput(query="Did I spend at Trader Joes in 2022?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Trader Joes"),
                Entity(type="temporal", value="2022")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Trader Joes")},
                {"type": Exact(value="temporal"), "value": Exact(value="2022")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_023",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my month on month spending at Walmart Whole Foods and Trader Joes for groceries in 2023",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_023():
    return {
        "input": QueryInput(query="What is my month on month spending at Walmart Whole Foods and Trader Joes for groceries in 2023"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Walmart"),
                Entity(type="merchant", value="Whole Foods"),
                Entity(type="merchant", value="Trader Joes"),
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Walmart")},
                {"type": Exact(value="merchant"), "value": Exact(value="Whole Foods")},
                {"type": Exact(value="merchant"), "value": Exact(value="Trader Joes")},
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_024",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I spent on train and bus this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_024():
    return {
        "input": QueryInput(query="How much have I spent on train and bus this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="train"),
                Entity(type="category", value="bus"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="train")},
                {"type": Exact(value="category"), "value": Exact(value="bus")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_025",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which of my direct debit merchants Netflix Spotify Amazon or Disney Plus has the highest subscription...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_025():
    return {
        "input": QueryInput(query="Which of my direct debit merchants Netflix Spotify Amazon or Disney Plus has the highest subscription fee?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Netflix"),
                Entity(type="merchant", value="Spotify"),
                Entity(type="merchant", value="Amazon"),
                Entity(type="merchant", value="Disney Plus")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Netflix")},
                {"type": Exact(value="merchant"), "value": Exact(value="Spotify")},
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="merchant"), "value": Exact(value="Disney Plus")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_026",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did I change my Netflix direct debit plan from 20 dollars to 37 dollars?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_026():
    return {
        "input": QueryInput(query="When did I change my Netflix direct debit plan from 20 dollars to 37 dollars?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Netflix"),
                Entity(type="amount", value="20 dollars"),
                Entity(type="amount", value="37 dollars")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Netflix")},
                {"type": Exact(value="amount"), "value": Exact(value="20 dollars")},
                {"type": Exact(value="amount"), "value": Exact(value="37 dollars")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_027",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which airlines have I flown with in the past year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_027():
    return {
        "input": QueryInput(query="Which airlines have I flown with in the past year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="past year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="past year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_028",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was the total amount of direct debits from my account in February 2025?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_028():
    return {
        "input": QueryInput(query="What was the total amount of direct debits from my account in February 2025?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="February 2025")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="February 2025")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_030",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total amount spent at Amazon in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_030():
    return {
        "input": QueryInput(query="What is my total amount spent at Amazon in the last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_031",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount I received from my savings account each month in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_031():
    return {
        "input": QueryInput(query="What is the total amount I received from my savings account each month in 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_032",
    agent_class=ProcessableEntityExtractionAgent,
    description="What are my recurring payments over 50 dollars in the past three months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_032():
    return {
        "input": QueryInput(query="What are my recurring payments over 50 dollars in the past three months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="over 50 dollars"),
                Entity(type="temporal", value="past three months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Substring(value="50 dollars")},
                {"type": Exact(value="temporal"), "value": Exact(value="past three months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_034",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did I receive a refund from Tesco and what was the amount?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_034():
    return {
        "input": QueryInput(query="When did I receive a refund from Tesco and what was the amount?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Tesco")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Tesco")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_035",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my average amount spent per transaction in September",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_035():
    return {
        "input": QueryInput(query="What is my average amount spent per transaction in September"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="September")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="September")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_036",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my biggest outgoing transaction in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_036():
    return {
        "input": QueryInput(query="What is my biggest outgoing transaction in 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_037",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my spending at Burger King this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_037():
    return {
        "input": QueryInput(query="What is my spending at Burger King this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Burger King"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Burger King")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_038",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which subscription between TV Sky and Netflix had more frequent payments over the last 2 years",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_038():
    return {
        "input": QueryInput(query="Which subscription between TV Sky and Netflix had more frequent payments over the last 2 years"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="TV Sky"),
                Entity(type="merchant", value="Netflix"),
                Entity(type="temporal", value="last 2 years")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="TV Sky")},
                {"type": Exact(value="merchant"), "value": Exact(value="Netflix")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 2 years")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_039",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times did I order from Zomato in July?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_039():
    return {
        "input": QueryInput(query="How many times did I order from Zomato in July?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Zomato"),
                Entity(type="temporal", value="July")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Zomato")},
                {"type": Exact(value="temporal"), "value": Exact(value="July")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_040",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my account balance after sending $200 to Phil on 15th October?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_040():
    return {
        "input": QueryInput(query="What was my account balance after sending $200 to Phil on 15th October?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="$200"),
                Entity(type="temporal", value="15th October")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="$200")},
                {"type": Exact(value="temporal"), "value": Exact(value="15th October")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_041",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which month did I receive the lowest rent income this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_041():
    return {
        "input": QueryInput(query="Which month did I receive the lowest rent income this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="rent income"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="rent")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_042",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which month in the past year did I transfer the maximum amount to my savings account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_042():
    return {
        "input": QueryInput(query="Which month in the past year did I transfer the maximum amount to my savings account?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings"),
                Entity(type="temporal", value="past year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")},
                {"type": Exact(value="temporal"), "value": Exact(value="past year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_043",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many transactions contributed to the 450 dollars spent at Cliveland Cafe in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_043():
    return {
        "input": QueryInput(query="How many transactions contributed to the 450 dollars spent at Cliveland Cafe in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="450 dollars"),
                Entity(type="merchant", value="Cliveland Cafe"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="450 dollars")},
                {"type": Exact(value="merchant"), "value": Exact(value="Cliveland Cafe")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_044",
    agent_class=ProcessableEntityExtractionAgent,
    description="Why is there a transaction for Cliveland Cafe in my dining expenses if I never went there?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_044():
    return {
        "input": QueryInput(query="Why is there a transaction for Cliveland Cafe in my dining expenses if I never went there?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Cliveland Cafe"),
                Entity(type="category", value="dining")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Cliveland Cafe")},
                {"type": Exact(value="category"), "value": Exact(value="dining")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_045",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you review my spending from last weekend and provide a breakdown to verify the total amount spent?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_045():
    return {
        "input": QueryInput(query="Can you review my spending from last weekend and provide a breakdown to verify the total amount spent?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last weekend")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last weekend")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_046",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you recheck how much I spent last weekend?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_046():
    return {
        "input": QueryInput(query="Can you recheck how much I spent last weekend?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last weekend")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last weekend")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_047",
    agent_class=ProcessableEntityExtractionAgent,
    description="can you help me with my bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_047():
    return {
        "input": QueryInput(query="can you help me with my bills?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_048",
    agent_class=ProcessableEntityExtractionAgent,
    description="how do I pay my electricity bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_048():
    return {
        "input": QueryInput(query="how do I pay my electricity bills?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="electricity bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="electricity")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_049",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you find any payments made to Avis car hire in the last month, the last 6 months, and in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_049():
    return {
        "input": QueryInput(query="\"Can you find any payments made to Avis car hire in the last month, the last 6 months, and in 2024?\""),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Avis car hire"),
                Entity(type="temporal", value="last month"),
                Entity(type="temporal", value="last 6 months"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Substring(value="Avis")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_050",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my average amount spent per store for food during Xmas 2022 at Walmart Whole Foods and Trader...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_050():
    return {
        "input": QueryInput(query="What was my average amount spent per store for food during Xmas 2022 at Walmart Whole Foods and Trader Joes?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="food"),
                Entity(type="temporal", value="Xmas 2022"),
                Entity(type="merchant", value="Walmart"),
                Entity(type="merchant", value="Whole Foods"),
                Entity(type="merchant", value="Trader Joes")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="food")},
                {"type": Exact(value="temporal"), "value": Exact(value="Xmas 2022")},
                {"type": Exact(value="merchant"), "value": Exact(value="Walmart")},
                {"type": Exact(value="merchant"), "value": Exact(value="Whole Foods")},
                {"type": Exact(value="merchant"), "value": Exact(value="Trader Joes")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_051",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which months did I have round up savings this year till now?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_051():
    return {
        "input": QueryInput(query="Which months did I have round up savings this year till now?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_053",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend in total in the first quarter of the year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_053():
    return {
        "input": QueryInput(query="How much did I spend in total in the first quarter of the year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="first quarter")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="first quarter")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_054",
    agent_class=ProcessableEntityExtractionAgent,
    description="Were there any refunds among my biggest transactions last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_054():
    return {
        "input": QueryInput(query="Were there any refunds among my biggest transactions last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_055",
    agent_class=ProcessableEntityExtractionAgent,
    description="In which category or at which merchant did I spend the most in March June September October and December...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_055():
    return {
        "input": QueryInput(query="In which category or at which merchant did I spend the most in March June September October and December when my account balance dropped below 2000 pounds"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="category"),
                Entity(type="merchant", value="merchant"),
                Entity(type="temporal", value="March"),
                Entity(type="temporal", value="June"),
                Entity(type="temporal", value="September"),
                Entity(type="temporal", value="October"),
                Entity(type="temporal", value="December"),
                Entity(type="amount", value="2000 pounds")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="category")},
                {"type": Exact(value="merchant"), "value": Exact(value="merchant")},
                {"type": Exact(value="temporal"), "value": Exact(value="March")},
                {"type": Exact(value="temporal"), "value": Exact(value="June")},
                {"type": Exact(value="temporal"), "value": Exact(value="September")},
                {"type": Exact(value="temporal"), "value": Exact(value="October")},
                {"type": Exact(value="temporal"), "value": Exact(value="December")},
                {"type": Exact(value="amount"), "value": Exact(value="2000 pounds")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_056",
    agent_class=ProcessableEntityExtractionAgent,
    description="Who were my most frequently used travel vendors in July?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_056():
    return {
        "input": QueryInput(query="Who were my most frequently used travel vendors in July?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel"),
                Entity(type="temporal", value="July")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")},
                {"type": Exact(value="temporal"), "value": Exact(value="July")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_057",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times did I dine out each month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_057():
    return {
        "input": QueryInput(query="How many times did I dine out each month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="dine out")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="dine")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_058",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the month over month growth rate of my spending in each merchant subcategory",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_058():
    return {
        "input": QueryInput(query="What is the month over month growth rate of my spending in each merchant subcategory"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="merchant")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="merchant")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_059",
    agent_class=ProcessableEntityExtractionAgent,
    description="Compare my average daily spending in each expense area to the average daily spending in the previous month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_059():
    return {
        "input": QueryInput(query="Compare my average daily spending in each expense area to the average daily spending in the previous month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="previous month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="previous month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_060",
    agent_class=ProcessableEntityExtractionAgent,
    description="What were my bottom 3 spending categories last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_060():
    return {
        "input": QueryInput(query="What were my bottom 3 spending categories last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_061",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount I spent at Amazon and Starbucks in the last six months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_061():
    return {
        "input": QueryInput(query="What is the total amount I spent at Amazon and Starbucks in the last six months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="merchant", value="Starbucks"),
                Entity(type="temporal", value="last six months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="merchant"), "value": Exact(value="Starbucks")},
                {"type": Exact(value="temporal"), "value": Exact(value="last six months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_062",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times did I visit Starbucks in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_062():
    return {
        "input": QueryInput(query="How many times did I visit Starbucks in 2023?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Starbucks"),
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Starbucks")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_063",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many transactions did I make on Amazon and eBay in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_063():
    return {
        "input": QueryInput(query="How many transactions did I make on Amazon and eBay in 2023?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="merchant", value="eBay"),
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="merchant"), "value": Exact(value="eBay")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_064",
    agent_class=ProcessableEntityExtractionAgent,
    description="How does my spending on Amazon in 2023 compare to my spending on Amazon in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_064():
    return {
        "input": QueryInput(query="How does my spending on Amazon in 2023 compare to my spending on Amazon in 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="2023"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_065",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending on sports this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_065():
    return {
        "input": QueryInput(query="What is my total spending on sports this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="sports"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="sports")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_066",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which airline was my second highest in terms of spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_066():
    return {
        "input": QueryInput(query="Which airline was my second highest in terms of spending in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_067",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend on fuel in 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_067():
    return {
        "input": QueryInput(query="How much did I spend on fuel in 2022?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="fuel"),
                Entity(type="temporal", value="2022")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="fuel")},
                {"type": Exact(value="temporal"), "value": Exact(value="2022")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_068",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times was I overdrawn in March?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_068():
    return {
        "input": QueryInput(query="How many times was I overdrawn in March?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="March")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="March")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_070",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I receive any refunds from McDonalds last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_070():
    return {
        "input": QueryInput(query="Did I receive any refunds from McDonalds last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="McDonalds"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="McDonalds")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_071",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total water bill for this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_071():
    return {
        "input": QueryInput(query="What is my total water bill for this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="water bill"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="water")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_073",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the highest amount I spent on subscriptions in any month this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_073():
    return {
        "input": QueryInput(query="What is the highest amount I spent on subscriptions in any month this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="subscriptions"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="subscriptions")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_074",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you list all the merchants I purchased from for groceries in 2023",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_074():
    return {
        "input": QueryInput(query="Can you list all the merchants I purchased from for groceries in 2023"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_075",
    agent_class=ProcessableEntityExtractionAgent,
    description="List the stores where I purchased groceries in 2023",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_075():
    return {
        "input": QueryInput(query="List the stores where I purchased groceries in 2023"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_076",
    agent_class=ProcessableEntityExtractionAgent,
    description="my total earning on rent?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_076():
    return {
        "input": QueryInput(query="my total earning on rent?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="rent")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="rent")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_077",
    agent_class=ProcessableEntityExtractionAgent,
    description="how much I spend in rent?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_077():
    return {
        "input": QueryInput(query="how much I spend in rent?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="rent")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="rent")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_078",
    agent_class=ProcessableEntityExtractionAgent,
    description="my total medical bills at drugstores",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_078():
    return {
        "input": QueryInput(query="my total medical bills at drugstores"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="medical bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="medical")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_079",
    agent_class=ProcessableEntityExtractionAgent,
    description="my total medical bills at hospital",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_079():
    return {
        "input": QueryInput(query="my total medical bills at hospital"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="medical bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="medical")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_080",
    agent_class=ProcessableEntityExtractionAgent,
    description="What refunds did I receive last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_080():
    return {
        "input": QueryInput(query="What refunds did I receive last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_081",
    agent_class=ProcessableEntityExtractionAgent,
    description="What items did I purchase in my $300 transaction at Costco last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_081():
    return {
        "input": QueryInput(query="What items did I purchase in my $300 transaction at Costco last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="$300"),
                Entity(type="merchant", value="Costco"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="$300")},
                {"type": Exact(value="merchant"), "value": Exact(value="Costco")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_082",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did I last pay my Costco membership fee",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_082():
    return {
        "input": QueryInput(query="When did I last pay my Costco membership fee"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Costco")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Costco")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_083",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did I make my first mortgage payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_083():
    return {
        "input": QueryInput(query="When did I make my first mortgage payment?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="mortgage")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="mortgage")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_084",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount I have paid towards my mortgage payments?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_084():
    return {
        "input": QueryInput(query="What is the total amount I have paid towards my mortgage payments?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="mortgage")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="mortgage")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_085",
    agent_class=ProcessableEntityExtractionAgent,
    description="When is my next car insurance payment due to Geico?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_085():
    return {
        "input": QueryInput(query="When is my next car insurance payment due to Geico?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="car insurance"),
                Entity(type="merchant", value="Geico")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="insurance")},
                {"type": Exact(value="merchant"), "value": Exact(value="Geico")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_086",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount received from the DWP in the last 6 months including both fortnightly Wednesday...",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_086():
    return {
        "input": QueryInput(query="What is the total amount received from the DWP in the last 6 months including both fortnightly Wednesday payments and monthly Monday payments?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="DWP"),
                Entity(type="temporal", value="last 6 months"),
                Entity(type="temporal", value="Wednesday"),
                Entity(type="temporal", value="Monday")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="DWP")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")},
                {"type": Exact(value="temporal"), "value": Exact(value="Wednesday")},
                {"type": Exact(value="temporal"), "value": Exact(value="Monday")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_087",
    agent_class=ProcessableEntityExtractionAgent,
    description="How does my total savings in both my savings and checking accounts this year compare to last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_087():
    return {
        "input": QueryInput(query="How does my total savings in both my savings and checking accounts this year compare to last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings"),
                Entity(type="temporal", value="this year"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_088",
    agent_class=ProcessableEntityExtractionAgent,
    description="my cloth purchases",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_088():
    return {
        "input": QueryInput(query="my cloth purchases"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="cloth")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="cloth")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_089",
    agent_class=ProcessableEntityExtractionAgent,
    description="my earning in last 6 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_089():
    return {
        "input": QueryInput(query="my earning in last 6 months"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_090",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did I receive my Chb?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_090():
    return {
        "input": QueryInput(query="When did I receive my Chb?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_091",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my total spending at Amazon last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_091():
    return {
        "input": QueryInput(query="What was my total spending at Amazon last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_092",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much do I get in child benefits?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_092():
    return {
        "input": QueryInput(query="How much do I get in child benefits?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="child benefits")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Substring(value="child")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_093",
    agent_class=ProcessableEntityExtractionAgent,
    description="show the bills",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_093():
    return {
        "input": QueryInput(query="show the bills"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_094",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I send that money to X?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_094():
    return {
        "input": QueryInput(query="Did I send that money to X?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_095",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did John send me the 200 dollars they owed me?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_095():
    return {
        "input": QueryInput(query="When did John send me the 200 dollars they owed me?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="200 dollars")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="200 dollars")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_096",
    agent_class=ProcessableEntityExtractionAgent,
    description="did John pay me, if yes , how much",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_096():
    return {
        "input": QueryInput(query="\"did John pay me, if yes , how much\""),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_097",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my total electricity spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_097():
    return {
        "input": QueryInput(query="What was my total electricity spending in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="electricity"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="electricity")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_098",
    agent_class=ProcessableEntityExtractionAgent,
    description="how much refund did Adibas pay me",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_098():
    return {
        "input": QueryInput(query="how much refund did Adibas pay me"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Adibas")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Adibas")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_099",
    agent_class=ProcessableEntityExtractionAgent,
    description="how much money john helped me with",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_099():
    return {
        "input": QueryInput(query="how much money john helped me with"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_100",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the smallest transaction I have made to John since August?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_100():
    return {
        "input": QueryInput(query="What is the smallest transaction I have made to John since August?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="since August")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="since August")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_101",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my average monthly spending on groceries in 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_101():
    return {
        "input": QueryInput(query="What is my average monthly spending on groceries in 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_102",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total balance in my savings account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_102():
    return {
        "input": QueryInput(query="What is my total balance in my savings account?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_103",
    agent_class=ProcessableEntityExtractionAgent,
    description="my total depoists last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_103():
    return {
        "input": QueryInput(query="my total depoists last year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_104",
    agent_class=ProcessableEntityExtractionAgent,
    description="what cheque depoists I made?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_104():
    return {
        "input": QueryInput(query="what cheque depoists I made?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_105",
    agent_class=ProcessableEntityExtractionAgent,
    description="did I pay my tennis classes fee last month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_105():
    return {
        "input": QueryInput(query="did I pay my tennis classes fee last month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="sports"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="sports")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_106",
    agent_class=ProcessableEntityExtractionAgent,
    description="show my spend at swimming session in last 6 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_106():
    return {
        "input": QueryInput(query="show my spend at swimming session in last 6 months"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="sports"),
                Entity(type="temporal", value="last 6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="sports")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_107",
    agent_class=ProcessableEntityExtractionAgent,
    description="What days am I most likely to order a takeaway?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_107():
    return {
        "input": QueryInput(query="What days am I most likely to order a takeaway?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="takeaway")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="takeaway")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_108",
    agent_class=ProcessableEntityExtractionAgent,
    description="store I order most of my takeaways?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_108():
    return {
        "input": QueryInput(query="store I order most of my takeaways?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="takeaway")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="takeaway")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_109",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which stores did I order takeaway from on Mondays?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_109():
    return {
        "input": QueryInput(query="Which stores did I order takeaway from on Mondays?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="takeaway"),
                Entity(type="temporal", value="Monday")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="takeaway")},
                {"type": Exact(value="temporal"), "value": Exact(value="Monday")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_110",
    agent_class=ProcessableEntityExtractionAgent,
    description="show my top 3 recurring spending places in a month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_110():
    return {
        "input": QueryInput(query="show my top 3 recurring spending places in a month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_111",
    agent_class=ProcessableEntityExtractionAgent,
    description="total payements to supermarkets this vs last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_111():
    return {
        "input": QueryInput(query="total payements to supermarkets this vs last year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="this year"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_112",
    agent_class=ProcessableEntityExtractionAgent,
    description="total money transferred to my savings account this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_112():
    return {
        "input": QueryInput(query="total money transferred to my savings account this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_113",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times have I made purchases at Starbucks in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_113():
    return {
        "input": QueryInput(query="How many times have I made purchases at Starbucks in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Starbucks"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Starbucks")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_114",
    agent_class=ProcessableEntityExtractionAgent,
    description="In which categories did I exceed my budget last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_114():
    return {
        "input": QueryInput(query="In which categories did I exceed my budget last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="budget", value="budget"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_115",
    agent_class=ProcessableEntityExtractionAgent,
    description="Whats the damage this month on my spending?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_115():
    return {
        "input": QueryInput(query="Whats the damage this month on my spending?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_116",
    agent_class=ProcessableEntityExtractionAgent,
    description="my top 3 subscription services by spending",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_116():
    return {
        "input": QueryInput(query="my top 3 subscription services by spending"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="subscriptions")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="subscriptions")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_117",
    agent_class=ProcessableEntityExtractionAgent,
    description="At which merchant did I spend the most and during which time period in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_117():
    return {
        "input": QueryInput(query="At which merchant did I spend the most and during which time period in the last 6 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_118",
    agent_class=ProcessableEntityExtractionAgent,
    description="Why was my messages bill higher last month compared to August?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_118():
    return {
        "input": QueryInput(query="Why was my messages bill higher last month compared to August?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bills"),
                Entity(type="temporal", value="last month"),
                Entity(type="temporal", value="August")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")},
                {"type": Exact(value="temporal"), "value": Exact(value="August")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_119",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I spend more on dining out last month compared to this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_119():
    return {
        "input": QueryInput(query="Did I spend more on dining out last month compared to this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="dining out"),
                Entity(type="temporal", value="last month"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="dining out")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_120",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many transactions did I make last weekend?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_120():
    return {
        "input": QueryInput(query="How many transactions did I make last weekend?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last weekend")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last weekend")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_121",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I make any payments to Avis car hire in February this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_121():
    return {
        "input": QueryInput(query="Did I make any payments to Avis car hire in February this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Avis"),
                Entity(type="temporal", value="February"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Avis")},
                {"type": Exact(value="temporal"), "value": Exact(value="February")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_122",
    agent_class=ProcessableEntityExtractionAgent,
    description="Have there been any changes in the amounts paid to Netflix, Spotify, and Amazon through standing orders over the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_122():
    return {
        "input": QueryInput(query="Have there been any changes in the amounts paid to Netflix, Spotify, and Amazon through standing orders over the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Netflix"),
                Entity(type="merchant", value="Spotify"),
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Netflix")},
                {"type": Exact(value="merchant"), "value": Exact(value="Spotify")},
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_123",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I spent on my dog's vet bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_123():
    return {
        "input": QueryInput(query="How much have I spent on my dog's vet bills?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="vet")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="vet")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_124",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I spent on dog food in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_124():
    return {
        "input": QueryInput(query="How much have I spent on dog food in the last 6 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_125",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I spent at Apollo hospital this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_125():
    return {
        "input": QueryInput(query="How much have I spent at Apollo hospital this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="hospital"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="hospital")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_126",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was the amount of the last overdraft fee charged on my account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_126():
    return {
        "input": QueryInput(query="What was the amount of the last overdraft fee charged on my account?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_127",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount of my Amazon bill for next month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_127():
    return {
        "input": QueryInput(query="What is the total amount of my Amazon bill for next month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="next month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="next month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_128",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I spend more than 1000 dollars on medical bills in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_128():
    return {
        "input": QueryInput(query="Did I spend more than 1000 dollars on medical bills in the last 6 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="more than 1000 dollars"),
                Entity(type="category", value="medical"),
                Entity(type="temporal", value="last 6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Substring(value="1000 dollars")},
                {"type": Exact(value="category"), "value": Exact(value="medical")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_129",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending on travel in August and September 2025?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_129():
    return {
        "input": QueryInput(query="What is my total spending on travel in August and September 2025?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel"),
                Entity(type="temporal", value="August"),
                Entity(type="temporal", value="September"),
                Entity(type="temporal", value="2025")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")},
                {"type": Exact(value="temporal"), "value": Exact(value="August")},
                {"type": Exact(value="temporal"), "value": Exact(value="September")},
                {"type": Exact(value="temporal"), "value": Exact(value="2025")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_130",
    agent_class=ProcessableEntityExtractionAgent,
    description="Are there any rent refunds greater than 250 dollars this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_130():
    return {
        "input": QueryInput(query="Are there any rent refunds greater than 250 dollars this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="rent"),
                Entity(type="category", value="refunds"),
                Entity(type="amount", value="greater than 250 dollars"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="rent")},
                {"type": Exact(value="category"), "value": Exact(value="refunds")},
                {"type": Exact(value="amount"), "value": Substring(value="250 dollars")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_131",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my average order value for takeaway spending this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_131():
    return {
        "input": QueryInput(query="What is my average order value for takeaway spending this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="takeaway"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="takeaway")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_132",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount I have spent on my subscriptions in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_132():
    return {
        "input": QueryInput(query="What is the total amount I have spent on my subscriptions in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="subscriptions"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="subscriptions")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_133",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you break down my total spend of 1200 dollars in Spain last month by category or merchant?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_133():
    return {
        "input": QueryInput(query="Can you break down my total spend of 1200 dollars in Spain last month by category or merchant?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="1200 dollars"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="1200 dollars")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_134",
    agent_class=ProcessableEntityExtractionAgent,
    description="how can i get my budget back on track",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_134():
    return {
        "input": QueryInput(query="how can i get my budget back on track"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="budget", value="budget")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="budget"), "value": Exact(value="budget")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_135",
    agent_class=ProcessableEntityExtractionAgent,
    description="What one time payments do I have coming up?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_135():
    return {
        "input": QueryInput(query="What one time payments do I have coming up?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_136",
    agent_class=ProcessableEntityExtractionAgent,
    description="Are there any other unusual transactions in my account from last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_136():
    return {
        "input": QueryInput(query="Are there any other unusual transactions in my account from last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_137",
    agent_class=ProcessableEntityExtractionAgent,
    description="Were there any refunds in my transactions from last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_137():
    return {
        "input": QueryInput(query="Were there any refunds in my transactions from last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="refunds"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="refunds")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_138",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend on food in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_138():
    return {
        "input": QueryInput(query="How much did I spend on food in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="food"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="food")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_139",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much money will I have left at the end of the month based on my current balance expected income and upcoming expenses?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_139():
    return {
        "input": QueryInput(query="How much money will I have left at the end of the month based on my current balance expected income and upcoming expenses?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="end of the month"),
                Entity(type="category", value="income")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="end of the month")},
                {"type": Exact(value="category"), "value": Exact(value="income")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_140",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I spent on groceries this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_140():
    return {
        "input": QueryInput(query="How much have I spent on groceries this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_141",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend at Walmart on groceries?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_141():
    return {
        "input": QueryInput(query="How much did I spend at Walmart on groceries?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Walmart"),
                Entity(type="category", value="groceries")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Walmart")},
                {"type": Exact(value="category"), "value": Exact(value="groceries")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_142",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my current bank account balance?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_142():
    return {
        "input": QueryInput(query="What is my current bank account balance?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_143",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_143():
    return {
        "input": QueryInput(query="What is my total spending this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_144",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend at McDonalds in May?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_144():
    return {
        "input": QueryInput(query="How much did I spend at McDonalds in May?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="McDonald's"),
                Entity(type="temporal", value="May")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="McDonald's")},
                {"type": Exact(value="temporal"), "value": Exact(value="May")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_145",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I pay for my utility bill in January?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_145():
    return {
        "input": QueryInput(query="How much did I pay for my utility bill in January?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="utilities"),
                Entity(type="temporal", value="January")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="utilities")},
                {"type": Exact(value="temporal"), "value": Exact(value="January")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_146",
    agent_class=ProcessableEntityExtractionAgent,
    description="Are there any refunds expected in my predicted expenses for next month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_146():
    return {
        "input": QueryInput(query="Are there any refunds expected in my predicted expenses for next month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="refunds"),
                Entity(type="temporal", value="next month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="refunds")},
                {"type": Exact(value="temporal"), "value": Exact(value="next month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_147",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total estimated spending for groceries dining out and online shopping in the next 7 days?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_147():
    return {
        "input": QueryInput(query="What is my total estimated spending for groceries dining out and online shopping in the next 7 days?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="category", value="dining out"),
                Entity(type="category", value="shopping"),
                Entity(type="temporal", value="next 7 days")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="category"), "value": Exact(value="dining out")},
                {"type": Exact(value="category"), "value": Exact(value="shopping")},
                {"type": Exact(value="temporal"), "value": Exact(value="next 7 days")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_148",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my forecasted spending on travel for the next 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_148():
    return {
        "input": QueryInput(query="What is my forecasted spending on travel for the next 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel"),
                Entity(type="temporal", value="next 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")},
                {"type": Exact(value="temporal"), "value": Exact(value="next 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_149",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my estimated yearly spending on Amazon based on the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_149():
    return {
        "input": QueryInput(query="What is my estimated yearly spending on Amazon based on the last 6 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="last 6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_150",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you track my spending on food and bills for this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_150():
    return {
        "input": QueryInput(query="Can you track my spending on food and bills for this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="food"),
                Entity(type="category", value="bills"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="food")},
                {"type": Exact(value="category"), "value": Exact(value="bills")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_151",
    agent_class=ProcessableEntityExtractionAgent,
    description="How would cutting down on eating out affect my ability to save £500 this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_151():
    return {
        "input": QueryInput(query="How would cutting down on eating out affect my ability to save £500 this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="eating out"),
                Entity(type="amount", value="£500"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="eating out")},
                {"type": Exact(value="amount"), "value": Exact(value="£500")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_152",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend at The Italian Place last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_152():
    return {
        "input": QueryInput(query="How much did I spend at The Italian Place last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="The Italian Place"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="The Italian Place")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_153",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many transactions have I made this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_153():
    return {
        "input": QueryInput(query="How many transactions have I made this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_154",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much would I save if I reduce my travel expenses by 20 percent in the last 6 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_154():
    return {
        "input": QueryInput(query="How much would I save if I reduce my travel expenses by 20 percent in the last 6 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel"),
                Entity(type="temporal", value="last 6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_155",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my biggest expense last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_155():
    return {
        "input": QueryInput(query="What was my biggest expense last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_156",
    agent_class=ProcessableEntityExtractionAgent,
    description="How can I avoid early withdrawal fees on my savings account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_156():
    return {
        "input": QueryInput(query="How can I avoid early withdrawal fees on my savings account?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_157",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much money will I have left each month after accounting for my car loan payment, travel spending, and monthly bills?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_157():
    return {
        "input": QueryInput(query="How much money will I have left each month after accounting for my car loan payment, travel spending, and monthly bills?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel"),
                Entity(type="category", value="bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")},
                {"type": Exact(value="category"), "value": Exact(value="bills")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_158",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total interest I will pay if I pay an extra 400 pounds monthly on my 50000 pound loan at 4 percent interest over 10 years?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_158():
    return {
        "input": QueryInput(query="What is the total interest I will pay if I pay an extra 400 pounds monthly on my 50000 pound loan at 4 percent interest over 10 years?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="400 pounds"),
                Entity(type="amount", value="50000 pound")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="400 pounds")},
                {"type": Exact(value="amount"), "value": Exact(value="50000 pound")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_159",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend at Starbucks in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_159():
    return {
        "input": QueryInput(query="How much did I spend at Starbucks in the last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Starbucks"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Starbucks")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_160",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much total interest will I pay if I make monthly payments of 100 pounds on my 3000 pound credit card balance with an 18 percent APR?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_160():
    return {
        "input": QueryInput(query="How much total interest will I pay if I make monthly payments of 100 pounds on my 3000 pound credit card balance with an 18 percent APR?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="100 pounds"),
                Entity(type="amount", value="3000 pound")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="100 pounds")},
                {"type": Exact(value="amount"), "value": Exact(value="3000 pound")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_161",
    agent_class=ProcessableEntityExtractionAgent,
    description="What will happen to my ability to afford a £250 monthly direct debit for a new car if my income decreases?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_161():
    return {
        "input": QueryInput(query="What will happen to my ability to afford a £250 monthly direct debit for a new car if my income decreases?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="£250"),
                Entity(type="category", value="income")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="£250")},
                {"type": Exact(value="category"), "value": Exact(value="income")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_162",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount I will pay over 5 years for a £25000 loan with a 6.9 percent interest rate if I pay an extra £100 each month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_162():
    return {
        "input": QueryInput(query="What is the total amount I will pay over 5 years for a £25000 loan with a 6.9 percent interest rate if I pay an extra £100 each month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="£25000"),
                Entity(type="amount", value="£100")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="£25000")},
                {"type": Exact(value="amount"), "value": Exact(value="£100")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_163",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much do I spend monthly on Spotify?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_163():
    return {
        "input": QueryInput(query="How much do I spend monthly on Spotify?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Spotify")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Spotify")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_164",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the exact amount I spent on Netflix in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_164():
    return {
        "input": QueryInput(query="What is the exact amount I spent on Netflix in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Netflix"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Netflix")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_165",
    agent_class=ProcessableEntityExtractionAgent,
    description="How do I start investing in index funds?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_165():
    return {
        "input": QueryInput(query="How do I start investing in index funds?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_166",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much should I allocate for travel and dining out each month based on my current budget and savings goal?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_166():
    return {
        "input": QueryInput(query="How much should I allocate for travel and dining out each month based on my current budget and savings goal?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel"),
                Entity(type="category", value="dining out"),
                Entity(type="budget", value="budget"),
                Entity(type="category", value="savings")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")},
                {"type": Exact(value="category"), "value": Exact(value="dining out")},
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="category"), "value": Exact(value="savings")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_167",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I save in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_167():
    return {
        "input": QueryInput(query="How much did I save in 2023?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_168",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you help me set a budget for dining out and groceries for next month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_168():
    return {
        "input": QueryInput(query="Can you help me set a budget for dining out and groceries for next month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="budget", value="budget"),
                Entity(type="category", value="dining out"),
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="next month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="category"), "value": Exact(value="dining out")},
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="next month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_169",
    agent_class=ProcessableEntityExtractionAgent,
    description="When will my delayed Pension Credit payment of 500 dollars be credited to my bank account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_169():
    return {
        "input": QueryInput(query="When will my delayed Pension Credit payment of 500 dollars be credited to my bank account?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="pension"),
                Entity(type="amount", value="500 dollars")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="pension")},
                {"type": Exact(value="amount"), "value": Exact(value="500 dollars")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_170",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was the $50 Amazon transaction on the 5th of this month for?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_170():
    return {
        "input": QueryInput(query="What was the $50 Amazon transaction on the 5th of this month for?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="$50"),
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="5th of this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="$50")},
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="5th of this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_171",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_171():
    return {
        "input": QueryInput(query="What is my total spending in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_172",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I paid in interest on my credit card this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_172():
    return {
        "input": QueryInput(query="How much have I paid in interest on my credit card this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_173",
    agent_class=ProcessableEntityExtractionAgent,
    description="If I cancel my streaming subscriptions how much would I save monthly",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_173():
    return {
        "input": QueryInput(query="If I cancel my streaming subscriptions how much would I save monthly"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="streaming")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="streaming")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_174",
    agent_class=ProcessableEntityExtractionAgent,
    description="Was my last payment to John Smith a regular or recurring payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_174():
    return {
        "input": QueryInput(query="Was my last payment to John Smith a regular or recurring payment?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_175",
    agent_class=ProcessableEntityExtractionAgent,
    description="Has John Smith paid me the 200 dollars that was due last week?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_175():
    return {
        "input": QueryInput(query="Has John Smith paid me the 200 dollars that was due last week?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="200 dollars"),
                Entity(type="temporal", value="last week")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Exact(value="200 dollars")},
                {"type": Exact(value="temporal"), "value": Exact(value="last week")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_176",
    agent_class=ProcessableEntityExtractionAgent,
    description="When is the next subscription payment due?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_176():
    return {
        "input": QueryInput(query="When is the next subscription payment due?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="subscriptions")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="subscriptions")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_177",
    agent_class=ProcessableEntityExtractionAgent,
    description="What are my roundup savings for the last two months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_177():
    return {
        "input": QueryInput(query="What are my roundup savings for the last two months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings"),
                Entity(type="temporal", value="last two months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")},
                {"type": Exact(value="temporal"), "value": Exact(value="last two months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_178",
    agent_class=ProcessableEntityExtractionAgent,
    description="Why did I pay less credit card interest in 2023 compared to 2022?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_178():
    return {
        "input": QueryInput(query="Why did I pay less credit card interest in 2023 compared to 2022?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="2023"),
                Entity(type="temporal", value="2022")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="2023")},
                {"type": Exact(value="temporal"), "value": Exact(value="2022")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_179",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much more do I need to add to my current account balance to qualify for the discount on the account fee?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_179():
    return {
        "input": QueryInput(query="How much more do I need to add to my current account balance to qualify for the discount on the account fee?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_180",
    agent_class=ProcessableEntityExtractionAgent,
    description="What are my total charges including fees and interest in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_180():
    return {
        "input": QueryInput(query="What are my total charges including fees and interest in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_181",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much money do I have left in my shopping budget for this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_181():
    return {
        "input": QueryInput(query="How much money do I have left in my shopping budget for this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="shopping"),
                Entity(type="budget", value="budget"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="shopping")},
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_182",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend on Amazon in 2023 and 2024?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_182():
    return {
        "input": QueryInput(query="How much did I spend on Amazon in 2023 and 2024?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="2023"),
                Entity(type="temporal", value="2024")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")},
                {"type": Exact(value="temporal"), "value": Exact(value="2024")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_183",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_183():
    return {
        "input": QueryInput(query="What is my total spending in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_184",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my smallest grocery transaction in the last 3 months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_184():
    return {
        "input": QueryInput(query="What is my smallest grocery transaction in the last 3 months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="groceries"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="groceries")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_185",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_185():
    return {
        "input": QueryInput(query="What is my total spending in the last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_186",
    agent_class=ProcessableEntityExtractionAgent,
    description="my total spend in travel in 6 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_186():
    return {
        "input": QueryInput(query="my total spend in travel in 6 months"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel"),
                Entity(type="temporal", value="6 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")},
                {"type": Exact(value="temporal"), "value": Exact(value="6 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_187",
    agent_class=ProcessableEntityExtractionAgent,
    description="show my travel cost",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_187():
    return {
        "input": QueryInput(query="show my travel cost"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="travel")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="travel")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_188",
    agent_class=ProcessableEntityExtractionAgent,
    description="show bill",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_188():
    return {
        "input": QueryInput(query="show bill"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_189",
    agent_class=ProcessableEntityExtractionAgent,
    description="spend mrch and feb",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_189():
    return {
        "input": QueryInput(query="spend mrch and feb"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="March"),
                Entity(type="temporal", value="February")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="March")},
                {"type": Exact(value="temporal"), "value": Exact(value="February")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_190",
    agent_class=ProcessableEntityExtractionAgent,
    description="what refunds",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_190():
    return {
        "input": QueryInput(query="what refunds"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="refunds")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="refunds")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_191",
    agent_class=ProcessableEntityExtractionAgent,
    description="spend in nike and adidas",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_191():
    return {
        "input": QueryInput(query="spend in nike and adidas"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Nike"),
                Entity(type="merchant", value="Adidas")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Nike")},
                {"type": Exact(value="merchant"), "value": Exact(value="Adidas")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_192",
    agent_class=ProcessableEntityExtractionAgent,
    description="What did I spend on bills and travel?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_192():
    return {
        "input": QueryInput(query="What did I spend on bills and travel?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bills"),
                Entity(type="category", value="travel")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills")},
                {"type": Exact(value="category"), "value": Exact(value="travel")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_193",
    agent_class=ProcessableEntityExtractionAgent,
    description="total bills",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_193():
    return {
        "input": QueryInput(query="total bills"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bills")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_194",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending in the last six months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_194():
    return {
        "input": QueryInput(query="What is my total spending in the last six months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last six months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last six months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_195",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total spending across all merchants in the last six months?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_195():
    return {
        "input": QueryInput(query="What is my total spending across all merchants in the last six months?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last six months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last six months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_196",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my total loan payment in the last 2 years?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_196():
    return {
        "input": QueryInput(query="What is my total loan payment in the last 2 years?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 2 years")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 2 years")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_197",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the total amount I have paid towards my loans in the last 2 years?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_197():
    return {
        "input": QueryInput(query="What is the total amount I have paid towards my loans in the last 2 years?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last 2 years")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last 2 years")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_198",
    agent_class=ProcessableEntityExtractionAgent,
    description="spending in bus tickets?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_198():
    return {
        "input": QueryInput(query="spending in bus tickets?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bus")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bus")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_199",
    agent_class=ProcessableEntityExtractionAgent,
    description="spending in bus tickets in the last 3 months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_199():
    return {
        "input": QueryInput(query="spending in bus tickets in the last 3 months"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="bus"),
                Entity(type="temporal", value="last 3 months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bus")},
                {"type": Exact(value="temporal"), "value": Exact(value="last 3 months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_200",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many transactions did I make in Scotland versus England in the last month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_200():
    return {
        "input": QueryInput(query="How many transactions did I make in Scotland versus England in the last month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_201",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much do I have left at the end of each month in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_201():
    return {
        "input": QueryInput(query="How much do I have left at the end of each month in 2023?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_202",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you show me a summary of my recent transactions?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_202():
    return {
        "input": QueryInput(query="Can you show me a summary of my recent transactions?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_203",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you show me a breakdown of my expenses for the past three months",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_203():
    return {
        "input": QueryInput(query="Can you show me a breakdown of my expenses for the past three months"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="past three months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="past three months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_204",
    agent_class=ProcessableEntityExtractionAgent,
    description="Can you show me a list of my biggest transactions this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_204():
    return {
        "input": QueryInput(query="Can you show me a list of my biggest transactions this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_205",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many times has my account balance dropped below 2000 pounds in the last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_205():
    return {
        "input": QueryInput(query="How many times has my account balance dropped below 2000 pounds in the last year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="amount", value="below 2000 pounds"),
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="amount"), "value": Substring(value="2000 pounds")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_206",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the trend of my monthly spending on Entertainment merchant category in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_206():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending on Entertainment merchant category in 2023?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="entertainment"),
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="entertainment")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_207",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the correlation between my account balance and my total monthly spending",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_207():
    return {
        "input": QueryInput(query="What is the correlation between my account balance and my total monthly spending"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_208",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the month over month growth rate of my spending in each merchant subcategory",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_208():
    return {
        "input": QueryInput(query="What is the month over month growth rate of my spending in each merchant subcategory"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_209",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the percentage of my total spending that each merchant category represents and how has this percentage changed month over month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_209():
    return {
        "input": QueryInput(query="What is the percentage of my total spending that each merchant category represents and how has this percentage changed month over month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_210",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the trend of my monthly spending in each merchant category over the past year and how does this compare to the trend of my overall monthly spending",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_210():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending in each merchant category over the past year and how does this compare to the trend of my overall monthly spending"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="past year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="past year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_211",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my account balance at the end of 2023 and how much did I spend on online shopping?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_211():
    return {
        "input": QueryInput(query="What was my account balance at the end of 2023 and how much did I spend on online shopping?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="end of 2023"),
                Entity(type="category", value="shopping")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="end of 2023")},
                {"type": Exact(value="category"), "value": Exact(value="shopping")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_212",
    agent_class=ProcessableEntityExtractionAgent,
    description="Am I spending more or less a month than I did last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_212():
    return {
        "input": QueryInput(query="Am I spending more or less a month than I did last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_213",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my biggest outgoing?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_213():
    return {
        "input": QueryInput(query="What is my biggest outgoing?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_214",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many days was I overdrawn last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_214():
    return {
        "input": QueryInput(query="How many days was I overdrawn last year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_215",
    agent_class=ProcessableEntityExtractionAgent,
    description="What percentage of my total expenses was spent on subscriptions this year and how has that changed each month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_215():
    return {
        "input": QueryInput(query="What percentage of my total expenses was spent on subscriptions this year and how has that changed each month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="subscriptions"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="subscriptions")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_216",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my total spending on food last year compared to this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_216():
    return {
        "input": QueryInput(query="What was my total spending on food last year compared to this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="food"),
                Entity(type="temporal", value="last year"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="food")},
                {"type": Exact(value="temporal"), "value": Exact(value="last year")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_217",
    agent_class=ProcessableEntityExtractionAgent,
    description="When is my car insurance due for renewal?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_217():
    return {
        "input": QueryInput(query="When is my car insurance due for renewal?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="insurance")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="insurance")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_218",
    agent_class=ProcessableEntityExtractionAgent,
    description="Details of fortnightly Wednesday payments also monthly Monday payments from the DWP",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_218():
    return {
        "input": QueryInput(query="Details of fortnightly Wednesday payments also monthly Monday payments from the DWP"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="Wednesday"),
                Entity(type="temporal", value="Monday")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="Wednesday")},
                {"type": Exact(value="temporal"), "value": Exact(value="Monday")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_219",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I saved this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_219():
    return {
        "input": QueryInput(query="How much have I saved this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_220",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I send that money to X",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_220():
    return {
        "input": QueryInput(query="Did I send that money to X"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_221",
    agent_class=ProcessableEntityExtractionAgent,
    description="Has X sent me the money they owe me",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_221():
    return {
        "input": QueryInput(query="Has X sent me the money they owe me"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_222",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much money have I sent to John since August?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_222():
    return {
        "input": QueryInput(query="How much money have I sent to John since August?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="since August")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="since August")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_223",
    agent_class=ProcessableEntityExtractionAgent,
    description="I have got a payment to aspire teaching can you tell me what this is please",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_223():
    return {
        "input": QueryInput(query="I have got a payment to aspire teaching can you tell me what this is please"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_224",
    agent_class=ProcessableEntityExtractionAgent,
    description="Where is most of my cash going?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_224():
    return {
        "input": QueryInput(query="Where is most of my cash going?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_225",
    agent_class=ProcessableEntityExtractionAgent,
    description="Am I spending more than usual?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_225():
    return {
        "input": QueryInput(query="Am I spending more than usual?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_226",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I stay within my budget?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_226():
    return {
        "input": QueryInput(query="Did I stay within my budget?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="budget", value="budget")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="budget"), "value": Exact(value="budget")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_227",
    agent_class=ProcessableEntityExtractionAgent,
    description="Was there a spike in spending recently?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_227():
    return {
        "input": QueryInput(query="Was there a spike in spending recently?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_228",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend when I was out last weekend",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_228():
    return {
        "input": QueryInput(query="How much did I spend when I was out last weekend"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last weekend")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last weekend")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_229",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much was my last insurance payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_229():
    return {
        "input": QueryInput(query="How much was my last insurance payment?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="insurance")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="insurance")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_230",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I save through round ups last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_230():
    return {
        "input": QueryInput(query="How much did I save through round ups last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_231",
    agent_class=ProcessableEntityExtractionAgent,
    description="Did I pay any overdraft fees this year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_231():
    return {
        "input": QueryInput(query="Did I pay any overdraft fees this year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_232",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much do I typically spend between 8pm and 1am on Fridays?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_232():
    return {
        "input": QueryInput(query="How much do I typically spend between 8pm and 1am on Fridays?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="Friday")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="Friday")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_233",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is my budget for Groceries?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_233():
    return {
        "input": QueryInput(query="What is my budget for Groceries?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="budget", value="budget"),
                Entity(type="category", value="groceries")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="category"), "value": Exact(value="groceries")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_234",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I spent at Amazon in the last month",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_234():
    return {
        "input": QueryInput(query="How much have I spent at Amazon in the last month"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="merchant", value="Amazon"),
                Entity(type="temporal", value="last month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="merchant"), "value": Exact(value="Amazon")},
                {"type": Exact(value="temporal"), "value": Exact(value="last month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_235",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much did I spend on my night out last night",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_235():
    return {
        "input": QueryInput(query="How much did I spend on my night out last night"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last night")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last night")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_236",
    agent_class=ProcessableEntityExtractionAgent,
    description="What was my total spend whilst on holiday",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_236():
    return {
        "input": QueryInput(query="What was my total spend whilst on holiday"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_237",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many roundups did I save last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_237():
    return {
        "input": QueryInput(query="How many roundups did I save last year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_238",
    agent_class=ProcessableEntityExtractionAgent,
    description="What's the fee for my account?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_238():
    return {
        "input": QueryInput(query="What's the fee for my account?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_239",
    agent_class=ProcessableEntityExtractionAgent,
    description="Am I on track to stay within my shopping budget this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_239():
    return {
        "input": QueryInput(query="Am I on track to stay within my shopping budget this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="shopping"),
                Entity(type="budget", value="budget"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="shopping")},
                {"type": Exact(value="budget"), "value": Exact(value="budget")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_240",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much money did I receive from my savings account",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_240():
    return {
        "input": QueryInput(query="How much money did I receive from my savings account"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_241",
    agent_class=ProcessableEntityExtractionAgent,
    description="what was my account balance at the end of 2023, and how much did i spend on online shopping?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_241():
    return {
        "input": QueryInput(query="what was my account balance at the end of 2023, and how much did i spend on online shopping?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="end of 2023"),
                Entity(type="category", value="shopping")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="end of 2023")},
                {"type": Exact(value="category"), "value": Exact(value="shopping")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_242",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the trend of my monthly spending on 'Entertainment' merchant category in 2023?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_242():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending on 'Entertainment' merchant category in 2023?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="entertainment"),
                Entity(type="temporal", value="2023")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="entertainment")},
                {"type": Exact(value="temporal"), "value": Exact(value="2023")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_243",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the correlation between my account balance and my total monthly spending?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_243():
    return {
        "input": QueryInput(query="What is the correlation between my account balance and my total monthly spending?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_244",
    agent_class=ProcessableEntityExtractionAgent,
    description="Which merchant subcategories have seen the most significant increase in my spending over the past year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_244():
    return {
        "input": QueryInput(query="Which merchant subcategories have seen the most significant increase in my spending over the past year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="past year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="past year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_245",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the month-over-month growth rate of my spending in each merchant subcategory?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_245():
    return {
        "input": QueryInput(query="What is the month-over-month growth rate of my spending in each merchant subcategory?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_246",
    agent_class=ProcessableEntityExtractionAgent,
    description="How does my average daily spending in each merchant category compare to the average daily spending in the previous month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_246():
    return {
        "input": QueryInput(query="How does my average daily spending in each merchant category compare to the average daily spending in the previous month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="previous month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="previous month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_247",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the percentage of my total spending that each merchant category represents, and how has this percentage changed month-over-month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_247():
    return {
        "input": QueryInput(query="What is the percentage of my total spending that each merchant category represents, and how has this percentage changed month-over-month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_248",
    agent_class=ProcessableEntityExtractionAgent,
    description="What is the trend of my monthly spending in each merchant category over the past year, and how does this compare to the trend of my overall monthly spending?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_248():
    return {
        "input": QueryInput(query="What is the trend of my monthly spending in each merchant category over the past year, and how does this compare to the trend of my overall monthly spending?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="past year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="past year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_249",
    agent_class=ProcessableEntityExtractionAgent,
    description="What are the top 3 merchant names where my spending has decreased the most in the last six months, and what is the percentage decrease for each?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_249():
    return {
        "input": QueryInput(query="What are the top 3 merchant names where my spending has decreased the most in the last six months, and what is the percentage decrease for each?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last six months")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last six months")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_250",
    agent_class=ProcessableEntityExtractionAgent,
    description="What percentage of my total expenses was spent on subscriptions this year, and how has that changed monthly?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_250():
    return {
        "input": QueryInput(query="What percentage of my total expenses was spent on subscriptions this year, and how has that changed monthly?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="subscriptions"),
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="subscriptions")},
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_251",
    agent_class=ProcessableEntityExtractionAgent,
    description="When did I make my first mortgage payment?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_251():
    return {
        "input": QueryInput(query="When did I make my first mortgage payment?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="mortgage")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="mortgage")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_252",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much have I saved this year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_252():
    return {
        "input": QueryInput(query="How much have I saved this year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="this year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="this year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_253",
    agent_class=ProcessableEntityExtractionAgent,
    description="When do I get my Chb?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_253():
    return {
        "input": QueryInput(query="When do I get my Chb?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_254",
    agent_class=ProcessableEntityExtractionAgent,
    description="What days am I most likely to order a takeaway?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_254():
    return {
        "input": QueryInput(query="What days am I most likely to order a takeaway?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="takeaway")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="takeaway")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_255",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much money  have I transferred to my savings account this month?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_255():
    return {
        "input": QueryInput(query="How much money  have I transferred to my savings account this month?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="category", value="savings"),
                Entity(type="temporal", value="this month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="savings")},
                {"type": Exact(value="temporal"), "value": Exact(value="this month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_256",
    agent_class=ProcessableEntityExtractionAgent,
    description="Am I spending more than usual?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_256():
    return {
        "input": QueryInput(query="Am I spending more than usual?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_257",
    agent_class=ProcessableEntityExtractionAgent,
    description="How much round ups did I save last year?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_257():
    return {
        "input": QueryInput(query="How much round ups did I save last year?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_258",
    agent_class=ProcessableEntityExtractionAgent,
    description="Show me a breakdown of next month's predicted expenses by category.",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_258():
    return {
        "input": QueryInput(query="Show me a breakdown of next month's predicted expenses by category."),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="next month")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="next month")}
            ])
        }
    }


@eval_case(
    name="predicted_intent_259",
    agent_class=ProcessableEntityExtractionAgent,
    description="When was my last payment to John Smith?",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_259():
    return {
        "input": QueryInput(query="When was my last payment to John Smith?"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[]
        ),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="predicted_intent_260",
    agent_class=ProcessableEntityExtractionAgent,
    description="How many roundups did I save last year",
    tags=["predicted_user_intent"]
)
def eval_predicted_intent_260():
    return {
        "input": QueryInput(query="How many roundups did I save last year"),
        "expected": ProcessableEntityExtractionOutput(
            entities=[
                Entity(type="temporal", value="last year")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="temporal"), "value": Exact(value="last year")}
            ])
        }
    }