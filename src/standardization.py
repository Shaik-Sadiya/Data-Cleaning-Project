import pandas as pd


def standardize_data(df):
    """
    Standardize text columns by:
    1. Removing leading/trailing spaces
    2. Replacing multiple spaces with a single space
    3. Converting text to Title Case

    Parameters:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """

    print("\n" + "=" * 60)
    print("STANDARDIZING DATA")
    print("=" * 60)

    # Select all object (string) columns
    text_columns = df.select_dtypes(include=["object"]).columns

    for column in text_columns:
        df[column] = (
            df[column]
            .astype(str)
            .str.strip()                    # Remove leading/trailing spaces
            .str.replace(r"\s+", " ", regex=True)  # Remove extra spaces
            .str.title()                    # Convert to Title Case
        )

        print(f"Standardized column: {column}")

    print("=" * 60)

    return df