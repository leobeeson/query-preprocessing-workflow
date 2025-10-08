# Data Catalogue: Transaction and Budget Data

## Overview
This data catalogue documents `mii` synthetic test data containing:
- **Transaction data**: 119,984 customer transactions from 22 accounts spanning 2023-2025
- **Budget data**: Customer-defined spending budgets by category

The transaction data has been enriched with merchant identification, spending categorization, and carbon footprint calculations through the MIMO enrichment system.

### Purpose
This catalogue provides comprehensive field-level documentation to support:
- Natural language-to-SQL semantic layer development
- Transaction analysis and reporting
- Budget tracking and overspending detection
- Data integration and ETL processes
- Query optimization and indexing strategies

### What's Inside
- **Detailed field descriptions**: Purpose, characteristics, usage patterns, and semantic layer suitability for each field
- **Budget system documentation**: How budgets work and how to detect budget exceedances
- **Statistical profiling**: Cardinality analysis, null percentages, and data type information
- **Semantic classification**: Field types (categorical, continuous, temporal, identifiers)
- **Data quality insights**: Coverage, completeness, and analytical limitations

## Data Sources

### Transaction Data
- **DynamoDB Table**: `aiincd2-transactions-enriched-table`
- **S3 Backup Location**: `s3://649669169886-eu-west-1-prophet-aiincd2-emr-hive-metastore/backup_test/latest_dynamo_combined.csv`
- **Total Records**: 119,984 transactions
- **Date Range**: 2023-2025
- **Fields**: 23 fields (22 business fields + balance)

### Budget Data
- **DynamoDB Table**: `aiinc2-budgets-config-table`
- **Records**: Customer budgets by category
- **Key Fields**: customer_id, category_id, amount, deleted, last_modified_timestamp

### Reference Data
- **Category Mapping**: Maps category UUIDs to human-readable category names with tier hierarchy (tier_1, tier_2, tier_3)
- **Additional Master Data**: Various reference tables shared by colleagues (locations not specified in this document)

## Dataset Statistics

### Transaction Dataset Summary
- **Total Transactions**: 119,984
- **Unique Accounts**: 22
- **Date Coverage**: 2023-2025 (732 unique dates)
- **Transaction Types**: 2 (spending, income)
- **Merchant Categories**: 45 unique category UUIDs
- **Merchant Brands**: 321 unique display names

### Budget Dataset Summary
- **Budget Records**: Customer-defined budgets per category
- **Budget Application**: Fixed threshold amounts applied monthly
- **Active Budgets**: Filtered by deleted = false

## Field Classification Summary

The following table provides a high-level classification of all transaction fields by their semantic type and usage:

| Column | Field Type | Rationale |
|--------|-----------|-----------|
| transaction_type | categorical | Two values: spending/income. Used for filtering and grouping transactions. |
| spending_type | categorical | Two values: day-to-day/regular. Used for categorizing spending behavior. |
| record_creation_timestamp | temporal | Batch processing timestamp. Only 2 values suggest batch loading times. |
| transaction_status | categorical | Single value: booked. Status enumeration (though currently only one state). |
| proprietary_bank_transaction_code | categorical | 13 transaction type codes (POS, DPC, D/D, etc.). Used for transaction classification. |
| mimo_account_id | identifier_entity | 22 unique hashed account identifiers. Identifies customers/accounts in MIMO system. |
| prophet_account_id | identifier_entity | 22 unique account identifiers. Identifies customers/accounts in Prophet system. |
| agrmnt_id | identifier_entity | 22 unique agreement IDs. Identifies customer agreements/accounts. |
| category_id | categorical | 45 category UUIDs representing transaction categories. Primary categorical dimension for analysis. |
| mcc | categorical | 101 Merchant Category Codes. Standard industry categorization system. |
| recurring_payment_type | categorical | Type of recurring payment (SUBSCRIPTION). Sparse field (99.23% null) only for recurring transactions. |
| merchant_brand_code | categorical | 188 internal merchant brand codes. Used for merchant identification and grouping. |
| display_narrative | categorical | 321 merchant brand names. User-facing merchant categorization. |
| clean_narrative | categorical | 379 cleaned merchant descriptions. Standardized merchant names with location. |
| mimo_match_id | identifier_enrichment | 384 matching identifiers. Technical key for transaction matching/enrichment logic. |
| transaction_booking_timestamp | temporal | 732 unique dates (2023-2025). Transaction booking date for temporal analysis. |
| recurring_payment_id | identifier_entity | 29 recurring payment IDs. Identifies unique recurring payment arrangements. Sparse (99.23% null). |
| amount | continuous | 15,180 unique transaction amounts. Decimal values representing money transferred. |
| balance | continuous | Account balance after transaction applied. Critical for balance-based queries and overdraft detection. |
| total_kg_co2e | continuous | 45,085 unique CO2 values. Decimal measurements of carbon footprint. |
| mimo_transaction_id | identifier_transaction | 100% unique. MIMO system transaction identifier (MD5 hash). |
| prophet_transaction_id | identifier_transaction | 100% unique. Prophet system transaction identifier. |
| external_transaction_id | identifier_transaction | 100% unique. External system transaction identifier. |

## Statistical Profile

