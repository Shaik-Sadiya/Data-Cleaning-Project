import pandas as pd


def validate_data(df):
    """
    Validate the cleaned dataset.

    Checks:
    1. Missing values
    2. Duplicate rows
    3. Data types
    4. Dataset shape

    Parameters:
        df (pandas.DataFrame)

    Returns:
        bool
    """

    print("\n" + "=" * 60)
    print("DATA VALIDATION")
    print("=" * 60)

    # Dataset Shape
    print(f"Dataset Shape : {df.shape}")

    # Missing Values
    missing_values = df.isnull().sum().sum()

    if missing_values == 0:
        print("No Missing Values Found")
    else:
        print(f"Missing Values Found : {missing_values}")

    # Duplicate Rows
    duplicate_rows = df.duplicated().sum()

    if duplicate_rows == 0:
        print("No Duplicate Rows Found")
    else:
        print(f"Duplicate Rows Found : {duplicate_rows}")

    # Data Types
    print("\nColumn Data Types")
    print("-" * 60)
    print(df.dtypes)

    # Check Empty Dataset
    if df.empty:
        print("\n Dataset is Empty")
        return False

    # Validation Result
    if missing_values == 0 and duplicate_rows == 0:
        print("\n Data Validation Successful")
        print("=" * 60)
        return True
    else:
        print("\n Data Validation Failed")
        print("=" * 60)
        return False