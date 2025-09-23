"""
Evaluation cases for CategoryNormalisationAgent using decorator pattern.
"""

from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact
from src.workflow_nodes.query_preprocessing.category_normalisation_agent import CategoryNormalisationAgent
from src.models.category_normalisation_models import (
    CategoryNormalisationInput,
    CategoryNormalisationOutput,
    CategoryEntity,
    NormalisedCategoryEntity
)


# ========== Tier 1 Cases (3) ==========

@eval_case(
    name="tier1_expenses",
    agent_class=CategoryNormalisationAgent,
    description="Top-level expenses category",
    tags=["tier1", "expenses", "dev_cases"]
)
def eval_tier1_expenses():
    return {
        "input": CategoryNormalisationInput(
            query="Show me all my spending last year",
            entities=[CategoryEntity(type="category", value="spending")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="spending",
                canon="expenses"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="spending"), "canon": Exact(value="expenses")}
            ])
        }
    }


@eval_case(
    name="tier1_income",
    agent_class=CategoryNormalisationAgent,
    description="Top-level income category",
    tags=["tier1", "income", "dev_cases"]
)
def eval_tier1_income():
    return {
        "input": CategoryNormalisationInput(
            query="Total earnings this year",
            entities=[CategoryEntity(type="category", value="earnings")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="earnings",
                canon="income"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="earnings"), "canon": Exact(value="income")}
            ])
        }
    }


@eval_case(
    name="tier1_transfers",
    agent_class=CategoryNormalisationAgent,
    description="Top-level transfers category",
    tags=["tier1", "transfers", "dev_cases"]
)
def eval_tier1_transfers():
    return {
        "input": CategoryNormalisationInput(
            query="Show all money transfers",
            entities=[CategoryEntity(type="category", value="money transfers")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="money transfers",
                canon="transfers"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="money transfers"), "canon": Exact(value="transfers")}
            ])
        }
    }


# ========== Tier 2 Cases (7) ==========

@eval_case(
    name="tier2_bills",
    agent_class=CategoryNormalisationAgent,
    description="Generic bills category",
    tags=["tier2", "bills", "dev_cases"]
)
def eval_tier2_bills():
    return {
        "input": CategoryNormalisationInput(
            query="Show me my monthly bills",
            entities=[CategoryEntity(type="category", value="monthly bills")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="monthly bills",
                canon="expenses:bills"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="monthly bills"), "canon": Exact(value="expenses:bills")}
            ])
        }
    }


@eval_case(
    name="tier2_eating_out",
    agent_class=CategoryNormalisationAgent,
    description="Generic dining category",
    tags=["tier2", "eating_out", "dev_cases"]
)
def eval_tier2_eating_out():
    return {
        "input": CategoryNormalisationInput(
            query="How much on dining last month?",
            entities=[CategoryEntity(type="category", value="dining")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="dining",
                canon="expenses:eating-out"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="dining"), "canon": Exact(value="expenses:eating-out")}
            ])
        }
    }


@eval_case(
    name="tier2_entertainment",
    agent_class=CategoryNormalisationAgent,
    description="Generic fun & leisure category",
    tags=["tier2", "entertainment", "dev_cases"]
)
def eval_tier2_entertainment():
    return {
        "input": CategoryNormalisationInput(
            query="Entertainment spending this year",
            entities=[CategoryEntity(type="category", value="entertainment")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="entertainment",
                canon="expenses:entertainment"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="entertainment"), "canon": Exact(value="expenses:entertainment")}
            ])
        }
    }


@eval_case(
    name="tier2_transport",
    agent_class=CategoryNormalisationAgent,
    description="Generic transport category",
    tags=["tier2", "transport", "dev_cases"]
)
def eval_tier2_transport():
    return {
        "input": CategoryNormalisationInput(
            query="Transportation costs last quarter",
            entities=[CategoryEntity(type="category", value="transportation")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="transportation",
                canon="expenses:transport"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="transportation"), "canon": Exact(value="expenses:transport")}
            ])
        }
    }


@eval_case(
    name="tier2_shopping",
    agent_class=CategoryNormalisationAgent,
    description="Generic shopping category",
    tags=["tier2", "shopping", "dev_cases"]
)
def eval_tier2_shopping():
    return {
        "input": CategoryNormalisationInput(
            query="General shopping expenses",
            entities=[CategoryEntity(type="category", value="shopping")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="shopping",
                canon="expenses:shopping"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="shopping"), "canon": Exact(value="expenses:shopping")}
            ])
        }
    }