The following table provides detailed statistical characteristics for each field:

| Column | Data Type | Unique Count | Non-Null Count | Null Count | Total Count | Cardinality % | Null % | Cardinality Profile | Sample Values |
|--------|-----------|--------------|----------------|------------|-------------|---------------|--------|---------------------|---------------|
| transaction_type | object | 2 | 119,984 | 0 | 119,984 | 0.0 | 0.0 | low_cardinality | "spending", "income", "spending", "income", "income" |
| spending_type | object | 2 | 119,984 | 0 | 119,984 | 0.0 | 0.0 | low_cardinality | "day-to-day", "regular", "regular", "day-to-day", "day-to-day" |
| record_creation_timestamp | object | 2 | 119,984 | 0 | 119,984 | 0.0 | 0.0 | low_cardinality | "2025-08-06T14:29:30.000", "2025-08-06T14:29:30.000", "2025-08-20T13:39:20.000" |
| transaction_status | object | 1 | 119,984 | 0 | 119,984 | 0.0 | 0.0 | low_cardinality | "booked", "booked", "booked", "booked", "booked" |
| proprietary_bank_transaction_code | object | 13 | 119,984 | 0 | 119,984 | 0.01 | 0.0 | low_cardinality | "POS", "DPC", "D/D", "BAC", "CHP" |
| mimo_account_id | object | 22 | 119,984 | 0 | 119,984 | 0.02 | 0.0 | low_cardinality | "693733aeb89df94e1aeabec9b4ed50ad", "39e3a030ed0207eb6febd62a74933e61" |
| prophet_account_id | object | 22 | 119,984 | 0 | 119,984 | 0.02 | 0.0 | low_cardinality | "560000_10000013", "560000_10000011", "560000_10000000" |
| agrmnt_id | int64 | 22 | 119,984 | 0 | 119,984 | 0.02 | 0.0 | low_cardinality | "5560000012", "5560000010", "5560000000", "5560000000", "5560000019" |
| category_id | object | 45 | 119,984 | 0 | 119,984 | 0.04 | 0.0 | low_cardinality | "d6a42dad-0e00-336d-08dd-a5450768a1cc", "d49120d2-8be9-17ad-c494-521779c207f3" |
| mcc | int64 | 101 | 119,984 | 0 | 119,984 | 0.08 | 0.0 | low_cardinality | "5948", "20033", "5261", "20001", "9399" |
| recurring_payment_type | object | 1 | 920 | 119,064 | 119,984 | 0.11 | 99.23 | sparse | "SUBSCRIPTION", "SUBSCRIPTION", "SUBSCRIPTION" |
| merchant_brand_code | float64 | 188 | 100,200 | 19,784 | 119,984 | 0.19 | 16.49 | low_cardinality | "200581.0", "211172.0", "278.0", "85362.0", "307.0" |
| display_narrative | object | 321 | 119,984 | 0 | 119,984 | 0.27 | 0.0 | low_cardinality | "Lego", "B T GB", "Dobbies", "DMC11 HBOS RETAIL TRX", "Edinburgh Council" |
| clean_narrative | object | 379 | 119,984 | 0 | 119,984 | 0.32 | 0.0 | low_cardinality | "LEGO STORE GLASGOWGLASGOW GB", "B T GB*", "DOBBIES LISBURN GB" |
| mimo_match_id | object | 384 | 119,984 | 0 | 119,984 | 0.32 | 0.0 | low_cardinality | "35365fb4bc88ead627e9ab7b4f67ba4c", "ee7ba0c6467efa7cd2b48989f6483231" |
| transaction_booking_timestamp | object | 732 | 119,984 | 0 | 119,984 | 0.61 | 0.0 | low_cardinality | "2024-06-24", "2024-04-25", "2023-11-30", "2024-11-09", "2023-08-13" |
| recurring_payment_id | object | 29 | 920 | 119,064 | 119,984 | 3.15 | 99.23 | sparse | "292_292", "294_294", "5_5", "292_292", "121_121" |
| amount | float64 | 15,180 | 119,984 | 0 | 119,984 | 12.65 | 0.0 | high_cardinality | "-50.63", "-54.5", "-112.12", "-82.78", "-83.62" |
| total_kg_co2e | float64 | 45,085 | 104,047 | 15,937 | 119,984 | 43.33 | 13.28 | high_cardinality | "16.947", "9.508", "12.977", "11.068", "8.514" |
| mimo_transaction_id | object | 119,984 | 119,984 | 0 | 119,984 | 100.0 | 0.0 | unique | "c9ff7659bef87a88b26ec83ec8a08584", "4f799614b54f1fb26e6f8fa1cf51da09" |
| prophet_transaction_id | int64 | 119,984 | 119,984 | 0 | 119,984 | 100.0 | 0.0 | unique | "89710219102733", "79106734579222", "39781224025152" |
| external_transaction_id | int64 | 119,984 | 119,984 | 0 | 119,984 | 100.0 | 0.0 | unique | "10008594066050345", "10019032812627930", "10019738339627134" |

## Detailed Field Descriptions

This section provides comprehensive documentation for each field in the transaction dataset.

### Transaction Identifiers

