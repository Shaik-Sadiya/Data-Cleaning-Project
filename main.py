from config import (
    CSV_FILE,
    CLEANED_FILE,
    LOG_FILE,
    REPORT_FILE,
    VISUALIZATION_DIR
)

from src.load_data import load_csv
from src.integrity_check import check_data_integrity
from src.missing_values import handle_missing_values
from src.duplicates import remove_duplicates
from src.standardization import standardize_data
from src.outlier_detection import detect_and_remove_outliers
from src.validation import validate_data
from src.save_data import save_cleaned_data
from src.utils import setup_logger, log_message, dataset_summary
from src.report_generator import generate_report
from src.visualization import (
    plot_missing_values,
    plot_histograms,
    plot_boxplots,
    plot_correlation_heatmap
)


def main():

    # Setup logger
    setup_logger(LOG_FILE)
    log_message("Project Started")

    # Load Dataset
    df = load_csv(CSV_FILE)

    if df is None:
        print("Failed to load CSV dataset.")
        return

    # Keep a copy of the original dataset
    original_df = df.copy()

    

    log_message("Dataset Loaded Successfully")

    # Dataset Summary
    dataset_summary(df)

    # Data Integrity Check
    check_data_integrity(df)
    log_message("Integrity Check Completed")

    # Handle Missing Values
    df = handle_missing_values(df)
    log_message("Missing Values Handled")

    # Remove Duplicates
    df = remove_duplicates(df)
    log_message("Duplicate Rows Removed")

    # Standardize Data
    df = standardize_data(df)
    log_message("Data Standardized")

    # Detect and Remove Outliers
    df = detect_and_remove_outliers(df)
    log_message("Outliers Removed")

    # Validate Data
    is_valid = validate_data(df)

    if is_valid:
        log_message("Validation Successful")

        # Save Cleaned Dataset
        save_cleaned_data(df, CLEANED_FILE)
        log_message("Cleaned Dataset Saved")

        # Generate Visualizations
        plot_missing_values(df, VISUALIZATION_DIR)
        plot_histograms(df, VISUALIZATION_DIR)
        plot_boxplots(df, VISUALIZATION_DIR)
        plot_correlation_heatmap(df, VISUALIZATION_DIR)
        log_message("Visualizations Generated")

        # Generate Report
        generate_report(
            original_df,
            df,
            REPORT_FILE
        )
        log_message("Cleaning Report Generated")

        print("\nProject Completed Successfully.")

    else:

        log_message("Validation Failed")
        print("\nProject Failed. Validation Error.")


if __name__ == "__main__":
    main()