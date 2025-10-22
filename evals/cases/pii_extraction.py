"""
Evaluation cases for PIIExtractionAgent using decorator pattern.
"""

from evals.decorators import eval_case
from evals.field_validators import ListMatches, Exact, Substring
from src.workflow_nodes.query_preprocessing.pii_extraction_agent import PIIExtractionAgent
from src.models.base_models import QueryInput
from src.models.entity_extraction_models import PIIExtractionOutput, PIIEntity as Entity


# ========== Transaction Context Tests (NOT PII) - 6 cases ==========

@eval_case(
    name="merchant_in_query_not_pii",
    agent_class=PIIExtractionAgent,
    description="Merchant names in transaction queries are NOT PII",
    tags=["negative", "merchant", "dev_cases"]
)
def eval_merchant_in_query_not_pii():
    return {
        "input": QueryInput(query="Display all purchases at Waitrose this month"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="payment_recipient_not_pii",
    agent_class=PIIExtractionAgent,
    description="Payment recipients are NOT PII",
    tags=["negative", "recipient", "dev_cases"]
)
def eval_payment_recipient_not_pii():
    return {
        "input": QueryInput(query="Transfer to Emily Watson for £300 last week"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="business_phone_not_pii",
    agent_class=PIIExtractionAgent,
    description="Customer service numbers are NOT PII",
    tags=["negative", "phone", "dev_cases"]
)
def eval_business_phone_not_pii():
    return {
        "input": QueryInput(query="Contact support at 0845 678 901"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="store_location_not_pii",
    agent_class=PIIExtractionAgent,
    description="Store locations are NOT PII",
    tags=["negative", "location", "dev_cases"]
)
def eval_store_location_not_pii():
    return {
        "input": QueryInput(query="ASDA Manchester purchases"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="family_transfer_not_pii",
    agent_class=PIIExtractionAgent,
    description="Family member transfers are NOT PII",
    tags=["negative", "family", "dev_cases"]
)
def eval_family_transfer_not_pii():
    return {
        "input": QueryInput(query="Sent £100 to Mum yesterday"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="service_payment_not_pii",
    agent_class=PIIExtractionAgent,
    description="Payments for professional services are NOT PII",
    tags=["negative", "service", "dev_cases"]
)
def eval_service_payment_not_pii():
    return {
        "input": QueryInput(query="Payment to Dr. Anderson for medical consultation"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


# ========== Personal Contact Information - 7 cases ==========

@eval_case(
    name="exposed_name_email",
    agent_class=PIIExtractionAgent,
    description="Exposed personal name and email IS PII",
    tags=["personal", "name", "email", "dev_cases"]
)
def eval_exposed_name_email():
    return {
        "input": QueryInput(query="I'm Jane Doe and you can reach me at jane.doe@hotmail.com"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="name", value="Jane Doe"),
                Entity(type="email", value="jane.doe@hotmail.com")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="name"), "value": Exact(value="Jane Doe")},
                {"type": Exact(value="email"), "value": Substring(value="jane.doe")}
            ])
        }
    }


@eval_case(
    name="personal_phone",
    agent_class=PIIExtractionAgent,
    description="Personal phone number IS PII",
    tags=["personal", "phone", "dev_cases"]
)
def eval_personal_phone():
    return {
        "input": QueryInput(query="Reach me on 07812345678 regarding my query"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="phone", value="07812345678")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="phone"), "value": Exact(value="07812345678")}
            ])
        }
    }


@eval_case(
    name="email_with_typo",
    agent_class=PIIExtractionAgent,
    description="Email with typo preserved exactly",
    tags=["personal", "email", "typo", "dev_cases"]
)
def eval_email_with_typo():
    return {
        "input": QueryInput(query="Send it to sara.jonse@gmial.com"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="email", value="sara.jonse@gmial.com")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="email"), "value": Exact(value="sara.jonse@gmial.com")}
            ])
        }
    }


@eval_case(
    name="phone_with_formatting",
    agent_class=PIIExtractionAgent,
    description="Phone with formatting characters preserved",
    tags=["personal", "phone", "formatting", "dev_cases"]
)
def eval_phone_with_formatting():
    return {
        "input": QueryInput(query="Call me on (07955) 987654"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="phone", value="(07955) 987654")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="phone"), "value": Exact(value="(07955) 987654")}
            ])
        }
    }


