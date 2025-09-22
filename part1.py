import pandas as pd

# === Step 1: Load Data ===
print("📂 Loading dataset...")
df = pd.read_csv("data/metadata.csv", low_memory=False)

print("\n✅ Data loaded successfully!")
print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")

# === Step 2: Preview Data ===
print("\n🔍 First 5 rows:")
print(df.head())

# === Step 3: Data Structure ===
print("\n📊 DataFrame Info:")
print(df.info())

# === Step 4: Summary Statistics ===
print("\n📈 Summary statistics (numerical columns):")
print(df.describe())

print("\n📊 Summary statistics (categorical/text columns):")
print(df.describe(include='object'))

# === Step 5: Missing Values ===
print("\n❓ Missing values per column:")
missing = df.isnull().sum().sort_values(ascending=False)
print(missing.head(15))  # top 15 columns with most missing data