**`external_transaction_id`** (String, identifier_transaction)
- **Purpose**: Unique identifier from the external banking system
- **Characteristics**: 100% unique (119,984 distinct values), numeric format
- **Usage**: Primary key for deduplication, transaction lookup in external systems
- **Example**: "10008594066050345"

**`prophet_transaction_id`** (Integer, identifier_transaction)
- **Purpose**: Unique identifier within the Prophet system
- **Characteristics**: 100% unique (119,984 distinct values), integer format
- **Usage**: Primary key for internal transaction tracking
- **Example**: "89710219102733"

**`mimo_transaction_id`** (String Hash, identifier_transaction)
- **Purpose**: Unique identifier within the MIMO enrichment system
- **Characteristics**: 100% unique (119,984 distinct values), MD5 hash format (32 characters)
- **Usage**: Primary key for linking to MIMO enrichment data
- **Example**: "c9ff7659bef87a88b26ec83ec8a08584"

### Account/Entity Identifiers

**`prophet_account_id`** (String, identifier_entity)
- **Purpose**: Identifies the customer account in the Prophet system
- **Characteristics**: 22 unique accounts across 119,984 transactions (0.02% cardinality)
- **Usage**: Used to slice/group transactions by customer, not for categorical analysis
- **Format**: Pattern "560000_10000XXX" where XXX varies by account
- **Example**: "560000_10000013"
- **Note**: Dataset represents 22 distinct customer accounts

**`agrmnt_id`** (Integer, identifier_entity)
- **Purpose**: Agreement or account identifier
- **Characteristics**: 22 unique values (0.02% cardinality), corresponds 1:1 with prophet_account_id
- **Usage**: Alternative account identifier, likely used for agreement/contract referencing
- **Format**: Numeric, pattern "55600000XX"
- **Example**: "5560000012"

**`mimo_account_id`** (String Hash, identifier_entity)
- **Purpose**: Hashed account identifier in the MIMO system
- **Characteristics**: 22 unique MD5 hashes (0.02% cardinality)
- **Usage**: Privacy-preserving account identifier for MIMO enrichment system
- **Format**: MD5 hash (32 characters)
- **Example**: "693733aeb89df94e1aeabec9b4ed50ad"

**`recurring_payment_id`** (String, identifier_entity)
- **Purpose**: Identifies unique recurring payment arrangements (subscriptions, standing orders)
- **Characteristics**: 29 unique IDs, but 99.23% null (only 920 transactions are recurring)
- **Usage**: Groups transactions that are part of the same recurring payment setup
- **Format**: Pattern "XXX_XXX" (appears to be ID_ID format)
- **Example**: "292_292", "5_5"
- **Sparsity**: Only applicable to 0.77% of transactions

### Enrichment Keys

**`mimo_match_id`** (String Hash, identifier_enrichment)
- **Purpose**: Technical identifier for transaction matching/enrichment logic in MIMO system
- **Characteristics**: 384 unique values (0.32% cardinality), MD5 hash format
- **Usage**: Groups transactions that match to the same enrichment rule (specific purpose unknown)
- **Example**: "35365fb4bc88ead627e9ab7b4f67ba4c"
- **Note**: Multiple transactions can share the same mimo_match_id - 384 distinct groupings across 119,984 transactions

### Financial Data

**`amount`** (Decimal, continuous)
- **Purpose**: Monetary value of the transaction
- **Characteristics**: 15,180 unique values (12.65% cardinality), no nulls
- **Range**: Negative for spending/outflows, positive for income/inflows
- **Usage**: Primary financial metric for aggregations, averages, totals
- **Examples**: "-50.63" (spending), "8757.24" (income)
- **Semantic Layer**: Essential for "sum of spending", "average transaction", "total income" queries

**`balance`** (Decimal, continuous)
- **Purpose**: Account balance after this transaction has been applied
- **Characteristics**: Running balance following each transaction
- **Usage**: Critical for balance-based queries:
  - **Current balance**: Get most recent transaction's balance field
  - **Historical balance**: Filter to specific date, get last transaction's balance
  - **Overdraft detection**: WHERE balance < 0 identifies overdrawn periods
  - **Threshold monitoring**: Track when balance crosses thresholds (e.g., < £2000)
  - **Balance trends**: Analyze balance patterns over time
  - **Correlation analysis**: Relate balance levels to spending patterns
- **Format**: Decimal value representing post-transaction account balance
- **Semantic Layer**: Enables "current balance", "was I overdrawn", "balance at end of month" queries
- **Note**: Each transaction includes post-transaction balance, eliminating need for balance recalculation

**`total_kg_co2e`** (Decimal, continuous)
- **Purpose**: Estimated carbon footprint of the transaction in kilograms of CO2 equivalent
- **Characteristics**: 45,085 unique values (43.33% cardinality), 13.28% null
- **Coverage**: Available for 86.7% of transactions (104,047 records)
- **Usage**: Environmental impact analysis, sustainability metrics
- **Examples**: "16.947", "9.508"
- **Semantic Layer**: Used for "carbon footprint of spending", "environmental impact" queries
- **Note**: Missing for some transaction types (likely non-merchant transactions)

### Temporal Fields