@eval_case(
    name="international_phone",
    agent_class=PIIExtractionAgent,
    description="International phone number with country code",
    tags=["personal", "phone", "international", "dev_cases"]
)
def eval_international_phone():
    return {
        "input": QueryInput(query="My mobile is +44 7700 900456"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="phone", value="+44 7700 900456")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="phone"), "value": Substring(value="+44")}
            ])
        }
    }


@eval_case(
    name="email_subdomain",
    agent_class=PIIExtractionAgent,
    description="Email with subdomain",
    tags=["personal", "email", "subdomain", "dev_cases"]
)
def eval_email_subdomain():
    return {
        "input": QueryInput(query="My work email is robert.jones@finance.company.co.uk"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="email", value="robert.jones@finance.company.co.uk")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="email"), "value": Substring(value="robert.jones@")}
            ])
        }
    }


@eval_case(
    name="multiple_contact_info",
    agent_class=PIIExtractionAgent,
    description="Multiple contact details together",
    tags=["personal", "phone", "email", "multiple", "dev_cases"]
)
def eval_multiple_contact_info():
    return {
        "input": QueryInput(query="Contact details: 07901234567 or mike@gmail.com"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="phone", value="07901234567"),
                Entity(type="email", value="mike@gmail.com")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="phone"), "value": Exact(value="07901234567")},
                {"type": Exact(value="email"), "value": Exact(value="mike@gmail.com")}
            ])
        }
    }


# ========== Authentication & Access - 6 cases ==========

@eval_case(
    name="username_password_pin",
    agent_class=PIIExtractionAgent,
    description="Username, password, and PIN together",
    tags=["authentication", "username", "password", "pin", "dev_cases"]
)
def eval_username_password_pin():
    return {
        "input": QueryInput(query="My login: user987, password: Tr0ub4dor&3, PIN: 8421"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="username", value="user987"),
                Entity(type="password", value="Tr0ub4dor&3"),
                Entity(type="pin", value="8421")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="username"), "value": Exact(value="user987")},
                {"type": Exact(value="password"), "value": Exact(value="Tr0ub4dor&3")},
                {"type": Exact(value="pin"), "value": Exact(value="8421")}
            ])
        }
    }


@eval_case(
    name="social_media_handle",
    agent_class=PIIExtractionAgent,
    description="Social media username with @ symbol",
    tags=["authentication", "username", "social", "dev_cases"]
)
def eval_social_media_handle():
    return {
        "input": QueryInput(query="Add me on Twitter @jane_smith_2024"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="username", value="@jane_smith_2024")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="username"), "value": Exact(value="@jane_smith_2024")}
            ])
        }
    }


@eval_case(
    name="password_phrase",
    agent_class=PIIExtractionAgent,
    description="Password as a phrase with spaces",
    tags=["authentication", "password", "phrase", "dev_cases"]
)
def eval_password_phrase():
    return {
        "input": QueryInput(query="Reset password to: blue sky thinking 2025"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="password", value="blue sky thinking 2025")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="password"), "value": Substring(value="blue sky")}
            ])
        }
    }


@eval_case(
    name="forgotten_password",
    agent_class=PIIExtractionAgent,
    description="Password in forgot password context",
    tags=["authentication", "password", "dev_cases"]
)
def eval_forgotten_password():
    return {
        "input": QueryInput(query="Can't remember if my password was Winter2025! or Summer2024!"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="password", value="Winter2025!"),
                Entity(type="password", value="Summer2024!")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="password"), "value": Substring(value="Winter")},
                {"type": Exact(value="password"), "value": Substring(value="Summer")}
            ])
        }
    }


@eval_case(
    name="atm_pin",
    agent_class=PIIExtractionAgent,
    description="ATM PIN number",
    tags=["authentication", "pin", "atm", "dev_cases"]
)
def eval_atm_pin():
    return {
        "input": QueryInput(query="My cash machine PIN is 5283"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="pin", value="5283")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="pin"), "value": Exact(value="5283")}
            ])
        }
    }


@eval_case(
    name="system_username",
    agent_class=PIIExtractionAgent,
    description="System login username",
    tags=["authentication", "username", "system", "dev_cases"]
)
def eval_system_username():
    return {
        "input": QueryInput(query="System login is sarah.thompson"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="username", value="sarah.thompson")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="username"), "value": Exact(value="sarah.thompson")}
            ])
        }
    }


# ========== Financial Information - 9 cases ==========

