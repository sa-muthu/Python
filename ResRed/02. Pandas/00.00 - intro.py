import pandas as pd

# print(pd.__version__)

# Series = A one dimensional labeled array that can hold any data type
#          Think of it like a single coloumn in a spreadsheet (1 - dimentional)

# data = [100, 200, 300]
# series = pd.Series(data)
# print(series)


data = [100, 200, 300, 400, 500]
series = pd.Series(data, index = ["Sky", "Space", "Universe", "idk", "ydk"])
print(series)

# to access location
print(series.loc["Sky"])

#to change value
series.loc["Sky"] = 50

# to access location by index
print(series.iloc[0]) #iloc

#filter by value
print(series[series >= 350])
