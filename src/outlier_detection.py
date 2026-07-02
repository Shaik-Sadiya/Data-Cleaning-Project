import pandas as pd


def detect_and_remove_outliers(df):
    """
    Detect and remove outliers using the IQR method.

    Parameters:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """

    print("\n" + "=" * 60)
    print("OUTLIER DETECTION")
    print("=" * 60)

    # Select numeric columns
    numeric_columns = df.select_dtypes(include=["number"]).columns

    total_outliers = 0

    for column in numeric_columns:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - (1.5 * IQR)
        upper_bound = Q3 + (1.5 * IQR)

        outliers = (
            (df[column] < lower_bound) |
            (df[column] > upper_bound)
        )

        outlier_count = outliers.sum()

        if outlier_count > 0:
            print(f"{column} : {outlier_count} outliers found")

            # Remove outliers
            df = df[~outliers]

            total_outliers += outlier_count

    print("\nTotal Outliers Removed :", total_outliers)
    print("Remaining Rows :", len(df))

    print("=" * 60)

    return df