@eval_case(
    name="full_card_details",
    agent_class=PIIExtractionAgent,
    description="Complete card with number, CVV, and expiry",
    tags=["financial", "card", "complete", "dev_cases"]
)
def eval_full_card_details():
    return {
        "input": QueryInput(query="Card: 5555-6666-7777-8888, security code: 321, expiry: 11/27"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="card_number", value="5555-6666-7777-8888"),
                Entity(type="cvv", value="321"),
                Entity(type="card_expiry", value="11/27")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="card_number"), "value": Substring(value="5555-6666")},
                {"type": Exact(value="cvv"), "value": Exact(value="321")},
                {"type": Exact(value="card_expiry"), "value": Exact(value="11/27")}
            ])
        }
    }


@eval_case(
    name="partial_card_number",
    agent_class=PIIExtractionAgent,
    description="Partial card number last 4 digits",
    tags=["financial", "card", "partial", "dev_cases"]
)
def eval_partial_card_number():
    return {
        "input": QueryInput(query="Card finishing with 3456 was used"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="card_number", value="3456")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="card_number"), "value": Exact(value="3456")}
            ])
        }
    }


@eval_case(
    name="masked_card_with_visible",
    agent_class=PIIExtractionAgent,
    description="Masked card with visible last digits",
    tags=["financial", "card", "masked", "dev_cases"]
)
def eval_masked_card_with_visible():
    return {
        "input": QueryInput(query="Charge to card **** **** **** 5678"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="card_number", value="**** **** **** 5678")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="card_number"), "value": Substring(value="5678")}
            ])
        }
    }


@eval_case(
    name="cvv_as_cvc",
    agent_class=PIIExtractionAgent,
    description="CVV labeled as CVC",
    tags=["financial", "cvv", "dev_cases"]
)
def eval_cvv_as_cvc():
    return {
        "input": QueryInput(query="Enter CVC: 654"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="cvv", value="654")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="cvv"), "value": Exact(value="654")}
            ])
        }
    }


@eval_case(
    name="card_expiry_long_format",
    agent_class=PIIExtractionAgent,
    description="Card expiry in MM/YYYY format",
    tags=["financial", "card_expiry", "dev_cases"]
)
def eval_card_expiry_long_format():
    return {
        "input": QueryInput(query="Valid until 10/2026"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="card_expiry", value="10/2026")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="card_expiry"), "value": Exact(value="10/2026")}
            ])
        }
    }


@eval_case(
    name="iban_with_spaces",
    agent_class=PIIExtractionAgent,
    description="IBAN with spaces",
    tags=["financial", "iban", "dev_cases"]
)
def eval_iban_with_spaces():
    return {
        "input": QueryInput(query="Account: GB29 NWBK 6016 1331 9268 19"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="bank_account", value="GB29 NWBK 6016 1331 9268 19")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="bank_account"), "value": Substring(value="GB29")}
            ])
        }
    }


@eval_case(
    name="iban_no_spaces",
    agent_class=PIIExtractionAgent,
    description="IBAN without spaces",
    tags=["financial", "iban", "dev_cases"]
)
def eval_iban_no_spaces():
    return {
        "input": QueryInput(query="Send to GB15MIDL40051512345678"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="bank_account", value="GB15MIDL40051512345678")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="bank_account"), "value": Substring(value="GB15MIDL")}
            ])
        }
    }


@eval_case(
    name="swift_code_8char",
    agent_class=PIIExtractionAgent,
    description="SWIFT code 8 characters",
    tags=["financial", "swift", "dev_cases"]
)
def eval_swift_code_8char():
    return {
        "input": QueryInput(query="Bank SWIFT: NWBKGB2L"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="swift_code", value="NWBKGB2L")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="swift_code"), "value": Exact(value="NWBKGB2L")}
            ])
        }
    }


@eval_case(
    name="swift_code_11char",
    agent_class=PIIExtractionAgent,
    description="SWIFT code 11 characters with branch",
    tags=["financial", "swift", "dev_cases"]
)
def eval_swift_code_11char():
    return {
        "input": QueryInput(query="Wire transfer to CHASUS33XXX"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="swift_code", value="CHASUS33XXX")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="swift_code"), "value": Exact(value="CHASUS33XXX")}
            ])
        }
    }


# ========== UK-Specific Identifiers - 6 cases ==========

@eval_case(
    name="nhs_with_spaces",
    agent_class=PIIExtractionAgent,
    description="NHS number with spaces",
    tags=["uk_ids", "nhs", "dev_cases"]
)
def eval_nhs_with_spaces():
    return {
        "input": QueryInput(query="NHS: 987 654 3210"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="nhs_number", value="987 654 3210")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="nhs_number"), "value": Substring(value="987 654")}
            ])
        }
    }


