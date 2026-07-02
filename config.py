import os

# -----------------------------
# Project Directories
# -----------------------------

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data folders
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
CLEANED_DATA_DIR = os.path.join(BASE_DIR, "data", "cleaned")

# Report folder
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# Visualization folder
VISUALIZATION_DIR = os.path.join(BASE_DIR, "visualizations")

# Log folder
LOG_DIR = os.path.join(BASE_DIR, "logs")

# -----------------------------
# Dataset Paths
# -----------------------------

CSV_FILE = os.path.join(RAW_DATA_DIR, "cleaning_data.csv")



CLEANED_FILE = os.path.join(
    CLEANED_DATA_DIR,
    "cleaned_data.csv"
)

REPORT_FILE = os.path.join(
    REPORT_DIR,
    "cleaning_report.txt"
)

LOG_FILE = os.path.join(
    LOG_DIR,
    "cleaning.log"
)

# -----------------------------
# Create folders if they don't exist
# -----------------------------

os.makedirs(CLEANED_DATA_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(VISUALIZATION_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)