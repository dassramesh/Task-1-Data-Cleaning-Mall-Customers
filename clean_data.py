import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# 1. Rename columns
df.columns = df.columns.str.lower().str.replace(" ", "_")

# 2. Check missing values
missing = df.isnull().sum()
print("Missing values before cleaning:\n", missing)

# 3. Handle missing values (if any)
df = df.fillna({
    "age": df["age"].median(),
    "annual_income_(k$)": df["annual_income_(k$)"].median(),
    "spending_score_(1-100)": df["spending_score_(1-100)"].median()
})

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Standardize gender values
df["gender"] = df["gender"].str.strip().str.capitalize()

# 6. Fix data types
df["age"] = df["age"].astype(int)
df["annual_income_(k$)"] = df["annual_income_(k$)"].astype(float)
df["spending_score_(1-100)"] = df["spending_score_(1-100)"].astype(int)

# 7. Save cleaned dataset
df.to_csv("Mall_Customers_Cleaned.csv", index=False)

print("Cleaning completed. Saved as Mall_Customers_Cleaned.csv")
