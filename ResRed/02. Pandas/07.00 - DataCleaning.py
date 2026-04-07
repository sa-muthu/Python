import pandas as pd

df = pd.read_csv("03.01 - Pokemon.csv")
print(df)
print()

# Data Cleaning = the process of fixing/removing:
#                 incomplete, incorrect, or irrelevant data
#                 ~75% of work done with Pandas is data cleaning

# 1. Drop irrelevant coloumns
df = df.drop(columns = ["Legendary", "No"])
print(df)
print()


# 2. Handle missing data
# df = df.dropna(subset = ["Type2"])
# print(df)
# print()

# 3. Fill NaA with "none"
df = df.fillna({"Type2": "None"})
print(df)
print()

# 4. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})
print(df)
print()

df["Type1"] = df["Type1"].replace({"GRASS": "Grass",
                                   "Fire": "FIRE"})
print(df)
print()


# 5. Standardize text
df["Name"] = df["Name"].str.lower()
print(df)
print()

# 6. Change Data Types
df["Legendary"] = df["Legendary"].astype(bool)
print(df)
print()


# 7. Remove Duplicates
df = df.drop_duplicates()
print(df)
print()