**`transaction_booking_timestamp`** (Date, temporal)
- **Purpose**: The date when the transaction was officially booked to the account
- **Characteristics**: 732 unique dates (0.61% cardinality), covers 2023-2025
- **Format**: ISO date format "YYYY-MM-DD"
- **Usage**: Primary temporal dimension for time-series analysis, trend analysis, date filtering
- **Examples**: "2024-06-24", "2023-11-30"
- **Semantic Layer**: Critical for "transactions in January", "spending last month", "year-over-year" queries

**`record_creation_timestamp`** (Timestamp, temporal)
- **Purpose**: Timestamp when the record was created/loaded into the system
- **Characteristics**: Only 2 unique values (0.00% cardinality) - "2025-08-06T14:29:30.000" and "2025-08-20T13:39:20.000"
- **Format**: ISO 8601 with millisecond precision
- **Usage**: Data lineage/ETL tracking, not for business analysis
- **Note**: Indicates batch processing - data loaded in two separate batches

### Categorical Dimensions

**`transaction_type`** (String, categorical)
- **Purpose**: High-level classification of transaction direction
- **Values**: 2 unique values (100% coverage)
  - `spending`: Outgoing payment (negative amount) - expenditures, purchases, payments
  - `income`: Incoming payment (positive amount) - salary, refunds, deposits
- **Usage**: Primary filter for income vs. expenditure analysis
- **Semantic Layer**: Essential for "spending" vs "income" queries

**`transaction_status`** (String, categorical)
- **Purpose**: Current status of the transaction in the banking system
- **Values**: 1 unique value (100% coverage)
  - `booked`: Transaction has been fully processed and posted to account
- **Usage**: Limited analytical value as all transactions have same status
- **Note**: Dataset may only contain finalized transactions; pending/cancelled likely excluded

**`spending_type`** (String, categorical)
- **Purpose**: Classifies spending behavior pattern
- **Values**: 2 unique values (100% coverage)
  - `day-to-day`: Includes subscriptions (all 920 SUBSCRIPTION transactions) and other spending
  - `regular`: Meaning unclear without further analysis - does NOT include subscriptions
- **Usage**: Spending pattern classification with unknown semantic distinction
- **Semantic Layer**: Use with caution - field meaning requires further investigation
- **Note**: The semantic distinction between "day-to-day" and "regular" is not evident from the data alone

**`recurring_payment_type`** (String, categorical)
- **Purpose**: Specifies the type of recurring payment arrangement
- **Values**: 1 unique value (when present)
  - `SUBSCRIPTION`: Recurring subscription payment
- **Sparsity**: 99.23% null - only populated for 920 recurring transactions (0.77%)
- **Usage**: Identifies subscription-based payments when present
- **Note**: All 920 SUBSCRIPTION transactions have `spending_type = "day-to-day"` (not "regular")
- **Analytical value**: Very sparse, limited use at dataset level

**`proprietary_bank_transaction_code`** (String, categorical)
- **Purpose**: NatWest's internal classification of transaction method/channel
- **Values**: 13 unique codes (100% coverage)
  - `POS`: Point of Sale transaction - card payment at physical merchant terminal
  - `DPC`: Direct Banking by PC - online banking payment/transfer
  - `D/D`: Direct Debit - pre-authorized recurring payment pulled by merchant/service provider
  - `BAC`: Automated Credit (BACS) - Bankers' Automated Clearing Services payment
  - `CHP`: CHAPS payment - Clearing House Automated Payment System (same-day, high-value)
  - `ATM`: Automated Teller Machine - cash withdrawal or deposit
  - `S/O`: Standing Order - customer-initiated recurring payment
  - `IBP`: Inter-Branch Payment - internal bank transfer between branches
  - `ITL`: International - international transaction or transfer
  - `LON`: Loan - loan-related transaction (repayment or disbursement)
  - `SBT`: Screen Based Transaction - transaction via screen-based banking (likely mobile/tablet)
  - `CHG`: Charge - bank charge or fee
  - `TSU`: Telephone Banking - transaction initiated via telephone banking
- **Usage**: Analyze payment methods, channel usage, transaction types
- **Semantic Layer**: Valuable for "card payments", "direct debits", "international transactions" queries
- **Source**: Official NatWest transaction codes (verified from NatWest support documentation)

**`category_id`** (UUID, categorical)
- **Purpose**: Links transaction to a standardized spending category in a category dimension table
- **Values**: 45 unique UUIDs (100% coverage, 0.04% cardinality)
- **Format**: UUID with variant formatting (e.g., "d6a42dad-0e00-336d-08dd-a5450768a1cc")
- **Usage**: Primary categorical dimension for spending analysis by category
- **Semantic Layer**: Critical for "spending on groceries", "entertainment expenses" type queries
- **Note**: Foreign key to categories table - UUIDs themselves have no semantic meaning without lookup

**`mcc`** (Integer, categorical)
- **Purpose**: Merchant Category Code - standardized industry classification system
- **Values**: 101 unique codes (100% coverage, 0.08% cardinality)
- **Standard**: ISO 18245 standard maintained by card networks (Visa, Mastercard)
- **Format**: Numeric codes (e.g., "5948" = Toy Stores, "20033" = Telecommunications)
- **Usage**: Industry-level spending analysis, merchant classification
- **Semantic Layer**: Useful for industry-specific queries if MCC lookup table available
- **Examples**: "5411" (Grocery Stores), "5812" (Restaurants), "4511" (Airlines)