@eval_case(
    name="tier2_wellness",
    agent_class=CategoryNormalisationAgent,
    description="Generic health & beauty category",
    tags=["tier2", "wellness", "dev_cases"]
)
def eval_tier2_wellness():
    return {
        "input": CategoryNormalisationInput(
            query="Health and beauty expenses",
            entities=[CategoryEntity(type="category", value="health and beauty")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="health and beauty",
                canon="expenses:wellness"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="health and beauty"), "canon": Exact(value="expenses:wellness")}
            ])
        }
    }


@eval_case(
    name="tier2_income_salary",
    agent_class=CategoryNormalisationAgent,
    description="Salary income category",
    tags=["tier2", "income", "dev_cases"]
)
def eval_tier2_income_salary():
    return {
        "input": CategoryNormalisationInput(
            query="When did I get my wages?",
            entities=[CategoryEntity(type="category", value="wages")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="wages",
                canon="income:salary"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="wages"), "canon": Exact(value="income:salary")}
            ])
        }
    }


# ========== Tier 3 Cases (15) ==========

@eval_case(
    name="tier3_mortgage",
    agent_class=CategoryNormalisationAgent,
    description="Specific mortgage category",
    tags=["tier3", "bills", "dev_cases"]
)
def eval_tier3_mortgage():
    return {
        "input": CategoryNormalisationInput(
            query="How much is my home loan payment?",
            entities=[CategoryEntity(type="category", value="home loan")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="home loan",
                canon="expenses:bills.mortgage"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="home loan"), "canon": Exact(value="expenses:bills.mortgage")}
            ])
        }
    }


@eval_case(
    name="tier3_groceries_supermarket",
    agent_class=CategoryNormalisationAgent,
    description="Food shopping to supermarkets",
    tags=["tier3", "groceries", "dev_cases"]
)
def eval_tier3_groceries_supermarket():
    return {
        "input": CategoryNormalisationInput(
            query="Total spent on food shopping",
            entities=[CategoryEntity(type="category", value="food shopping")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="food shopping",
                canon="expenses:groceries.supermarkets"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="food shopping"), "canon": Exact(value="expenses:groceries.supermarkets")}
            ])
        }
    }


@eval_case(
    name="tier3_electricity",
    agent_class=CategoryNormalisationAgent,
    description="Electricity to energy providers",
    tags=["tier3", "bills", "utilities", "dev_cases"]
)
def eval_tier3_electricity():
    return {
        "input": CategoryNormalisationInput(
            query="My power bills for 2024",
            entities=[CategoryEntity(type="category", value="power bills")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="power bills",
                canon="expenses:bills.energy-providers"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="power bills"), "canon": Exact(value="expenses:bills.energy-providers")}
            ])
        }
    }


@eval_case(
    name="tier3_coffee_shops",
    agent_class=CategoryNormalisationAgent,
    description="Coffee shop spending",
    tags=["tier3", "eating_out", "dev_cases"]
)
def eval_tier3_coffee_shops():
    return {
        "input": CategoryNormalisationInput(
            query="Amount at Starbucks and Costa",
            entities=[CategoryEntity(type="category", value="Starbucks and Costa")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="Starbucks and Costa",
                canon="expenses:eating-out.coffee"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="Starbucks and Costa"), "canon": Exact(value="expenses:eating-out.coffee")}
            ])
        }
    }


@eval_case(
    name="tier3_petrol",
    agent_class=CategoryNormalisationAgent,
    description="Petrol to vehicle fuel",
    tags=["tier3", "transport", "dev_cases"]
)
def eval_tier3_petrol():
    return {
        "input": CategoryNormalisationInput(
            query="Fuel costs this year",
            entities=[CategoryEntity(type="category", value="fuel")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="fuel",
                canon="expenses:transport.car-fuels"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="fuel"), "canon": Exact(value="expenses:transport.car-fuels")}
            ])
        }
    }


@eval_case(
    name="tier3_utilities",
    agent_class=CategoryNormalisationAgent,
    description="Utility bills category",
    tags=["tier3", "bills", "dev_cases"]
)
def eval_tier3_utilities():
    return {
        "input": CategoryNormalisationInput(
            query="Water and gas bills",
            entities=[CategoryEntity(type="category", value="water and gas")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="water and gas",
                canon="expenses:bills.utilities"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="water and gas"), "canon": Exact(value="expenses:bills.utilities")}
            ])
        }
    }


@eval_case(
    name="tier3_takeaway",
    agent_class=CategoryNormalisationAgent,
    description="Takeout food orders",
    tags=["tier3", "eating_out", "dev_cases"]
)
def eval_tier3_takeaway():
    return {
        "input": CategoryNormalisationInput(
            query="Deliveroo orders last month",
            entities=[CategoryEntity(type="category", value="Deliveroo")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="Deliveroo",
                canon="expenses:eating-out.takeouts"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="Deliveroo"), "canon": Exact(value="expenses:eating-out.takeouts")}
            ])
        }
    }


