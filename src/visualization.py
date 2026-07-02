import os
import matplotlib.pyplot as plt
import seaborn as sns


def plot_missing_values(df, output_folder):
    """
    Plot missing values for each column.
    """

    os.makedirs(output_folder, exist_ok=True)

    missing = df.isnull().sum()

    plt.figure(figsize=(12, 6))
    missing.plot(kind="bar")

    plt.title("Missing Values")
    plt.xlabel("Columns")
    plt.ylabel("Count")

    plt.tight_layout()

    plt.savefig(
        os.path.join(output_folder, "missing_values.png")
    )

    plt.close()


def plot_histograms(df, output_folder):
    """
    Plot histograms for all numeric columns.
    """

    os.makedirs(output_folder, exist_ok=True)

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:

        plt.figure(figsize=(8, 4))

        plt.hist(df[column].dropna(), bins=30)

        plt.title(f"Histogram - {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                f"histogram_{column}.png"
            )
        )

        plt.close()


def plot_boxplots(df, output_folder):
    """
    Plot boxplots for all numeric columns.
    """

    os.makedirs(output_folder, exist_ok=True)

    numeric_columns = df.select_dtypes(include=["number"]).columns

    for column in numeric_columns:

        plt.figure(figsize=(8, 4))

        sns.boxplot(x=df[column].dropna())

        plt.title(f"Boxplot - {column}")

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                output_folder,
                f"boxplot_{column}.png"
            )
        )

        plt.close()


def plot_correlation_heatmap(df, output_folder):
    """
    Plot correlation heatmap.
    """

    os.makedirs(output_folder, exist_ok=True)

    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        return

    plt.figure(figsize=(12, 8))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_folder,
            "correlation_heatmap.png"
        )
    )

    plt.close()