**`merchant_brand_code`** (String, categorical)
- **Purpose**: Internal code identifying specific merchant brand/chain
- **Values**: 188 unique codes (0.19% cardinality), 16.49% null
- **Format**: Numeric codes (e.g., "200581", "211172", "85362")
- **Usage**: Brand-level spending analysis, specific merchant identification
- **Nullability**: Missing for ~20k transactions (likely non-merchant transactions like transfers)
- **Semantic Layer**: Enables brand-specific queries if brand lookup table available

**`display_narrative`** (String, categorical)
- **Purpose**: User-facing, cleaned merchant/brand name
- **Values**: 321 unique names (0.27% cardinality), 100% coverage
- **Format**: Human-readable brand names (e.g., "Lego", "Tesco", "Amazon Prime")
- **Usage**: Most user-friendly merchant identifier for analysis and reporting
- **Semantic Layer**: Ideal for "spending at Tesco", "Amazon transactions" type queries
- **Examples**: "Lego", "B T GB", "Edinburgh Council", "Tesco"

**`clean_narrative`** (String, categorical)
- **Purpose**: Standardized merchant description with location details
- **Values**: 379 unique descriptions (0.32% cardinality), 100% coverage
- **Format**: Merchant name + location + country code (e.g., "LEGO STORE GLASGOWGLASGOW GB")
- **Usage**: More detailed merchant identification including location context
- **Semantic Layer**: Useful for location-specific merchant queries
- **Examples**: "LEGO STORE GLASGOWGLASGOW GB", "TESCO STORES MID GLAMORGAN GB"
- **Note**: May contain duplicate location text (e.g., "GLASGOWGLASGOW")

## Semantic Layer Considerations

When building a natural language-to-SQL interface, the following fields are most suitable for different query patterns:

### Primary Dimensions for Filtering/Grouping
- **`transaction_type`**: Essential for income vs. spending queries (clear semantics)
- **`proprietary_bank_transaction_code`**: Enables payment method/channel queries (verified definitions)
- **`category_id`**: Critical dimension (requires category lookup table for semantic meaning)
- **`display_narrative`**: Most user-friendly merchant identifier
- **`transaction_booking_timestamp`**: Primary temporal dimension
- **`spending_type`**: Classification exists but semantic meaning unclear (requires investigation)

### Measures for Aggregation
- **`amount`**: Primary financial metric (sum, average, count)
- **`total_kg_co2e`**: Environmental impact metric

### Identifiers (Not for User Queries)
- Transaction IDs: Used for deduplication, not for semantic queries
- Account IDs: May be used for customer segmentation but not exposed in natural language
- Enrichment keys: Technical keys, not for user-facing queries

### Fields Requiring Lookup Tables
- **`category_id`**: Needs category name mapping (45 categories)
- **`mcc`**: Needs MCC description mapping (101 codes)
- **`merchant_brand_code`**: Needs brand name mapping (188 codes)

### Low-Value Fields for Semantic Layer
- **`transaction_status`**: Single value (all "booked") - no filtering value
- **`record_creation_timestamp`**: ETL metadata, not business data
- **`recurring_payment_type`**: Too sparse (99.23% null)
- **`recurring_payment_id`**: Too sparse, technical identifier

## Budget System

### Overview
The budget system allows customers to set spending limits by category. Budget data is stored separately from transaction data and linked via `category_id`.

**File Location**: `ai_docs/context/docs/query_preprocessing/budgets.csv`

### Budget Fields

**`customer_id`** (String)
- **Purpose**: Links budget to specific customer
- **Usage**: Requires mapping to transaction account identifiers (mimo_account_id, prophet_account_id, agrmnt_id)
- **Note**: Customer-to-account mapping table exists for joining transaction and budget data

**`budget_id`** (String)
- **Purpose**: Unique identifier for each budget entry
- **Format**: Composite format "{customer_id}-{category_id}"
- **Example**: "3701555829-e63f7849-c0c0-012e-440e-3d0bc2c8ea94"

**`category_id`** (UUID)
- **Purpose**: Links budget to spending category (matches transaction category_id)
- **Format**: UUID (e.g., "e63f7849-c0c0-012e-440e-3d0bc2c8ea94" for Groceries)
- **Usage**: Join key between budgets and transactions - filter transactions by category_id to calculate spending against budget

**`amount`** (Decimal)
- **Purpose**: Budget threshold amount
- **Semantics**: Fixed spending limit that applies on an ongoing basis (typically monthly)
- **Usage**: Compare aggregated spending to this threshold to detect budget exceedances
- **Examples**: "80" (£80 groceries budget), "100" (£100 entertainment budget)

**`deleted`** (Boolean)
- **Purpose**: Indicates if budget is active or has been deleted
- **Values**: "true" (deleted/inactive), "false" (active)
- **Usage**: Filter by deleted = false to get only active budgets

**`description`** (String)
- **Purpose**: Human-readable description of budget category
- **Format**: Category hierarchy path (e.g., "expenses:groceries", "expenses:eating-out")
- **Examples**: "expenses:groceries", "expenses:entertainment", "transfers:other"

