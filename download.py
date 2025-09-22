import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

DATA_DIR = "data"
CSV_FILE = os.path.join(DATA_DIR, "metadata.csv")
ZIP_FILE = os.path.join(DATA_DIR, "metadata.csv.zip")

os.makedirs(DATA_DIR, exist_ok=True)

# Always re-download to be safe (force refresh)
if os.path.exists(CSV_FILE):
    os.remove(CSV_FILE)
if os.path.exists(ZIP_FILE):
    os.remove(ZIP_FILE)

print("⬇️ Downloading metadata.csv from Kaggle ...")
api = KaggleApi()
api.authenticate()

api.dataset_download_file(
    "allen-institute-for-ai/CORD-19-research-challenge",
    file_name="metadata.csv",
    path=DATA_DIR
)

# Extract properly
if os.path.exists(ZIP_FILE):
    print("📦 Extracting metadata.csv ...")
    with zipfile.ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(DATA_DIR)
    os.remove(ZIP_FILE)

print(f"✅ Done. Saved CSV at: {CSV_FILE}")

# Quick sanity check
with open(CSV_FILE, "r", encoding="utf-8", errors="ignore") as f:
    print("🔍 First line of CSV:", f.readline().strip())
