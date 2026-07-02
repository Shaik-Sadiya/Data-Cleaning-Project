import logging
import os


def setup_logger(log_file):
    """
    Configure logging.

    Parameters:
        log_file (str): Path to log file

    Returns:
        None
    """

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w"
    )


def log_message(message):
    """
    Write an information message to the log file.
    """

    logging.info(message)


def print_separator():
    """
    Print a separator line.
    """

    print("=" * 60)


def dataset_summary(df):
    """
    Display basic information about the dataset.

    Parameters:
        df (pandas.DataFrame)

    Returns:
        None
    """

    print_separator()
    print("DATASET SUMMARY")
    print_separator()

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print_separator()