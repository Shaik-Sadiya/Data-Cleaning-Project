import pandas as pd


def handle_missing_values(df):
    """
    Handle missing values in the dataset.

    Numeric Columns:
        Fill missing values with median.

    Categorical Columns:
        Fill missing values with mode.

    Parameters:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """

    print("\n" + "=" * 60)
    print("HANDLING MISSING VALUES")
    print("=" * 60)

    # Count missing values before cleaning
    missing_before = df.isnull().sum().sum()
    print(f"Total Missing Values Before Cleaning: {missing_before}")

    # Numeric Columns
    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:
        if df[column].isnull().sum() > 0:
            median = df[column].median()
            df[column] = df[column].fillna(median)
            print(f"Filled missing values in '{column}' with median.")

    # Categorical Columns
    categorical_columns = df.select_dtypes(include=["object"]).columns

    for column in categorical_columns:
        if df[column].isnull().sum() > 0:
            mode = df[column].mode()[0]
            df[column] = df[column].fillna(mode)
            print(f"Filled missing values in '{column}' with mode.")

    # Count missing values after cleaning
    missing_after = df.isnull().sum().sum()

    print(f"\nTotal Missing Values After Cleaning: {missing_after}")

    print("=" * 60)

    return df