@eval_case(
    name="tier3_gym_fitness",
    agent_class=CategoryNormalisationAgent,
    description="Gym to fitness category",
    tags=["tier3", "wellness", "dev_cases"]
)
def eval_tier3_gym_fitness():
    return {
        "input": CategoryNormalisationInput(
            query="Fitness club membership fees",
            entities=[CategoryEntity(type="category", value="fitness club")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="fitness club",
                canon="expenses:wellness.healthcare"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="fitness club"), "canon": Exact(value="expenses:wellness.healthcare")}
            ])
        }
    }


@eval_case(
    name="tier3_council_tax",
    agent_class=CategoryNormalisationAgent,
    description="Council tax to utilities",
    tags=["tier3", "bills", "dev_cases"]
)
def eval_tier3_council_tax():
    return {
        "input": CategoryNormalisationInput(
            query="Local council payments",
            entities=[CategoryEntity(type="category", value="local council")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="local council",
                canon="expenses:bills.utilities"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="local council"), "canon": Exact(value="expenses:bills.utilities")}
            ])
        }
    }


@eval_case(
    name="tier3_clothes",
    agent_class=CategoryNormalisationAgent,
    description="Clothing and fashion",
    tags=["tier3", "shopping", "dev_cases"]
)
def eval_tier3_clothes():
    return {
        "input": CategoryNormalisationInput(
            query="Spending on fashion items",
            entities=[CategoryEntity(type="category", value="fashion")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="fashion",
                canon="expenses:shopping.clothes"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="fashion"), "canon": Exact(value="expenses:shopping.clothes")}
            ])
        }
    }


@eval_case(
    name="tier3_train",
    agent_class=CategoryNormalisationAgent,
    description="Train travel expenses",
    tags=["tier3", "transport", "dev_cases"]
)
def eval_tier3_train():
    return {
        "input": CategoryNormalisationInput(
            query="Railway ticket expenses",
            entities=[CategoryEntity(type="category", value="railway ticket")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="railway ticket",
                canon="expenses:transport.train"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="railway ticket"), "canon": Exact(value="expenses:transport.train")}
            ])
        }
    }


@eval_case(
    name="tier3_restaurants",
    agent_class=CategoryNormalisationAgent,
    description="Restaurant dining",
    tags=["tier3", "eating_out", "dev_cases"]
)
def eval_tier3_restaurants():
    return {
        "input": CategoryNormalisationInput(
            query="Fine dining expenses",
            entities=[CategoryEntity(type="category", value="fine dining")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="fine dining",
                canon="expenses:eating-out.restaurants"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="fine dining"), "canon": Exact(value="expenses:eating-out.restaurants")}
            ])
        }
    }


@eval_case(
    name="tier3_bars",
    agent_class=CategoryNormalisationAgent,
    description="Pub and bar spending",
    tags=["tier3", "eating_out", "dev_cases"]
)
def eval_tier3_bars():
    return {
        "input": CategoryNormalisationInput(
            query="Money spent at pubs",
            entities=[CategoryEntity(type="category", value="pubs")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="pubs",
                canon="expenses:eating-out.bars"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="pubs"), "canon": Exact(value="expenses:eating-out.bars")}
            ])
        }
    }


@eval_case(
    name="tier3_savings_transfer",
    agent_class=CategoryNormalisationAgent,
    description="Savings account transfers",
    tags=["tier3", "transfers", "dev_cases"]
)
def eval_tier3_savings_transfer():
    return {
        "input": CategoryNormalisationInput(
            query="Money saved this month",
            entities=[CategoryEntity(type="category", value="saved")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="saved",
                canon="transfers:savings"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="saved"), "canon": Exact(value="transfers:savings")}
            ])
        }
    }


@eval_case(
    name="tier3_flights",
    agent_class=CategoryNormalisationAgent,
    description="Air travel expenses",
    tags=["tier3", "transport", "dev_cases"]
)
def eval_tier3_flights():
    return {
        "input": CategoryNormalisationInput(
            query="Airline ticket costs",
            entities=[CategoryEntity(type="category", value="airline tickets")]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[NormalisedCategoryEntity(
                type="category",
                value="airline tickets",
                canon="expenses:transport.flights"
            )]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="airline tickets"), "canon": Exact(value="expenses:transport.flights")}
            ])
        }
    }


# ========== Multiple Categories Cases (5) ==========