**`title`** (String)
- **Purpose**: Display title for budget (typically same as description)
- **Examples**: "expenses:groceries", "expenses:wellness"

**`last_modified_timestamp`** (Timestamp ISO 8601)
- **Purpose**: When budget was last modified or created
- **Format**: ISO 8601 with millisecond precision (e.g., "2025-08-14T11:57:58.917")
- **Usage**: Determines when budget became active - use to check if budget existed during specific time periods

**`record_creation_timestamp`** (Timestamp ISO 8601)
- **Purpose**: When budget record was originally created
- **Format**: ISO 8601 with millisecond precision
- **Usage**: Audit trail for budget creation

### How Budgets Work

**Budget Semantics**:
- Budgets are **fixed threshold amounts**, not time-bound totals
- They apply on an **ongoing basis** (typically monthly periods)
- When a budget is set at £80 for groceries, this means the user intends to limit grocery spending to £80 per month

**Detecting Budget Exceedances**:

To determine if a user exceeded their budget:

1. **Join Data**:
   - Transactions → account_id → customer_id (via mapping table) → budgets
   - Join on `category_id` to match transaction category with budget category

2. **Filter Active Budgets**:
   - WHERE deleted = false
   - Check last_modified_timestamp to ensure budget was active during period being analyzed

3. **Aggregate Spending**:
   - Group transactions by time period (typically monthly)
   - SUM(ABS(amount)) for transactions matching budget category_id
   - Filter by transaction_type = 'spending' if needed

4. **Compare to Threshold**:
   - For each time period, compare aggregated spending to budget.amount
   - If period_spending > budget.amount, budget was exceeded in that period

5. **Count Exceedances**:
   - COUNT periods where spending exceeded budget threshold
   - Useful for queries like "How many times did I exceed my grocery budget last year?"

**Example Query Logic** (Groceries budget for 2024):
```
1. Get customer's grocery budget:
   - category_id = e63f7849-c0c0-012e-440e-3d0bc2c8ea94 (Groceries)
   - deleted = false
   - budget.amount = £80

2. Calculate monthly grocery spending for 2024:
   - Filter transactions: category_id = groceries, year = 2024
   - GROUP BY MONTH(transaction_booking_timestamp)
   - SUM(ABS(amount)) per month

3. Compare each month:
   - January: £95 > £80 ✓ Exceeded
   - February: £72 < £80 ✗ Within budget
   - March: £88 > £80 ✓ Exceeded
   - ...

4. Result: "You exceeded your grocery budget 2 times in Q1 2024"
```

### Budget Categories Available

Common budget categories found in the data:
- **expenses:groceries** (e63f7849-c0c0-012e-440e-3d0bc2c8ea94)
- **expenses:eating-out** (ad2b8c89-ca33-1d71-04a8-84d087ae76b1)
- **expenses:entertainment** (2b01b420-7e0e-bcee-fbf9-cc79dfd2a5e4)
- **expenses:transport** (0dd00427-7f5b-bbff-d7c5-f65743115d73)
- **expenses:shopping** (2d997971-dc47-0bfa-c951-8f34630b910d)
- **expenses:home** (4e97a163-6aed-401e-7ab4-cde2c81a0f52)
- **expenses:wellness** (52974940-22bb-5880-1b55-af7070bb804b)
- **expenses:bills** (7186ed64-50c3-96c1-85d8-e6af2b21407c)
- **expenses:misc** (8c983c86-5b8a-19f9-9318-00620a863b5f)
- **transfers:other** (d3404628-3070-8ad8-5fb6-d742ab0f3563)

See `mapping_table_unique_categories.csv` for complete category hierarchy with tier 1, tier 2, tier 3 breakdowns.

### Semantic Layer Usage

Budget-related queries that can be processed:
- "Did I exceed my [category] budget [time period]?" - Compare aggregated spending to budget threshold
- "How many times did I exceed my budget last year?" - Count periods where spending > budget.amount
- "How much am I over/under budget this month?" - Calculate difference between actual spending and budget.amount
- "What's my budget for [category]?" - Look up budget.amount for specified category
- "Which categories am I over budget on?" - Find all categories where spending > budget for current period

**Required Data Joins**:
- Customer-to-account mapping (to link transaction account IDs to budget customer_id)
- Category mapping (for human-readable category names in queries)

## Field Classification

### Methodology

Field classification uses a two-dimensional approach separating **statistical profiling** from **semantic classification**:

#### 1. Statistical Profiling (Automated)

The `analyze_cardinality.py` script performs statistical profiling using chunked processing to handle 119,984 transactions efficiently without loading all data into memory. It calculates:

**Key Metrics:**
- **Cardinality Percentage**: (Unique values / Non-null values) × 100
- **Null Percentage**: (Null values / Total values) × 100
- **Data Type**: Pandas inferred dtype (object, int64, float64, etc.)
- **Sample Values**: First 5 unique values for inspection

