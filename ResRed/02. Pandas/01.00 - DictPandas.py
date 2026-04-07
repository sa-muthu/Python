import pandas as pd

data = {"A": 12, "B": 24, "C": 23}

series = pd.Series(data)

print(series)
print(series.loc["A"])

series.loc["A"] += 50

print(series)
print(series.loc["A"])

print(series[series >= 24])