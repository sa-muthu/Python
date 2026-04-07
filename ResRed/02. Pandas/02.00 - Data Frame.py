import pandas as pd

data = {
    "Name": ["Jack", "Sack", "Pack"],
    "Age": [12, 13, 35],
}

df = pd.DataFrame(data)
print(df)
print()

df = pd.DataFrame(data, index = ["Person 1", "Person 2", "Person 3"])
pd.DataFrame(df)

print(df.loc["Person 1"])
print(df.iloc[1])
print()

# add a new frame
df["Job"] = ["gamer", "doomer", "boomer"]
print(df)
print( )

# add a new row 
new_row = pd.DataFrame([{"Name": "Jinku", "Age": 13, "Job": "useless"}],
                       index = ["Person 4"])
df = pd.concat([df, new_row])
print(df)
print()

# add a new rows
new_rows = pd.DataFrame([{"Name": "Pinku", "Age": 17, "Job": "Hopeless"},
                        {"Name": "Sinku", "Age": 24, "Job": "Lifeless"}],
                        index = ["Person 5", "Person 6"])
df = pd.concat([df, new_rows])
print(df)