import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/metadata_cleaned.csv")

# === 1. Publications per Year ===
pubs_per_year = df["year"].value_counts().sort_index()
plt.figure(figsize=(10,5))
pubs_per_year.plot(kind="bar", color="skyblue")
plt.title("Publications per Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.tight_layout()
plt.savefig("data/publications_per_year.png")
plt.close()

# === 2. Top Journals ===
top_journals = df["journal"].value_counts().head(10)
plt.figure(figsize=(10,5))
top_journals.plot(kind="barh", color="lightgreen")
plt.title("Top 10 Journals by Publication Count")
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.tight_layout()
plt.savefig("data/top_journals.png")
plt.close()

# === 3. Abstract Word Count Distribution ===
plt.figure(figsize=(10,5))
df["abstract_word_count"].hist(bins=50, color="salmon")
plt.title("Distribution of Abstract Word Counts")
plt.xlabel("Word Count")
plt.ylabel("Number of Papers")
plt.tight_layout()
plt.savefig("data/abstract_word_count.png")
plt.close()

# === 4. Source Breakdown ===
source_counts = df["source_x"].value_counts()
plt.figure(figsize=(8,5))
source_counts.plot(kind="pie", autopct="%1.1f%%", startangle=140)
plt.title("Publication Sources")
plt.ylabel("")
plt.tight_layout()
plt.savefig("data/source_breakdown.png")
plt.close()

print("✅ Analysis complete! Charts saved in 'data/' folder:")
print("- publications_per_year.png")
print("- top_journals.png")
print("- abstract_word_count.png")
print("- source_breakdown.png")
