import pandas as pd

df = pd.read_csv("03.01 - Pokemon.csv")
print(df)
print()

# Selection by Coloumn
print(df["Name"])
print()
print(df["Name"].to_string())
print()
print(df[["Name", "Height", "Weight"]])
print()

# Selection by Rows
print(df.loc[1])
print()

# or 
df = pd.read_csv("03.01 - Pokemon.csv", index_col = "Name")
print(df.loc["Psyduck"])
print()

print(df.loc["Psyduck", ["Height", "Weight"]])
print()

# slice
print(df.loc["Psyduck":"Onix", ["Height", "Weight"]])
print()
# print(df.loc["Psyduck":"Bulbasaur", ["Height", "Weight"]]) - returns empty list cause goes in reverse

# using indices
print(df.iloc[0:10])
print()

print(df.iloc[0:10:2])
print()

print(df.iloc[0:10:2, 0:3])
print()






# Problem

Name = input("Enter a Pokemon Name: ")
try:
    print(df.loc[Name])
except KeyError:
    print(f"{Name} Not Found")

print(df.loc[0, "Name"]) # to select a single column and row