**Cardinality Profile** (Statistical Classification):
1. **low_cardinality** (cardinality_pct < 10%): Few distinct values
2. **high_cardinality** (10% ≤ cardinality_pct < 95%): Moderate variation
3. **unique** (cardinality_pct ≥ 95%): Unique or near-unique values
4. **sparse** (null_pct ≥ 90%): Insufficient non-null data

**Important Note:** Cardinality percentage is calculated based only on non-null values to avoid distortion from sparse fields. For example, `recurring_payment_id` has only 920 non-null values (0.77% of dataset), and among those non-null values, there are 29 unique values (3.15% cardinality).

#### 2. Semantic Classification (Manual)

Based on statistical profiling results and domain knowledge, each field is assigned a **semantic field type** in `field_type_mapping.csv`:

**Field Types:**
- **categorical**: Unordered groups for filtering/aggregation (e.g., `transaction_type`, `category_id`, `mcc`)
- **continuous**: Numerical measurements (e.g., `amount`, `total_kg_co2e`)
- **temporal**: Dates and timestamps (e.g., `transaction_booking_timestamp`, `record_creation_timestamp`)
- **identifier_transaction**: Unique transaction identifiers (e.g., `external_transaction_id`)
- **identifier_entity**: Entity identifiers like accounts/customers (e.g., `prophet_account_id`, `agrmnt_id`)
- **identifier_enrichment**: Technical matching/joining keys (e.g., `mimo_match_id`)

### Field Classification Summary

#### Categorical Fields (11 columns)
Fields suitable for grouping, filtering, and aggregation:

| Column | Unique Values | Cardinality % | Null % | Description |
|--------|--------------|---------------|---------|-------------|
| `transaction_type` | 2 | 0.00% | 0.00% | spending/income |
| `spending_type` | 2 | 0.00% | 0.00% | day-to-day/regular |
| `transaction_status` | 1 | 0.00% | 0.00% | booked |
| `proprietary_bank_transaction_code` | 13 | 0.01% | 0.00% | POS, DPC, D/D, BAC, CHP |
| `category_id` | 45 | 0.04% | 0.00% | Transaction category UUIDs |
| `mcc` | 101 | 0.08% | 0.00% | Merchant Category Codes |
| `merchant_brand_code` | 188 | 0.19% | 16.49% | Internal merchant codes |
| `display_narrative` | 321 | 0.27% | 0.00% | Merchant brand names |
| `clean_narrative` | 379 | 0.32% | 0.00% | Standardized merchant descriptions |
| `recurring_payment_type` | 1 | 0.11% | 99.23% | Subscription type (sparse) |

#### Continuous Fields (2 columns)
Numerical measurements:

| Column | Unique Values | Cardinality % | Null % | Description |
|--------|--------------|---------------|---------|-------------|
| `amount` | 15,180 | 12.65% | 0.00% | Transaction amount (money) |
| `total_kg_co2e` | 45,085 | 43.33% | 13.28% | Carbon footprint measurement |

#### Temporal Fields (2 columns)
Date and timestamp fields:

| Column | Unique Values | Cardinality % | Null % | Description |
|--------|--------------|---------------|---------|-------------|
| `transaction_booking_timestamp` | 732 | 0.61% | 0.00% | Transaction booking date (2023-2025) |
| `record_creation_timestamp` | 2 | 0.00% | 0.00% | Batch processing timestamp |

#### Transaction Identifiers (3 columns)
Unique identifiers per transaction:

| Column | Unique Values | Cardinality % | Null % | Description |
|--------|--------------|---------------|---------|-------------|
| `external_transaction_id` | 119,984 | 100.00% | 0.00% | External system ID |
| `prophet_transaction_id` | 119,984 | 100.00% | 0.00% | Prophet system ID |
| `mimo_transaction_id` | 119,984 | 100.00% | 0.00% | MIMO system ID (MD5 hash) |

#### Entity Identifiers (4 columns)
Account and customer identifiers:

| Column | Unique Values | Cardinality % | Null % | Description |
|--------|--------------|---------------|---------|-------------|
| `prophet_account_id` | 22 | 0.02% | 0.00% | Prophet account identifier |
| `agrmnt_id` | 22 | 0.02% | 0.00% | Agreement/account ID |
| `mimo_account_id` | 22 | 0.02% | 0.00% | MIMO account hash |
| `recurring_payment_id` | 29 | 3.15% | 99.23% | Recurring payment ID (sparse) |

#### Enrichment Identifiers (1 column)
Technical matching/joining keys:

| Column | Unique Values | Cardinality % | Null % | Description |
|--------|--------------|---------------|---------|-------------|
| `mimo_match_id` | 384 | 0.32% | 0.00% | Transaction matching identifier |

**Note**: Only 920 transactions (0.77%) are recurring payments, explaining the sparse nature of `recurring_payment_type` and `recurring_payment_id`.

## Data Format Details

### Hash Fields
- All MIMO identifiers (`mimo_transaction_id`, `mimo_account_id`, `mimo_match_id`) are MD5 hashes (32 hexadecimal characters)
- Used for privacy-preserving cross-system referencing

### Date/Time Formats
- **`transaction_booking_timestamp`**: ISO date format "YYYY-MM-DD"
- **`record_creation_timestamp`**: ISO 8601 with millisecond precision "YYYY-MM-DDTHH:MM:SS.SSS"
- Date range: 2023-2025 (732 unique transaction dates)

