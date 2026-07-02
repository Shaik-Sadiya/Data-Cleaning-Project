import pandas as pd


def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)

        print("CSV loaded successfully.")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")

        return df

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"Error loading CSV: {e}")

    return None