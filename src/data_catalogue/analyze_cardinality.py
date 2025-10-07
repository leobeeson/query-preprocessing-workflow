import pandas as pd
from collections import defaultdict
from pathlib import Path

def analyze_cardinality(csv_path: str, chunk_size: int = 10000, sparse_threshold: float = 90.0,
                       low_cardinality_threshold: float = 10.0, unique_threshold: float = 95.0):
    """
    Perform statistical profiling of CSV columns.

    Args:
        csv_path: Path to CSV file
        chunk_size: Number of rows to process per chunk
        sparse_threshold: Percentage threshold for sparse fields (high null rate)
        low_cardinality_threshold: Percentage threshold for low cardinality classification
        unique_threshold: Percentage threshold for unique/identifier classification

    Returns:
        DataFrame with statistical profiling results
    """
    # Initialize counters
    column_stats = defaultdict(lambda: {
        "unique_values": set(),
        "non_null_count": 0,
        "null_count": 0,
        "dtype": None,
        "sample_values": []
    })

    # Read and process in chunks
    for chunk in pd.read_csv(csv_path, chunksize=chunk_size):
        for col in chunk.columns:
            non_null_values = chunk[col].dropna()

            # Store dtype (from first chunk)
            if column_stats[col]["dtype"] is None:
                column_stats[col]["dtype"] = str(chunk[col].dtype)

            # Update unique values (as strings for cardinality counting)
            column_stats[col]["unique_values"].update(non_null_values.astype(str).unique())

            # Store sample values (first 5 unique)
            if len(column_stats[col]["sample_values"]) < 5:
                new_samples = non_null_values.astype(str).unique()[:5 - len(column_stats[col]["sample_values"])]
                column_stats[col]["sample_values"].extend(new_samples)

            # Update counts
            column_stats[col]["non_null_count"] += len(non_null_values)
            column_stats[col]["null_count"] += chunk[col].isna().sum()

    # Calculate statistics
    results = []
    for col, stats in column_stats.items():
        unique_count = len(stats["unique_values"])
        non_null_count = stats["non_null_count"]
        null_count = stats["null_count"]
        total_count = non_null_count + null_count

        # Calculate percentages based on non-null values only
        cardinality_pct = (unique_count / non_null_count * 100) if non_null_count > 0 else 0
        null_pct = (null_count / total_count * 100) if total_count > 0 else 0

        # Determine cardinality profile (statistical only)
        if null_pct >= sparse_threshold:
            cardinality_profile = "sparse"
        elif cardinality_pct >= unique_threshold:
            cardinality_profile = "unique"
        elif cardinality_pct >= low_cardinality_threshold:
            cardinality_profile = "high_cardinality"
        else:
            cardinality_profile = "low_cardinality"

        # Format sample values
        sample_str = ", ".join([f'"{v}"' for v in stats["sample_values"][:5]])

        results.append({
            "column": col,
            "dtype": stats["dtype"],
            "unique_count": unique_count,
            "non_null_count": non_null_count,
            "null_count": null_count,
            "total_count": total_count,
            "cardinality_pct": round(cardinality_pct, 2),
            "null_pct": round(null_pct, 2),
            "cardinality_profile": cardinality_profile,
            "sample_values": sample_str
        })

    results_df = pd.DataFrame(results).sort_values("cardinality_pct")
    return results_df


if __name__ == "__main__":
    # Configuration
    csv_path = "ai_docs/context/docs/query_preprocessing/latest_dynamo_combined.csv"
    output_dir = Path("src/data_catalogue/results")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Run analysis
    print(f"Analyzing statistical profile for: {csv_path}")
    results_df = analyze_cardinality(csv_path)

    # Save results
    output_path = output_dir / "cardinality_analysis.csv"
    results_df.to_csv(output_path, index=False)
    print(f"\nResults saved to: {output_path}")

    # Display summary
    print("\n" + "="*120)
    print("STATISTICAL PROFILING SUMMARY")
    print("="*120)
    display_cols = ["column", "dtype", "unique_count", "non_null_count", "cardinality_pct", "null_pct", "cardinality_profile"]
    print(results_df[display_cols].to_string(index=False))

    # Group by cardinality profile
    print("\n" + "="*120)
    print("LOW CARDINALITY FIELDS (cardinality < 10%)")
    print("="*120)
    low_card = results_df[results_df["cardinality_profile"] == "low_cardinality"]
    print(low_card[["column", "dtype", "unique_count", "cardinality_pct", "null_pct", "sample_values"]].to_string(index=False))

    print("\n" + "="*120)
    print("HIGH CARDINALITY FIELDS (10% <= cardinality < 95%)")
    print("="*120)
    high_card = results_df[results_df["cardinality_profile"] == "high_cardinality"]
    print(high_card[["column", "dtype", "unique_count", "cardinality_pct", "null_pct", "sample_values"]].to_string(index=False))

    print("\n" + "="*120)
    print("UNIQUE FIELDS (cardinality >= 95%)")
    print("="*120)
    unique = results_df[results_df["cardinality_profile"] == "unique"]
    print(unique[["column", "dtype", "unique_count", "cardinality_pct", "null_pct", "sample_values"]].to_string(index=False))

    print("\n" + "="*120)
    print("SPARSE FIELDS (null >= 90%)")
    print("="*120)
    sparse = results_df[results_df["cardinality_profile"] == "sparse"]
    print(sparse[["column", "dtype", "unique_count", "cardinality_pct", "null_pct", "sample_values"]].to_string(index=False))
