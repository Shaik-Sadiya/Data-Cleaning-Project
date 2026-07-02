import pandas as pd


def remove_duplicates(df):
    """
    Detect and remove duplicate rows from the dataset.

    Parameters:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """

    print("\n" + "=" * 60)
    print("DUPLICATE REMOVAL")
    print("=" * 60)

    # Number of duplicate rows
    duplicate_count = df.duplicated().sum()

    print(f"Duplicate Rows Found : {duplicate_count}")

    # Remove duplicates
    df = df.drop_duplicates()

    print(f"Duplicate Rows Removed : {duplicate_count}")
    print(f"Remaining Rows : {len(df)}")

    print("=" * 60)

    return df