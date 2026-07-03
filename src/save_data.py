import os


def save_cleaned_data(df, output_path):
    """
    Save the cleaned dataset as a CSV file.

    Parameters:
        df (pandas.DataFrame): Cleaned DataFrame
        output_path (str): Path to save the CSV

    Returns:
        None
    """

    print("\n" + "=" * 60)
    print("SAVING CLEANED DATA")
    print("=" * 60)

    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save CSV
    df.to_csv(output_path, index=False)

    print(f"Cleaned dataset saved successfully.")
    print(f"Location: {output_path}")
    print(f"Final Dataset Shape: {df.shape}")

    print("=" * 60)