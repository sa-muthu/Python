# Pandas Aggregation
# This script covers common aggregation functions used in Pandas.

import pandas as pd

# Load the dataset
df = pd.read_csv("Pokemon.csv")

# 1. Summary Statistics for the Entire DataFrame
# Use numeric_only=True to avoid errors with non-numeric columns
print("--- Mean of Numerical Columns ---")
print(df.mean(numeric_only=True))
print("\n--- Summary Description ---")
print(df.describe())  # Provides count, mean, std, min, 25%, 50%, 75%, max

# 2. Aggregation on Specific Columns
print("\n--- Height Statistics ---")
print(f"Mean Height:   {df['Height'].mean():.2f}")
print(f"Median Height: {df['Height'].median():.2f}")
print(f"Max Height:    {df['Height'].max():.2f}")
print(f"Min Height:    {df['Height'].min():.2f}")

# Categorical Aggregation
print("\n--- Type1 Value Counts ---")
print(df["Type1"].value_counts())
print("\n--- Unique Types ---")
print(df["Type1"].unique())

# 3. Aggregation on Multiple Columns
print("\n--- Mean of Height and Weight ---")
print(df[["Height", "Weight"]].mean())

# 4. Aggregation on Filtered Rows
# Example: Mean stats for legendary Pokemon only
legendary_df = df[df["Legendary"] == 1]
print("\n--- Mean Stats for Legendary Pokemon ---")
print(legendary_df[["Height", "Weight"]].mean())

# 5. Grouped Aggregation (GroupBy)
# Grouping data by 'Type1' and calculating the mean for each group
print("\n--- Mean Height by Type1 ---")
type_group = df.groupby("Type1")
print(type_group["Height"].mean().sort_values(ascending=False))
