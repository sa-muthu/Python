import pandas as pd

df = pd.read_csv("03.01 - Pokemon.csv")
print(df)

# Aggregate Functions = Reduce a set of values into a single summary value
#                       Used to summarize and analyze data
#                       Often used with the groupby() function


# for whole dataframe
print(df.mean(numeric_only = True))
print()

print(df.sum(numeric_only = True))
print()

print(df.max(numeric_only = True))
print()

print(df.min(numeric_only = True))
print()

print(df.count(numeric_only = True))
print()


# for single coloumn
print(df["Height"].mean())
print()

print(df["Height"].sum())
print()

print(df["Height"].max())
print()

print(df["Height"].min())
print()

print(df["Height"].count())
print()



# Groupby

group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].max())
print(group["Height"].count())