@eval_case(
    name="multiple_groceries_utilities",
    agent_class=CategoryNormalisationAgent,
    description="Multiple category normalisation",
    tags=["multiple", "dev_cases"]
)
def eval_multiple_groceries_utilities():
    return {
        "input": CategoryNormalisationInput(
            query="Compare supermarket shopping and utility costs",
            entities=[
                CategoryEntity(type="category", value="supermarket shopping"),
                CategoryEntity(type="category", value="utility costs")
            ]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[
                NormalisedCategoryEntity(type="category", value="supermarket shopping", canon="expenses:groceries.supermarkets"),
                NormalisedCategoryEntity(type="category", value="utility costs", canon="expenses:bills.utilities")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="supermarket shopping"), "canon": Exact(value="expenses:groceries.supermarkets")},
                {"type": Exact(value="category"), "value": Exact(value="utility costs"), "canon": Exact(value="expenses:bills.utilities")}
            ])
        }
    }


@eval_case(
    name="multiple_transport_dining",
    agent_class=CategoryNormalisationAgent,
    description="Transport and dining categories",
    tags=["multiple", "dev_cases"]
)
def eval_multiple_transport_dining():
    return {
        "input": CategoryNormalisationInput(
            query="Petrol and restaurant spending",
            entities=[
                CategoryEntity(type="category", value="petrol"),
                CategoryEntity(type="category", value="restaurant")
            ]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[
                NormalisedCategoryEntity(type="category", value="petrol", canon="expenses:transport.car-fuels"),
                NormalisedCategoryEntity(type="category", value="restaurant", canon="expenses:eating-out.restaurants")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="petrol"), "canon": Exact(value="expenses:transport.car-fuels")},
                {"type": Exact(value="category"), "value": Exact(value="restaurant"), "canon": Exact(value="expenses:eating-out.restaurants")}
            ])
        }
    }


@eval_case(
    name="multiple_income_expense",
    agent_class=CategoryNormalisationAgent,
    description="Income and expense categories",
    tags=["multiple", "mixed", "dev_cases"]
)
def eval_multiple_income_expense():
    return {
        "input": CategoryNormalisationInput(
            query="Salary versus mortgage payments",
            entities=[
                CategoryEntity(type="category", value="salary"),
                CategoryEntity(type="category", value="mortgage payments")
            ]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[
                NormalisedCategoryEntity(type="category", value="salary", canon="income:salary"),
                NormalisedCategoryEntity(type="category", value="mortgage payments", canon="expenses:bills.mortgage")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="salary"), "canon": Exact(value="income:salary")},
                {"type": Exact(value="category"), "value": Exact(value="mortgage payments"), "canon": Exact(value="expenses:bills.mortgage")}
            ])
        }
    }


@eval_case(
    name="multiple_tier_mix",
    agent_class=CategoryNormalisationAgent,
    description="Mixed tier categories",
    tags=["multiple", "mixed_tiers", "dev_cases"]
)
def eval_multiple_tier_mix():
    return {
        "input": CategoryNormalisationInput(
            query="Bills, coffee, and overall spending",
            entities=[
                CategoryEntity(type="category", value="bills"),
                CategoryEntity(type="category", value="coffee"),
                CategoryEntity(type="category", value="overall spending")
            ]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[
                NormalisedCategoryEntity(type="category", value="bills", canon="expenses:bills"),
                NormalisedCategoryEntity(type="category", value="coffee", canon="expenses:eating-out.coffee"),
                NormalisedCategoryEntity(type="category", value="overall spending", canon="expenses")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="bills"), "canon": Exact(value="expenses:bills")},
                {"type": Exact(value="category"), "value": Exact(value="coffee"), "canon": Exact(value="expenses:eating-out.coffee")},
                {"type": Exact(value="category"), "value": Exact(value="overall spending"), "canon": Exact(value="expenses")}
            ])
        }
    }


@eval_case(
    name="multiple_similar_categories",
    agent_class=CategoryNormalisationAgent,
    description="Similar category variations",
    tags=["multiple", "similar", "dev_cases"]
)
def eval_multiple_similar_categories():
    return {
        "input": CategoryNormalisationInput(
            query="Train, flights, and taxi expenses",
            entities=[
                CategoryEntity(type="category", value="train"),
                CategoryEntity(type="category", value="flights"),
                CategoryEntity(type="category", value="taxi")
            ]
        ),
        "expected": CategoryNormalisationOutput(
            entities=[
                NormalisedCategoryEntity(type="category", value="train", canon="expenses:transport.train"),
                NormalisedCategoryEntity(type="category", value="flights", canon="expenses:transport.flights"),
                NormalisedCategoryEntity(type="category", value="taxi", canon="expenses:transport.taxi")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="category"), "value": Exact(value="train"), "canon": Exact(value="expenses:transport.train")},
                {"type": Exact(value="category"), "value": Exact(value="flights"), "canon": Exact(value="expenses:transport.flights")},
                {"type": Exact(value="category"), "value": Exact(value="taxi"), "canon": Exact(value="expenses:transport.taxi")}
            ])
        }
    }
