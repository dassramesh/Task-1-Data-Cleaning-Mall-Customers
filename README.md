#Task 1 — Data Cleaning & Preprocessing (Mall Customer Segmentation Dataset)

This repository contains the solution for Task 1 of the Data Analyst Internship.
The goal is to clean and preprocess a real-world dataset to make it analysis-ready.

 Objective

Identify and handle missing values

Remove duplicate records

Standardize inconsistent text formats

Clean column names

Correct data types

Generate a clean version of the dataset

🛠 Tools Used

Python 3

Pandas

VS Code

 Dataset

Dataset Used: Mall Customer Segmentation Data
Source: Kaggle

Files in this repository:

Mall_Customers.csv               # Raw dataset
Mall_Customers_Cleaned.csv       # Final cleaned dataset
clean_data.py                    # Python script used for cleaning
README.md                        # Documentation

 Data Cleaning Steps
✔ 1. Loaded Dataset

Using pandas.read_csv().

✔ 2. Cleaned Column Names

Converted all column names to lowercase

Replaced spaces with underscores

✔ 3. Checked Missing Values

Used df.isnull().sum() to identify missing values.

✔ 4. Handled Missing Values

Filled numeric missing values with median

Filled categorical missing values (Gender) with mode

✔ 5. Removed Duplicates

Used df.drop_duplicates() to remove repeated rows.

✔ 6. Standardized Text Values

Cleaned unwanted spaces

Fixed inconsistent capitalization (e.g., male, Male, MALE → Male)

✔ 7. Converted Data Types

Age → integer

Annual income → float

Spending score → integer

✔ 8. Exported Clean Dataset

Saved the cleaned dataset as:
Mall_Customers_Cleaned.csv

 Python Script (clean_data.py)
import pandas as pd

df = pd.read_csv("Mall_Customers.csv")

df.columns = df.columns.str.lower().str.replace(" ", "_")

df = df.fillna({
    "age": df["age"].median(),
    "annual_income_(k$)": df["annual_income_(k$)"].median(),
    "spending_score_(1-100)": df["spending_score_(1-100)"].median()
})

df = df.drop_duplicates()

df["gender"] = df["gender"].str.strip().str.capitalize()

df["age"] = df["age"].astype(int)
df["annual_income_(k$)"] = df["annual_income_(k$)"].astype(float)
df["spending_score_(1-100)"] = df["spending_score_(1-100)"].astype(int)

df.to_csv("Mall_Customers_Cleaned.csv", index=False)

print("Cleaning completed. Saved as Mall_Customers_Cleaned.csv")

 Output

The cleaned dataset contains:

No missing values

No duplicates

Properly formatted text

Consistent column names

Correct data types

Final file: Mall_Customers_Cleaned.csv
