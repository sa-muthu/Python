import pandas as pd

data = pd.read_csv("pokemon.csv")
print(data)

# Filtering = Keeping the rows that match a condition

# 1. Filtering by value
print(data[data["Height"] >= 5])
print(data[data["Weight"] >= 300])


# 2. Filtering by multiple conditions
print(data[(data["Height"] >= 5) & (data["Weight"] >= 300)])
print(data[(data["Height"] >= 5) | (data["Weight"] >= 300)])
print(data[(data["Height"] >= 5) & (data["Weight"] >= 300) | (data["Legendary"] == 1)])
print(data[(data["Height"] >= 5) & (data["Weight"] >= 300) | (data["Legendary"] == 1)])

# 3. Filtering by list
print(data[data["Type1"].isin(["Fire", "Water", "Grass"])])
print(data[data["Type1"].isin(["Fire", "Water", "Grass"]) & (data["Legendary"] == 1)])
print(data[data["Type1"].isin(["Fire", "Water", "Grass"]) & (data["Legendary"] == 1) | (data["Type2"] == "Fire")])
print(data[data["Type1"].isin(["Fire", "Water", "Grass"]) & (data["Legendary"] == 1) | (data["Type2"] == "Fire")])

# 4. Filtering by string
print(data[data["Name"].str.contains("Mega")])
print(data[data["Name"].str.contains("Mega") & (data["Legendary"] == 1)])

# 5. Filtering by null values
print(data[data["Type2"].isnull()])

# 6. Filtering by not null values
print(data[data["Type2"].notnull()])

# 7. Filtering by index
print(data.iloc[0:10])

# 8. Filtering by index and value
print(data.iloc[0:10, 0:3])
