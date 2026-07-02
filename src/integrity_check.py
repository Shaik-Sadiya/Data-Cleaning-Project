import pandas as pd


def check_data_integrity(df):
    """
    Perform basic data integrity checks on the dataset.

    Parameters:
        df (pandas.DataFrame): Input DataFrame

    Returns:
        None
    """

    print("\n" + "=" * 60)
    print("DATA INTEGRITY REPORT")
    print("=" * 60)

    # Shape
    print(f"\nDataset Shape: {df.shape}")

    # Column Names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # Data Types
    print("\nData Types:")
    print(df.dtypes)

    # Missing Values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate Rows
    duplicate_count = df.duplicated().sum()
    print(f"\nDuplicate Rows: {duplicate_count}")

    # Unique Values
    print("\nUnique Values Per Column:")
    print(df.nunique())

    # Summary Statistics
    print("\nSummary Statistics:")
    print(df.describe(include="all").transpose())

    print("\n" + "=" * 60)
    print("DATA INTEGRITY CHECK COMPLETED")
    print("=" * 60)