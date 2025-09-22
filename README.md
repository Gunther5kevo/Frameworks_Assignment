# Frameworks Assignment - COVID-19 Research Papers Analysis

## Project Overview

This project analyzes the CORD-19 dataset, a comprehensive collection of COVID-19 and coronavirus-related research papers. The analysis includes data exploration, cleaning, visualization, and an interactive Streamlit dashboard to explore publication trends and patterns.

## Dataset Information

- **Source**: CORD-19 (COVID-19 Open Research Dataset)
- **Original Size**: 1,056,660 rows × 19 columns
- **Final Cleaned Size**: 1,054,343 rows × 21 columns
- **Key Features**: Research paper metadata including titles, abstracts, publication dates, journals, and author information

## Project Structure

```
frameworks_assignment/
├── data/
│   ├── metadata.csv                    # Original dataset
│   ├── metadata_cleaned.csv            # Cleaned dataset
│   ├── publications_per_year.png       # Generated visualizations
│   ├── top_journals.png
│   ├── abstract_word_count.png
│   └── source_breakdown.png
├── part1.py                            # Data loading and exploration
├── part2.py                            # Data cleaning
├── part3.py                            # Data analysis and visualization
├── app.py                              # Streamlit dashboard
├── requirements.txt                    # Python dependencies
└── README.md                           # This file
```

## Implementation Details

### Part 1: Data Loading & Exploration
- Successfully loaded the complete CORD-19 dataset
- Performed comprehensive exploratory data analysis
- Identified key patterns and missing value distributions
- Generated summary statistics for both numerical and categorical columns

**Key Findings:**
- Large amounts of missing data in certain columns (mag_id: 100%, arxiv_id: 98.7%)
- Multiple data sources (PMC, WHO, etc.) with WHO being the most prominent (450,459 entries)
- Publication timespan covering multiple decades

### Part 2: Data Cleaning
- Handled missing values strategically based on data importance
- Added derived columns for enhanced analysis:
  - `year`: Extracted from publish_time
  - `abstract_word_count`: Word count of abstracts
- Reduced dataset size minimally (99.8% retention rate)
- Saved cleaned data for downstream analysis

**Cleaning Results:**
- Original: 1,056,660 rows → Final: 1,054,343 rows
- Added meaningful derived features
- Maintained data integrity while improving usability

### Part 3: Data Analysis & Visualization
Generated four key visualizations:

1. **Publications Per Year**: Time series showing research output trends
2. **Top Journals**: Bar chart of most prolific journals in the dataset
3. **Abstract Word Count Distribution**: Histogram showing abstract length patterns
4. **Source Breakdown**: Pie chart of data source distribution

### Part 4: Interactive Streamlit Dashboard
Built a user-friendly web application featuring:
- Interactive year range slider for temporal filtering
- Journal selection dropdown for focused analysis
- Dynamic data preview with real-time filtering
- Embedded visualizations from Part 3
- Clean, responsive interface design

## Installation & Usage

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/Gunther5kevo/Frameworks_Assignment.git
   cd frameworks_assignment
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure data availability**:
   - Place the original `metadata.csv` in the `data/` directory
   - Or run the cleaning scripts to generate the required files

4. **Run individual components**:
   ```bash
   # Data exploration
   python part1.py
   
   # Data cleaning
   python part2.py
   
   # Generate visualizations
   python part3.py
   ```

5. **Launch the Streamlit dashboard**:
   ```bash
   streamlit run app.py
   ```

The dashboard will be available at `http://localhost:8501`
also deployed at https://gunther5kevo-frameworks-assignment-app-stjn2l.streamlit.app/

## Key Dependencies

```
streamlit>=1.28.0
pandas>=1.5.0
matplotlib>=3.6.0
seaborn>=0.11.0
plotly>=5.17.0
numpy>=1.21.0
```

## Technical Challenges & Solutions

### Memory Management
- **Challenge**: Large dataset (1M+ rows) causing memory issues
- **Solution**: Implemented efficient data types and strategic column selection during loading

### Missing Data Handling
- **Challenge**: Significant missing values across multiple columns
- **Solution**: Developed column-specific strategies, prioritizing data preservation while maintaining analytical value

### Performance Optimization
- **Challenge**: Slow processing times for large dataset operations
- **Solution**: Utilized pandas vectorized operations and efficient data structures

## Results & Insights

### Publication Trends
- Identified peak publication periods during COVID-19 pandemic
- Observed correlation between global events and research output

### Journal Analysis
- Determined most active journals in coronavirus research
- Revealed specialization patterns across different publication venues

### Content Analysis
- Abstract length distribution provides insights into publication standards
- Word count variations across different time periods and journals

## Future Enhancements

1. **Advanced Analytics**:
   - Topic modeling using NLP techniques
   - Citation network analysis
   - Geographic distribution of research

2. **Enhanced Interactivity**:
   - Real-time data updates
   - Advanced filtering options
   - Export functionality for filtered datasets

3. **Scalability Improvements**:
   - Database integration for larger datasets
   - Caching mechanisms for improved performance
   - Cloud deployment options

## Reflection

This project provided valuable hands-on experience with:
- Large-scale data processing and cleaning techniques
- Effective visualization strategies for complex datasets
- Building interactive web applications with Streamlit
- Managing technical challenges in real-world data analysis scenarios

The CORD-19 dataset's complexity and size presented excellent learning opportunities for developing robust data analysis workflows and creating user-friendly interfaces for data exploration.


*This project was completed as part of a frameworks/data analysis course assignment.*