@eval_case(
    name="nhs_no_spaces",
    agent_class=PIIExtractionAgent,
    description="NHS number without spaces",
    tags=["uk_ids", "nhs", "dev_cases"]
)
def eval_nhs_no_spaces():
    return {
        "input": QueryInput(query="Patient number 9876543210"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="nhs_number", value="9876543210")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="nhs_number"), "value": Exact(value="9876543210")}
            ])
        }
    }


@eval_case(
    name="ni_with_spaces",
    agent_class=PIIExtractionAgent,
    description="NI number with spaces",
    tags=["uk_ids", "ni", "dev_cases"]
)
def eval_ni_with_spaces():
    return {
        "input": QueryInput(query="NI number: QQ 12 34 56 C"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="ni_number", value="QQ 12 34 56 C")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="ni_number"), "value": Substring(value="QQ 12 34")}
            ])
        }
    }


@eval_case(
    name="ni_no_spaces",
    agent_class=PIIExtractionAgent,
    description="NI number without spaces",
    tags=["uk_ids", "ni", "dev_cases"]
)
def eval_ni_no_spaces():
    return {
        "input": QueryInput(query="Insurance number: AB987654C"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="ni_number", value="AB987654C")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="ni_number"), "value": Exact(value="AB987654C")}
            ])
        }
    }


@eval_case(
    name="utr_formatted",
    agent_class=PIIExtractionAgent,
    description="UTR with formatting",
    tags=["uk_ids", "utr", "dev_cases"]
)
def eval_utr_formatted():
    return {
        "input": QueryInput(query="Tax ref: 98765 43210"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="utr_number", value="98765 43210")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="utr_number"), "value": Substring(value="98765")}
            ])
        }
    }


@eval_case(
    name="utr_unformatted",
    agent_class=PIIExtractionAgent,
    description="UTR without formatting",
    tags=["uk_ids", "utr", "dev_cases"]
)
def eval_utr_unformatted():
    return {
        "input": QueryInput(query="UTR: 1234567890"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="utr_number", value="1234567890")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="utr_number"), "value": Exact(value="1234567890")}
            ])
        }
    }


# ========== Cloud Credentials - 2 cases ==========

@eval_case(
    name="aws_access_key",
    agent_class=PIIExtractionAgent,
    description="AWS access key",
    tags=["cloud", "aws", "dev_cases"]
)
def eval_aws_access_key():
    return {
        "input": QueryInput(query="Access: AKIATESTKEYEXAMPLE123"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="aws_key", value="AKIATESTKEYEXAMPLE123")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="aws_key"), "value": Substring(value="AKIA")}
            ])
        }
    }


@eval_case(
    name="aws_secret_key",
    agent_class=PIIExtractionAgent,
    description="AWS secret key",
    tags=["cloud", "aws", "dev_cases"]
)
def eval_aws_secret_key():
    return {
        "input": QueryInput(query="Secret: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="aws_key", value="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="aws_key"), "value": Substring(value="wJalrXUtn")}
            ])
        }
    }


# ========== OTHER PII - 5 cases ==========

@eval_case(
    name="ssn_format",
    agent_class=PIIExtractionAgent,
    description="Social Security Number",
    tags=["other_pii", "ssn", "dev_cases"]
)
def eval_ssn_format():
    return {
        "input": QueryInput(query="SSN: 987-65-4321"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="other", value="987-65-4321")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="other"), "value": Exact(value="987-65-4321")}
            ])
        }
    }


@eval_case(
    name="passport_number",
    agent_class=PIIExtractionAgent,
    description="Passport number",
    tags=["other_pii", "passport", "dev_cases"]
)
def eval_passport_number():
    return {
        "input": QueryInput(query="Passport: GB9876543"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="other", value="GB9876543")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="other"), "value": Exact(value="GB9876543")}
            ])
        }
    }


@eval_case(
    name="drivers_license",
    agent_class=PIIExtractionAgent,
    description="Driver's license number",
    tags=["other_pii", "license", "dev_cases"]
)
def eval_drivers_license():
    return {
        "input": QueryInput(query="License number: JOHNS123456AB9CD"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="other", value="JOHNS123456AB9CD")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="other"), "value": Substring(value="JOHNS")}
            ])
        }
    }


@eval_case(
    name="medical_record",
    agent_class=PIIExtractionAgent,
    description="Medical record number",
    tags=["other_pii", "medical", "dev_cases"]
)
def eval_medical_record():
    return {
        "input": QueryInput(query="Patient record MRN-987654"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="other", value="MRN-987654")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="other"), "value": Exact(value="MRN-987654")}
            ])
        }
    }


