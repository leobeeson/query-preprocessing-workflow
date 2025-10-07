import pandas as pd
from pathlib import Path
from collections import defaultdict

def extract_categorical_values(csv_path: str, mapping_path: str, chunk_size: int = 10000):
    """
    Extract unique values for all categorical fields.

    Args:
        csv_path: Path to the main CSV file
        mapping_path: Path to field_type_mapping.csv
        chunk_size: Number of rows to process per chunk

    Returns:
        Dictionary mapping categorical column names to their unique values
    """
    # Read field type mapping with proper CSV parsing
    mapping_df = pd.read_csv(mapping_path, skipinitialspace=True)
    mapping_df.columns = mapping_df.columns.str.strip()

    # Strip whitespace from all string columns
    for col in mapping_df.columns:
        if mapping_df[col].dtype == 'object':
            mapping_df[col] = mapping_df[col].str.strip()

    # Filter for categorical fields
    categorical_fields = mapping_df[mapping_df['field_type'] == 'categorical']['column'].str.strip().tolist()

    print(f"Found {len(categorical_fields)} categorical fields:")
    for field in categorical_fields:
        print(f"  - {field}")

    # Initialize storage for unique values
    categorical_values = defaultdict(set)

    # Build dtype specification to force categorical fields as strings
    dtype_spec = {field: str for field in categorical_fields}

    # Read main CSV in chunks and extract unique values
    print(f"\nExtracting unique values from {csv_path}...")
    for chunk in pd.read_csv(csv_path, chunksize=chunk_size, dtype=dtype_spec):
        for field in categorical_fields:
            if field in chunk.columns:
                non_null_values = chunk[field].dropna()
                categorical_values[field].update(non_null_values.unique())

    # Convert sets to sorted lists
    categorical_values = {
        field: sorted(values)
        for field, values in categorical_values.items()
    }

    return categorical_values

def render_markdown(categorical_values: dict, output_path: Path):
    """
    Render categorical values to markdown format.

    Args:
        categorical_values: Dictionary mapping field names to their unique values
        output_path: Path to output markdown file
    """
    lines = ["# Categorical Field Values\n"]
    lines.append("This document lists all unique values for each categorical field in the dataset.\n")

    for field, values in categorical_values.items():
        lines.append(f"\n## {field}\n")
        lines.append(f"**Unique values:** {len(values)}\n")

        for value in values:
            # Escape markdown special characters
            escaped_value = value.replace('|', '\\|').replace('*', '\\*')
            lines.append(f"- `{escaped_value}`\n")

    # Write to file
    with open(output_path, 'w') as f:
        f.writelines(lines)

    print(f"\nMarkdown file written to: {output_path}")

if __name__ == "__main__":
    # Configuration
    csv_path = "ai_docs/context/docs/query_preprocessing/latest_dynamo_combined.csv"
    mapping_path = "src/data_catalogue/results/field_type_mapping.csv"
    output_dir = Path("src/data_catalogue/results")
    output_path = output_dir / "categorical_values.md"

    # Extract categorical values
    categorical_values = extract_categorical_values(csv_path, mapping_path)

    # Render to markdown
    render_markdown(categorical_values, output_path)

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    for field, values in categorical_values.items():
        print(f"{field:40} {len(values):6} unique values")