### Identifier Formats
- **`prophet_account_id`**: String pattern "560000_10000XXX"
- **`agrmnt_id`**: Integer pattern "55600000XX"
- **`category_id`**: UUID with hyphens (e.g., "d6a42dad-0e00-336d-08dd-a5450768a1cc")
- **Transaction IDs**: All 100% unique across 119,984 records

### Null Patterns
- **High sparsity** (>90% null): `recurring_payment_id`, `recurring_payment_type`
- **Moderate nulls** (~13-16%): `total_kg_co2e`, `merchant_brand_code`
- **Complete coverage** (0% null): All other fields

## Files and References

### Generated Files
- **Statistical Profile**: `src/data_catalogue/results/cardinality_analysis.csv` - Automated statistical profiling results
- **Semantic Mapping**: `src/data_catalogue/results/field_type_mapping.csv` - Manual semantic field type classifications with rationale
- **Categorical Values**: `src/data_catalogue/results/categorical_values.md` - All unique values for categorical fields

### Scripts
- **Statistical Profiling**: `src/data_catalogue/analyze_cardinality.py` - Generates cardinality analysis
- **Categorical Values Extraction**: `src/data_catalogue/extract_categorical_values.py` - Extracts unique values for categorical fields

### Usage Notes
- Run `python3 src/data_catalogue/analyze_cardinality.py` to regenerate statistical profiles when data changes
- Run `python3 src/data_catalogue/extract_categorical_values.py` to regenerate categorical values list
- Update `field_type_mapping.csv` when adding new fields or when field semantics change
- The two-dimensional approach (statistical + semantic) ensures both objective metrics and domain expertise inform classification

## Key Dataset Insights

### Coverage and Completeness
- **Total transactions**: 119,984 records spanning 2023-2025 (732 unique dates)
- **Account coverage**: 22 unique customer accounts
- **Carbon footprint data**: Available for 86.7% of transactions (104,047 records)
- **Recurring payments**: Only 0.77% (920 transactions) - very sparse
- **Merchant data**: All transactions have `display_narrative` and `clean_narrative`
- **Missing data**: `merchant_brand_code` missing for 16.49% (non-merchant transactions)

### Data Quality Observations
- All transactions have status "booked" - no pending/cancelled in dataset
- Three parallel identifier systems (external, prophet, mimo) for cross-referencing
- Record creation timestamps suggest two batch loads (Aug 6 and Aug 20, 2025)
- Some clean narratives have duplicate location text (e.g., "GLASGOWGLASGOW")
- Category IDs use UUID format but require lookup table for semantic meaning

### Enrichment Data
- **Merchant enrichment**: 321 distinct brands via `display_narrative`
- **Category enrichment**: 45 spending categories via `category_id`
- **MCC enrichment**: 101 industry codes via `mcc`
- **Carbon enrichment**: CO2 estimates for 86.7% of transactions
- **Matching identifiers**: 384 distinct `mimo_match_id` values for enrichment grouping

### Transaction Distribution
- **Transaction types**: Mix of spending (negative amount) and income (positive amount)
- **Spending classification**: Both "day-to-day" and "regular" categories present (semantic distinction unclear)
- **Payment methods**: 13 different transaction codes (POS, DPC, D/D, etc.)
- **Amount range**: 15,180 distinct transaction amounts (12.65% cardinality)

### Analytical Limitations
- No access to actual category names (only UUIDs)
- No MCC description lookup available
- No merchant brand code mapping
- Single transaction status limits filtering options
- Recurring payment data too sparse for meaningful analysis

---

## Next Steps: Semantic Layer Development

This catalogue is designed to support natural language-to-SQL semantic layer development. Key considerations:

### Recommended Dimensions for Semantic Layer
1. **Transaction Type** (`transaction_type`) - income vs. spending (clear semantics)
2. **Payment Method** (`proprietary_bank_transaction_code`) - 13 payment types with verified NatWest definitions
3. **Merchant** (`display_narrative`) - 321 merchant brands, user-friendly names
4. **Date** (`transaction_booking_timestamp`) - temporal analysis
5. **Spending Type** (`spending_type`) - day-to-day vs. regular (semantic distinction unclear, requires investigation)

### Required Lookup Tables
To enable semantic queries, the following dimension tables are needed:
- **Category names**: Map `category_id` (45 UUIDs) to human-readable category names
- **MCC descriptions** (optional): Map `mcc` codes to industry descriptions
- **Brand names** (optional): Map `merchant_brand_code` to brand names

### Query Pattern Examples
With this data structure, the semantic layer should support queries like:
- "Show my spending at Tesco last month" (uses `display_narrative`, `transaction_booking_timestamp`)
- "How much did I spend using my card vs direct debits?" (uses `proprietary_bank_transaction_code`)
- "What's the carbon footprint of my grocery shopping?" (uses `total_kg_co2e`, requires category lookup)
- "Show income transactions in Q1 2024" (uses `transaction_type`, `transaction_booking_timestamp`)
- "What are my subscription payments?" (uses `recurring_payment_type`, but very sparse - only 920 transactions)

See `results/categorical_values.md` for complete lists of all categorical field values.