@eval_case(
    name="employee_id",
    agent_class=PIIExtractionAgent,
    description="Employee ID with context",
    tags=["other_pii", "employee", "dev_cases"]
)
def eval_employee_id():
    return {
        "input": QueryInput(query="Staff ID: EMP54321"),
        "expected": PIIExtractionOutput(
            entities=[Entity(type="other", value="EMP54321")]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="other"), "value": Exact(value="EMP54321")}
            ])
        }
    }


# ========== Complex Mixed Cases - 4 cases ==========

@eval_case(
    name="pii_with_transaction_context",
    agent_class=PIIExtractionAgent,
    description="PII mixed with transaction context",
    tags=["complex", "mixed", "dev_cases"]
)
def eval_pii_with_transaction_context():
    return {
        "input": QueryInput(query="Transfer to Bob Smith, use card **** 7890 exp 04/25"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="card_number", value="7890"),
                Entity(type="card_expiry", value="04/25")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="card_number"), "value": Substring(value="7890")},
                {"type": Exact(value="card_expiry"), "value": Substring(value="04/25")}
            ])
        }
    }


@eval_case(
    name="credentials_with_merchant",
    agent_class=PIIExtractionAgent,
    description="Login credentials mentioned with merchant",
    tags=["complex", "mixed", "dev_cases"]
)
def eval_credentials_with_merchant():
    return {
        "input": QueryInput(query="eBay login is mary_seller_99 password Vintage2025"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="username", value="mary_seller_99"),
                Entity(type="password", value="Vintage2025")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="username"), "value": Exact(value="mary_seller_99")},
                {"type": Exact(value="password"), "value": Exact(value="Vintage2025")}
            ])
        }
    }


@eval_case(
    name="name_with_credentials",
    agent_class=PIIExtractionAgent,
    description="Name exposed with account credentials",
    tags=["complex", "name", "credentials", "dev_cases"]
)
def eval_name_with_credentials():
    return {
        "input": QueryInput(query="User: Michael Brown, pass: Ocean123Wave!"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="name", value="Michael Brown"),
                Entity(type="password", value="Ocean123Wave!")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="name"), "value": Exact(value="Michael Brown")},
                {"type": Exact(value="password"), "value": Exact(value="Ocean123Wave!")}
            ])
        }
    }


@eval_case(
    name="multiple_pii_types",
    agent_class=PIIExtractionAgent,
    description="Multiple different PII types together",
    tags=["complex", "multiple", "dev_cases"]
)
def eval_multiple_pii_types():
    return {
        "input": QueryInput(query="Contact: anna@example.org, phone 07123456789, NHS 1112223334"),
        "expected": PIIExtractionOutput(
            entities=[
                Entity(type="email", value="anna@example.org"),
                Entity(type="phone", value="07123456789"),
                Entity(type="nhs_number", value="1112223334")
            ]
        ),
        "field_validations": {
            "entities": ListMatches(items=[
                {"type": Exact(value="email"), "value": Substring(value="anna@")},
                {"type": Exact(value="phone"), "value": Exact(value="07123456789")},
                {"type": Exact(value="nhs_number"), "value": Exact(value="1112223334")}
            ])
        }
    }


# ========== Negative Cases - 3 cases ==========

@eval_case(
    name="test_data_not_extracted",
    agent_class=PIIExtractionAgent,
    description="Test/placeholder data should not be extracted",
    tags=["negative", "test_data", "dev_cases"]
)
def eval_test_data_not_extracted():
    return {
        "input": QueryInput(query="For testing use test@example.com and card 0000-0000-0000-0000"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="no_pii_general_query",
    agent_class=PIIExtractionAgent,
    description="General query with no PII",
    tags=["negative", "general", "dev_cases"]
)
def eval_no_pii_general_query():
    return {
        "input": QueryInput(query="How do I update my preferences in the system?"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }


@eval_case(
    name="multiple_merchants_no_pii",
    agent_class=PIIExtractionAgent,
    description="Multiple merchants but no PII",
    tags=["negative", "merchant", "multiple", "dev_cases"]
)
def eval_multiple_merchants_no_pii():
    return {
        "input": QueryInput(query="Transactions at ASDA, Waitrose, and Morrisons last month"),
        "expected": PIIExtractionOutput(entities=[]),
        "field_validations": {
            "entities": ListMatches(items=[])
        }
    }
