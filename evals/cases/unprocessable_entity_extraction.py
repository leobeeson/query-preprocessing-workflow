"""
Evaluation cases for UnprocessableEntityExtractionAgent using decorator pattern.
"""

from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact, OneOf, Substring
from src.workflow_nodes.query_preprocessing.unprocessable_entity_extraction_agent import UnprocessableEntityExtractionAgent
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import UnprocessableEntityExtractionOutput, UnprocessableEntity


# ========== Geographic Entity Tests (7) ==========

@eval_case(
    name="geographic_comparison",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Geographic regions comparison",
    tags=["geographic", "critical", "dev_cases"]
)
def eval_geographic_comparison():
    return {
        "input": QueryInput(query="Transaction count in Wales compared to Northern Ireland from last quarter"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="Wales", critical=True),
                UnprocessableEntity(type="geographic", value="Northern Ireland", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Exact(value="Wales"), "critical": Exact(value=True)},
                {"type": Exact(value="geographic"), "value": Exact(value="Northern Ireland"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="city_location",
    agent_class=UnprocessableEntityExtractionAgent,
    description="City-based filtering",
    tags=["geographic", "critical", "dev_cases"]
)
def eval_city_location():
    return {
        "input": QueryInput(query="Sainsbury's transactions in Birmingham"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="Birmingham", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Exact(value="Birmingham"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="international_transactions",
    agent_class=UnprocessableEntityExtractionAgent,
    description="International location reference",
    tags=["geographic", "critical", "dev_cases"]
)
def eval_international_transactions():
    return {
        "input": QueryInput(query="Purchases made overseas during holidays"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="overseas", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Exact(value="overseas"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="uk_reference_critical",
    agent_class=UnprocessableEntityExtractionAgent,
    description="UK geographic filter for transaction location",
    tags=["geographic", "critical", "dev_cases"]
)
def eval_uk_reference_critical():
    return {
        "input": QueryInput(query="My UK-based NatWest transactions at Costa"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="UK-based", critical=False),
                UnprocessableEntity(type="bank_reference", value="NatWest", critical=False)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Substring(value="UK"), "critical": Exact(value=False)},
                {"type": Exact(value="bank_reference"), "value": Exact(value="NatWest"), "critical": Exact(value=False)}
            ])
        }
    }


@eval_case(
    name="redundant_uk_reference",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Redundant UK reference in Sterling context",
    tags=["geographic", "non-critical", "dev_cases"]
)
def eval_redundant_uk_reference():
    return {
        "input": QueryInput(query="UK pounds Sterling transactions at Tesco"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="UK", critical=False)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Exact(value="UK"), "critical": Exact(value=False)}
            ])
        }
    }


