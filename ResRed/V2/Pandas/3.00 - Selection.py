import pandas as pd

data = pd.read_csv("Pokemon.csv")
print(data)

# 1. Selection by Column
print(data["Name"]) # to select a single column
print(data["Name"].to_string()) # to print the whole column
print(data[["Name", "Height", "Weight"]]) # to select multiple columns

# 2. Selection by Row
print(data.loc[0]) # to select a single row
print(data.loc[0:10]) # to select multiple rows
print(data.loc[0:10:2]) # to select multiple rows with step
print(data.loc[0:10, ["Name", "Height", "Weight"]]) # to select multiple rows and columns

# 3. Selection by Column and Row
print(data.loc[0, "Name"]) # to select a single column and row
