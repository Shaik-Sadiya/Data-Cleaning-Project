from datetime import datetime


def generate_report(
    original_df,
    cleaned_df,
    report_path
):
    """
    Generate a data cleaning report.

    Parameters:
        original_df (DataFrame): Original dataset
        cleaned_df (DataFrame): Cleaned dataset
        report_path (str): Path to save report

    Returns:
        None
    """

    original_rows = original_df.shape[0]
    original_columns = original_df.shape[1]

    cleaned_rows = cleaned_df.shape[0]
    cleaned_columns = cleaned_df.shape[1]

    missing_before = original_df.isnull().sum().sum()
    missing_after = cleaned_df.isnull().sum().sum()

    duplicates_before = original_df.duplicated().sum()
    duplicates_after = cleaned_df.duplicated().sum()

    rows_removed = original_rows - cleaned_rows

    memory_usage = round(
        cleaned_df.memory_usage(deep=True).sum() / 1024,
        2
    )

    with open(report_path, "w") as report:

        report.write("=" * 60 + "\n")
        report.write("DATA CLEANING REPORT\n")
        report.write("=" * 60 + "\n\n")

        report.write(
            f"Report Generated : "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        report.write(
            f"Original Dataset Shape : "
            f"{original_rows} Rows x {original_columns} Columns\n"
        )

        report.write(
            f"Cleaned Dataset Shape : "
            f"{cleaned_rows} Rows x {cleaned_columns} Columns\n\n"
        )

        report.write(
            f"Rows Removed : {rows_removed}\n"
        )

        report.write(
            f"Missing Values Before : {missing_before}\n"
        )

        report.write(
            f"Missing Values After : {missing_after}\n"
        )

        report.write(
            f"Duplicate Rows Before : {duplicates_before}\n"
        )

        report.write(
            f"Duplicate Rows After : {duplicates_after}\n\n"
        )

        report.write(
            f"Memory Usage : {memory_usage} KB\n\n"
        )

        report.write("Column Data Types\n")
        report.write("-" * 60 + "\n")

        for column, dtype in cleaned_df.dtypes.items():
            report.write(f"{column:<30}{dtype}\n")

        report.write("\n")
        report.write("=" * 60 + "\n")
        report.write("Data Cleaning Completed Successfully\n")
        report.write("=" * 60 + "\n")

    print(f"Cleaning report saved to: {report_path}")