@eval_case(
    name="country_specific",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Country-specific transactions",
    tags=["geographic", "critical", "dev_cases"]
)
def eval_country_specific():
    return {
        "input": QueryInput(query="Spending in France during summer"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="France", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Exact(value="France"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="regional_reference",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Regional geographic reference",
    tags=["geographic", "critical", "dev_cases"]
)
def eval_regional_reference():
    return {
        "input": QueryInput(query="Purchases in the North West region"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="North West region", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Substring(value="North West"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="domestic_international",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Domestic vs international",
    tags=["geographic", "critical", "dev_cases"]
)
def eval_domestic_international():
    return {
        "input": QueryInput(query="Domestic spending versus foreign purchases"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="geographic", value="Domestic", critical=True),
                UnprocessableEntity(type="geographic", value="foreign", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="geographic"), "value": Exact(value="Domestic"), "critical": Exact(value=True)},
                {"type": Exact(value="geographic"), "value": Exact(value="foreign"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Payment Method Tests (7) ==========

@eval_case(
    name="card_type_filter",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Debit card payment method",
    tags=["payment_method", "critical", "dev_cases"]
)
def eval_card_type_filter():
    return {
        "input": QueryInput(query="Debit card spending at Amazon"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="payment_method", value="Debit card", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Substring(value="Debit card"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="contactless_payments",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Contactless payment method",
    tags=["payment_method", "critical", "dev_cases"]
)
def eval_contactless_payments():
    return {
        "input": QueryInput(query="Tap-to-pay transactions below £50"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="payment_method", value="Tap-to-pay", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Substring(value="Tap-to-pay"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="cash_withdrawals",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Cash payment reference",
    tags=["payment_method", "critical", "dev_cases"]
)
def eval_cash_withdrawals():
    return {
        "input": QueryInput(query="Money withdrawn in cash from last week"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="payment_method", value="cash", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Exact(value="cash"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="multiple_payment_methods",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Multiple payment methods",
    tags=["payment_method", "critical", "dev_cases"]
)
def eval_multiple_payment_methods():
    return {
        "input": QueryInput(query="Credit versus debit card usage this month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="payment_method", value="Credit", critical=True),
                UnprocessableEntity(type="payment_method", value="debit card", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Substring(value="Credit"), "critical": Exact(value=True)},
                {"type": Exact(value="payment_method"), "value": Substring(value="debit"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="apple_pay",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Digital wallet payment",
    tags=["payment_method", "critical", "dev_cases"]
)
def eval_apple_pay():
    return {
        "input": QueryInput(query="Apple Pay purchases at retail stores"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="payment_method", value="Apple Pay", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Exact(value="Apple Pay"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Person Recipient Tests (6) ==========

@eval_case(
    name="named_person",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Payment to named individual",
    tags=["person_recipient", "critical", "dev_cases"]
)
def eval_named_person():
    return {
        "input": QueryInput(query="Payments sent to David Johnson"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="person_recipient", value="David Johnson", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="David Johnson"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="family_member",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Payment to family member",
    tags=["person_recipient", "critical", "dev_cases"]
)
def eval_family_member():
    return {
        "input": QueryInput(query="Money transferred to my daughter"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="person_recipient", value="my daughter", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="my daughter"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="landlord_payment",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Rent to property owner",
    tags=["person_recipient", "critical", "dev_cases"]
)
def eval_landlord_payment():
    return {
        "input": QueryInput(query="Monthly rent to the property owner"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="person_recipient", value="property owner", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Substring(value="property owner"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="multiple_recipients",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Multiple person recipients",
    tags=["person_recipient", "critical", "dev_cases"]
)
def eval_multiple_recipients():
    return {
        "input": QueryInput(query="Transfers to Bob and Alice in January"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="person_recipient", value="Bob", critical=True),
                UnprocessableEntity(type="person_recipient", value="Alice", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="Bob"), "critical": Exact(value=True)},
                {"type": Exact(value="person_recipient"), "value": Exact(value="Alice"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="roommate_payment",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Payment to roommate",
    tags=["person_recipient", "critical", "dev_cases"]
)
def eval_roommate_payment():
    return {
        "input": QueryInput(query="Split bills with my flatmate"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="person_recipient", value="my flatmate", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Exact(value="my flatmate"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="friend_payment",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Payment to friend",
    tags=["person_recipient", "critical", "dev_cases"]
)
def eval_friend_payment():
    return {
        "input": QueryInput(query="Loans to my best friend Sarah"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="person_recipient", value="my best friend Sarah", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="person_recipient"), "value": Substring(value="Sarah"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Transaction Channel Tests (6) ==========

@eval_case(
    name="web_purchases",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Web-based transactions",
    tags=["transaction_channel", "critical", "dev_cases"]
)
def eval_web_purchases():
    return {
        "input": QueryInput(query="Web-based shopping from yesterday"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="Web-based", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Substring(value="Web"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="physical_store",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Physical store purchases",
    tags=["transaction_channel", "critical", "dev_cases"]
)
def eval_physical_store():
    return {
        "input": QueryInput(query="Physical store visits at Next"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="Physical store", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Substring(value="Physical store"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="cash_machine",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Cash machine withdrawals",
    tags=["transaction_channel", "critical", "dev_cases"]
)
def eval_cash_machine():
    return {
        "input": QueryInput(query="Cash machine usage this week"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="Cash machine", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Substring(value="Cash machine"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="phone_app",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Phone app transactions",
    tags=["transaction_channel", "critical", "dev_cases"]
)
def eval_phone_app():
    return {
        "input": QueryInput(query="Payments through phone application"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="phone application", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Substring(value="phone"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="telephone_banking",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Telephone banking transactions",
    tags=["transaction_channel", "critical", "dev_cases"]
)
def eval_telephone_banking():
    return {
        "input": QueryInput(query="Telephone banking transfers"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="Telephone banking", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Exact(value="Telephone banking"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="branch_transactions",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Bank branch transactions",
    tags=["transaction_channel", "critical", "dev_cases"]
)
def eval_branch_transactions():
    return {
        "input": QueryInput(query="In-branch deposits last month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="In-branch", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Substring(value="branch"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Product/Service Tests (7) ==========

@eval_case(
    name="specific_coffee_product",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Specific coffee product",
    tags=["product_service", "critical", "dev_cases"]
)
def eval_specific_coffee_product():
    return {
        "input": QueryInput(query="Spending on cappuccinos at Costa"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="cappuccinos", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Exact(value="cappuccinos"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="fuel_type",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Specific fuel type",
    tags=["product_service", "critical", "dev_cases"]
)
def eval_fuel_type():
    return {
        "input": QueryInput(query="Diesel purchases at Shell"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="Diesel", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Exact(value="Diesel"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="clothing_item",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Specific clothing item",
    tags=["product_service", "critical", "dev_cases"]
)
def eval_clothing_item():
    return {
        "input": QueryInput(query="Jacket purchases at Zara"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="Jacket", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Exact(value="Jacket"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="personal_service",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Personal service type",
    tags=["product_service", "critical", "dev_cases"]
)
def eval_personal_service():
    return {
        "input": QueryInput(query="Manicure appointments this quarter"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="Manicure", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="Manicure"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="food_item",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Specific food item",
    tags=["product_service", "critical", "dev_cases"]
)
def eval_food_item():
    return {
        "input": QueryInput(query="Pizza orders from Domino's"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="Pizza", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="Pizza"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="electronics_product",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Electronics product",
    tags=["product_service", "critical", "dev_cases"]
)
def eval_electronics_product():
    return {
        "input": QueryInput(query="Laptop purchases at Currys"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="Laptop", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Exact(value="Laptop"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="subscription_service",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Specific subscription service",
    tags=["product_service", "critical", "dev_cases"]
)
def eval_subscription_service():
    return {
        "input": QueryInput(query="Game Pass subscription fees"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="Game Pass", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="Game Pass"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Financial Product Tests (5) ==========

@eval_case(
    name="home_loan",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Home loan financial product",
    tags=["financial_product", "critical", "dev_cases"]
)
def eval_home_loan():
    return {
        "input": QueryInput(query="Home loan repayments"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="financial_product", value="Home loan", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": OneOf(values=["financial_product", "product_service"]), "value": Exact(value="Home loan"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="student_loan",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Student loan payments",
    tags=["financial_product", "critical", "dev_cases"]
)
def eval_student_loan():
    return {
        "input": QueryInput(query="Student loan deductions this year"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="financial_product", value="Student loan", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": OneOf(values=["financial_product", "product_service"]), "value": Substring(value="Student loan"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="overdraft_fees",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Overdraft financial product",
    tags=["financial_product", "critical", "dev_cases"]
)
def eval_overdraft_fees():
    return {
        "input": QueryInput(query="Overdraft charges last month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="financial_product", value="Overdraft", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": OneOf(values=["financial_product", "product_service"]), "value": Substring(value="Overdraft"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="credit_facility",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Credit facility reference",
    tags=["financial_product", "critical", "dev_cases"]
)
def eval_credit_facility():
    return {
        "input": QueryInput(query="Line of credit usage"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="financial_product", value="Line of credit", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": OneOf(values=["financial_product", "product_service"]), "value": Substring(value="credit"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="interest_charges",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Interest charges",
    tags=["financial_product", "critical", "dev_cases"]
)
def eval_interest_charges():
    return {
        "input": QueryInput(query="Interest charges on purchases"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="financial_product", value="Interest", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": OneOf(values=["financial_product", "product_service"]), "value": Substring(value="Interest"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Transaction Status Tests (5) ==========

@eval_case(
    name="awaiting_clearance",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Pending transaction status",
    tags=["transaction_status", "critical", "dev_cases"]
)
def eval_awaiting_clearance():
    return {
        "input": QueryInput(query="Transactions awaiting clearance"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_status", value="awaiting clearance", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_status"), "value": Substring(value="awaiting"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="rejected_payments",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Rejected transaction status",
    tags=["transaction_status", "critical", "dev_cases"]
)
def eval_rejected_payments():
    return {
        "input": QueryInput(query="Rejected payment attempts"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_status", value="Rejected", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_status"), "value": Exact(value="Rejected"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="reversed_transactions",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Reversed transaction status",
    tags=["transaction_status", "critical", "dev_cases"]
)
def eval_reversed_transactions():
    return {
        "input": QueryInput(query="Reversed charges from retailers"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_status", value="Reversed", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_status"), "value": Substring(value="Reversed"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="cancelled_orders",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Cancelled transaction status",
    tags=["transaction_status", "critical", "dev_cases"]
)
def eval_cancelled_orders():
    return {
        "input": QueryInput(query="Cancelled online orders"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_status", value="Cancelled", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_status"), "value": Exact(value="Cancelled"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Account Type Tests (4) ==========

@eval_case(
    name="current_account",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Current account reference",
    tags=["account", "critical", "dev_cases"]
)
def eval_current_account():
    return {
        "input": QueryInput(query="Spending from checking account"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="account", value="checking account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="checking"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="business_account",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Business account reference",
    tags=["account", "critical", "dev_cases"]
)
def eval_business_account():
    return {
        "input": QueryInput(query="Business account expenditure"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="account", value="Business account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="Business"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="pension_account",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Pension account reference",
    tags=["account", "critical", "dev_cases"]
)
def eval_pension_account():
    return {
        "input": QueryInput(query="Check my pension account balance"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="account", value="pension account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="pension account"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="isa_account",
    agent_class=UnprocessableEntityExtractionAgent,
    description="ISA account reference",
    tags=["account", "critical", "dev_cases"]
)
def eval_isa_account():
    return {
        "input": QueryInput(query="ISA account deposits"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="account", value="ISA account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Substring(value="ISA"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Complex/Mixed Entity Tests (6) ==========

@eval_case(
    name="multiple_unprocessable_types",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Multiple different unprocessable entity types",
    tags=["complex", "critical", "dev_cases"]
)
def eval_multiple_unprocessable_types():
    return {
        "input": QueryInput(query="Debit card payments in Bristol for fuel"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="payment_method", value="Debit card", critical=True),
                UnprocessableEntity(type="geographic", value="Bristol", critical=True),
                UnprocessableEntity(type="product_service", value="fuel", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="payment_method"), "value": Substring(value="Debit card"), "critical": Exact(value=True)},
                {"type": Exact(value="geographic"), "value": Exact(value="Bristol"), "critical": Exact(value=True)},
                {"type": Exact(value="product_service"), "value": Exact(value="fuel"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="mixed_criticality",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Mix of critical and non-critical entities",
    tags=["complex", "mixed-critical", "dev_cases"]
)
def eval_mixed_criticality():
    return {
        "input": QueryInput(query="Web purchases in British pounds at European retailers"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="Web", critical=True),
                UnprocessableEntity(type="geographic", value="European", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Substring(value="Web"), "critical": Exact(value=True)},
                {"type": Exact(value="geographic"), "value": Substring(value="European"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="channel_and_method",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Transaction channel with payment method",
    tags=["complex", "critical", "dev_cases"]
)
def eval_channel_and_method():
    return {
        "input": QueryInput(query="ATM cash withdrawals abroad"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_channel", value="ATM", critical=True),
                UnprocessableEntity(type="payment_method", value="cash", critical=True),
                UnprocessableEntity(type="geographic", value="abroad", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_channel"), "value": Exact(value="ATM"), "critical": Exact(value=True)},
                {"type": Exact(value="payment_method"), "value": Exact(value="cash"), "critical": Exact(value=True)},
                {"type": Exact(value="geographic"), "value": Exact(value="abroad"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="person_and_product",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Person recipient with product",
    tags=["complex", "critical", "dev_cases"]
)
def eval_person_and_product():
    return {
        "input": QueryInput(query="Birthday gift purchases for my sister"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="product_service", value="Birthday gift", critical=True),
                UnprocessableEntity(type="person_recipient", value="my sister", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="product_service"), "value": Substring(value="gift"), "critical": Exact(value=True)},
                {"type": Exact(value="person_recipient"), "value": Exact(value="my sister"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="status_and_channel",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Transaction status with channel",
    tags=["complex", "critical", "dev_cases"]
)
def eval_status_and_channel():
    return {
        "input": QueryInput(query="Failed online payment attempts"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="transaction_status", value="Failed", critical=True),
                UnprocessableEntity(type="transaction_channel", value="online", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="transaction_status"), "value": Exact(value="Failed"), "critical": Exact(value=True)},
                {"type": Exact(value="transaction_channel"), "value": Exact(value="online"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="account_and_method",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Account type with processable transaction type",
    tags=["complex", "critical", "dev_cases"]
)
def eval_account_and_method():
    return {
        "input": QueryInput(query="Joint account direct debit payments"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="account", value="Joint account", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="account"), "value": Exact(value="Joint account"), "critical": Exact(value=True)}
            ])
        }
    }


# ========== Negative Tests - No Unprocessable Entities (10) ==========

@eval_case(
    name="only_processable_entities",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Query with only processable entities",
    tags=["negative", "no-entities", "dev_cases"]
)
def eval_only_processable_entities():
    return {
        "input": QueryInput(query="Sainsbury's transactions over £50 yesterday"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="category_not_product",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Category that might seem like product",
    tags=["negative", "category", "dev_cases"]
)
def eval_category_not_product():
    return {
        "input": QueryInput(query="Total spending on coffee this month"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="books_category",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Books as category not product",
    tags=["negative", "category", "dev_cases"]
)
def eval_books_category():
    return {
        "input": QueryInput(query="Books purchases from last quarter"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="beauty_category",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Beauty as category not service",
    tags=["negative", "category", "dev_cases"]
)
def eval_beauty_category():
    return {
        "input": QueryInput(query="Beauty spending in December"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="home_repairs_category",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Home repairs as compound category",
    tags=["negative", "category", "dev_cases"]
)
def eval_home_repairs_category():
    return {
        "input": QueryInput(query="Home repairs costs this year"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="car_maintenance_category",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Car maintenance as compound category",
    tags=["negative", "category", "dev_cases"]
)
def eval_car_maintenance_category():
    return {
        "input": QueryInput(query="Car maintenance expenses last month"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="organization_not_person",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Organization is merchant not person recipient",
    tags=["negative", "merchant", "dev_cases"]
)
def eval_organization_not_person():
    return {
        "input": QueryInput(query="Council tax payments to the local authority"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="bank_transfer_is_category",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Bank transfer is a processable category not payment method",
    tags=["negative", "transfer", "dev_cases"]
)
def eval_bank_transfer_is_category():
    return {
        "input": QueryInput(query="Bank transfer payments last month"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="budget_is_processable",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Budget references are processable",
    tags=["negative", "budget", "dev_cases"]
)
def eval_budget_is_processable():
    return {
        "input": QueryInput(query="Check spending against budget limits"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


# ========== Edge Cases (3) ==========

@eval_case(
    name="ambiguous_mortgage",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Mortgage as financial product vs category",
    tags=["edge-case", "financial_product", "dev_cases"]
)
def eval_ambiguous_mortgage():
    # When "mortgage" appears as a financial product context (not as spending category)
    return {
        "input": QueryInput(query="Interest on my mortgage loan"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="financial_product", value="Interest", critical=True),
                UnprocessableEntity(type="financial_product", value="mortgage loan", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": OneOf(values=["financial_product", "product_service"]), "value": Substring(value="Interest"), "critical": Exact(value=True)},
                {"type": OneOf(values=["financial_product", "product_service"]), "value": Substring(value="mortgage"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="currency_reference",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Foreign currency reference",
    tags=["edge-case", "currency", "dev_cases"]
)
def eval_currency_reference():
    return {
        "input": QueryInput(query="Payments in dollars last month"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="currency", value="dollars", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="currency"), "value": Exact(value="dollars"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="business_purpose",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Business expense purpose",
    tags=["edge-case", "purpose", "dev_cases"]
)
def eval_business_purpose():
    return {
        "input": QueryInput(query="Work-related purchases at shops"),
        "expected": UnprocessableEntityExtractionOutput(
            entities=[
                UnprocessableEntity(type="expense_purpose", value="Work-related", critical=True)
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="expense_purpose"), "value": Substring(value="Work"), "critical": Exact(value=True)}
            ])
        }
    }


@eval_case(
    name="budget_query",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Budget is processable entity",
    tags=["negative", "budget", "dev_cases"]
)
def eval_budget_query():
    return {
        "input": QueryInput(query="My expenses budget?"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="home_repairs_query",
    agent_class=UnprocessableEntityExtractionAgent,
    description="Home repairs is a processable category",
    tags=["negative", "category", "dev_cases"]
)
def eval_home_repairs_query():
    return {
        "input": QueryInput(query="How much I have spent on home repairs in 2025?"),
        "expected": UnprocessableEntityExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }