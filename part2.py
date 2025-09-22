import pandas as pd

# Load dataset
df = pd.read_csv("data/metadata.csv", low_memory=False)
sample = df.sample(10000, random_state=42)
sample.to_csv("data/metadata_sample.csv", index=False)
# === Step 1: Handle Missing Data ===
print("\n❌ Missing values before cleaning:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# Drop rows without publish_time or title (essential for analysis)
df = df.dropna(subset=["publish_time", "title"])

# Fill missing abstracts with empty string
df["abstract"] = df["abstract"].fillna("")

# Fill missing journal names with "Unknown"
df["journal"] = df["journal"].fillna("Unknown")

print("\n✅ After cleaning:")
print(df.isnull().sum().sort_values(ascending=False).head(10))

# === Step 2: Convert Dates ===
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# === Step 3: Add New Feature (Abstract word count) ===
df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))

# === Save Cleaned Data ===
df.to_csv("data/metadata_cleaned.csv", index=False)

print("\n✅ Cleaned dataset saved as data/metadata_cleaned.csv")
print(f"Final shape: {df.shape}")
print(df[["title", "journal", "year", "abstract_word_count"]].head())
