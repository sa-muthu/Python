# Pandas Data Cleaning
# This script covers the process of cleaning and standardizing your dataset.

import pandas as pd

# Load the dataset
df = pd.read_csv("Pokemon.csv")

# 1. Drop Irrelevant Columns
# We can remove columns that aren't needed for our analysis.
# Note: Keep 'Legendary' for later type casting.
df_cleaned = df.drop(columns=["No"])
print("--- After Dropping 'No' Column ---")
print(df_cleaned.head())

# 2. Handle Missing Data
# We can drop rows with missing values in specific columns.
# Example: Drop rows where 'Type2' is missing.
df_dropna = df_cleaned.dropna(subset=["Type2"])
print("\n--- After Dropping Missing 'Type2' Rows ---")
print(df_dropna.head())

# 3. Fill Missing Data
# Alternatively, we can fill missing values with a default string.
df_filled = df_cleaned.fillna({"Type2": "None"})
print("\n--- After Filling Missing 'Type2' with 'None' ---")
print(df_filled.head())

# 4. Fix Inconsistent Values
# Use .replace() to standardize naming or fix errors.
df_filled["Type1"] = df_filled["Type1"].replace({"Grass": "GRASS"})
print("\n--- After Replacing 'Grass' with 'GRASS' ---")
print(df_filled["Type1"].head())

# 5. Standardize Text
# Change text to lowercase or uppercase for consistency.
df_filled["Name"] = df_filled["Name"].str.lower()
print("\n--- After Making Names Lowercase ---")
print(df_filled["Name"].head())

# 6. Change Data Types
# Use .astype() to cast columns to the correct type (e.g., int to bool).
df_filled["Legendary"] = df_filled["Legendary"].astype(bool)
print("\n--- After Casting 'Legendary' to Boolean ---")
print(df_filled["Legendary"].head())

# 7. Remove Duplicates
# Ensures each row in your dataset is unique.
df_final = df_filled.drop_duplicates()
print("\n--- Rows after dropping duplicates ---")
print(len(df_final))
