# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned metadata
df = pd.read_csv("data/metadata_sample.csv", low_memory=False)


# Rename for consistency
if "year" in df.columns:
    df = df.rename(columns={"year": "publish_year"})

# Streamlit App
st.title("CORD-19 Data Explorer")
st.write("Explore metadata from COVID-19 research papers")

# Sidebar filters
st.sidebar.header("Filters")
min_year = int(df["publish_year"].min())
max_year = int(df["publish_year"].max())
year_range = st.sidebar.slider("Select year range", min_year, max_year, (2019, 2021))

# Apply filter
filtered_df = df[
    (df["publish_year"] >= year_range[0]) &
    (df["publish_year"] <= year_range[1])
]

# Show sample of data
st.subheader("Sample of Data")
st.dataframe(filtered_df.head(20))

# --- Visualization 1: Publications Over Time ---
st.subheader("Publications Over Time")
year_counts = filtered_df["publish_year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
ax.set_title("Publications by Year")
st.pyplot(fig)

# --- Visualization 2: Top Journals ---
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
fig, ax = plt.subplots()
top_journals.plot(kind="bar", ax=ax)
ax.set_xlabel("Journal")
ax.set_ylabel("Number of Publications")
ax.set_title("Top Journals")
st.pyplot(fig)

# --- Visualization 3: Abstract Word Count Distribution ---
st.subheader("Abstract Word Count Distribution")
fig, ax = plt.subplots()
filtered_df["abstract_word_count"].dropna().hist(bins=30, ax=ax)
ax.set_xlabel("Word Count")
ax.set_ylabel("Frequency")
ax.set_title("Distribution of Abstract Length")
st.pyplot(fig)

# --- Visualization 4: Source Breakdown ---
st.subheader("Source Breakdown")
fig, ax = plt.subplots()
filtered_df["source_x"].value_counts().head(10).plot(kind="bar", ax=ax)
ax.set_xlabel("Source")
ax.set_ylabel("Number of Papers")
ax.set_title("Top Sources")
st.pyplot(fig)
