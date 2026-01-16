# Command-Line GDP Data Cleaning & Summarization Tool

## Overview
This project is a **Python-based command-line application** designed to clean, process, and summarize **GDP per capita time-series data** (World Bank format). It allows a user to select a country and receive meaningful summary statistics directly from the terminal.

The project demonstrates core data-engineering and analytics skills including data cleaning, transformation, aggregation, and user interaction via a CLI interface.

This repository is intended for **code review and technical feedback**.

---

## Project Objectives
- Clean raw, real-world CSV data containing missing and inconsistent values
- Convert wide-format time-series data into an analyzable structure
- Compute meaningful summary statistics for a single country
- Provide a simple, interactive **command-line user experience**
- Demonstrate practical use of **pandas** outside of notebooks

---

## Repository Structure
```
command line interface CSV cleaning and summarization program/
│
├── CLI_App_2.py                     # Main command-line application
├── CLI App.ipynb                    # Development & exploratory notebook
├── cleaned_gdp_data.csv             # Cleaned and processed dataset
│
├── API_NY.GDP.PCAP.CD_DS2_*.csv      # Raw World Bank GDP per capita data
├── Metadata_Country_*.csv            # Country metadata
├── Metadata_Indicator_*.csv          # Indicator metadata
```

---

## Data Source
- **World Bank – GDP per capita (current US$)**
- Raw data contains:
  - Metadata rows
  - Missing values
  - Year columns spanning multiple decades

The cleaning process removes non-data rows, standardizes country names, and ensures numeric consistency across year columns.

---

## Key Features
- Command-line user input for country selection
- Automatic handling of missing values
- Summary statistics calculated across available years, including:
  - Mean GDP per capita
  - Median GDP per capita
  - Minimum and maximum values
  - GDP growth trend metrics (e.g., CAGR)
- Separation of **data cleaning** and **analysis logic**

---

## How to Run
1. Clone the repository
2. Ensure Python 3.10+ is installed
3. Install dependencies:
   ```bash
   pip install pandas
   ```
4. Run the CLI application:
   ```bash
   python CLI_App_2.py
   ```
5. Enter a country name when prompted

---

## Why a CLI Instead of Notebook Only
While development began in Jupyter, the final implementation was intentionally moved to a **standalone Python script** to demonstrate:
- Script-based execution
- Separation of logic from exploration
- Real-world usability outside notebooks

---

## Skills Demonstrated
- Python scripting
- pandas data manipulation
- Handling real-world, messy datasets
- Command-line application design
- Basic data analytics & summarization

---


## Notes for Review
- Focus was placed on **clarity and correctness** rather than over-engineering
- The project is intentionally simple but extensible
- Feedback on structure, efficiency, and best practices is welcome

---

**Author:** Phillip Dimitrov

