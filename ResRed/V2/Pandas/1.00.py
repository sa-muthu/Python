import pandas as pd # You are importing pandas with the alias pd

# 1. Converting a list (Data) into a panda series
# Pandas series is an one dimensional labeled array that can hold any data type
# synonym to a coloumn in spread sheet (1- Dimensional)

# For normal conversion of data to series u can use the function pd.series(input)
# example:
data = [100, "a", "b", 400.34, True] # this is the data
series = pd.Series(data) # conversion of data to series
# NOTE: S is Capital

print(series) # printing the converted data (series)

# These datas are stored with respect to indexing, giving 0 to the first row and following up
# To make it custom, you can give keywork argument as index = ["", "", "", "", ""] in the conversion function
# example:
series_with_index = pd.Series(data, index = ["Integer", "Vowel", "Consonent", "Float", "Boolean"])
print(series_with_index)


# 2. Accessing the Data inside the series
# You can locate inside the Series using the function name.loc["index_name"]
# You can also locate inside the series using index using the function name.iloc[index]
# Locating a data can also be used to change it using assignment operator
# examples:
print(series_with_index.loc["Consonent"])
print(series_with_index.iloc[2])

series_with_index.loc["Consonent"] = "G"
series_with_index.iloc[1] = "E"
print(series_with_index)

# 3. Filtering By Value
# You can filter a value by certain conditions using
# name[name condition]
# example
numerical_data = [1, 5, 3, 4, 3, 2, 5, 5, 6, 3, 4, 5, 7, 3, 4, 2, 3]
numerical_data_series = pd.Series(numerical_data)
larger_datas = numerical_data_series[numerical_data_series > 4]
print(larger_datas)

# 4. Mathematical Operations
# You can perform mathematical operations on the series
# example
print(numerical_data_series.sum())
print(numerical_data_series.mean())
print(numerical_data_series.median())
print(numerical_data_series.mode())
print(numerical_data_series.std())
print(numerical_data_series.var())
print(numerical_data_series.min())
print(numerical_data_series.max())
print(numerical_data_series.count())
print(numerical_data_series.unique())
print(numerical_data_series.value_counts())
# you dont have to memorise all this, you can use the function name.describe() to see all this, or just use help(pd.Series)

# 5. Creating a series from a dictionary
# example:
data = {"a": 1, "b": 2, "c": 3}
data_series = pd.Series(data)
print(data_series)

# 6. Creating a series from a numpy array
# example:
import numpy as np
data = np.array([1, 2, 3, 4, 5])
data_series = pd.Series(data)
print(data_series)

# 7. Creating a series from a scalar value
# example:
data = 10
data_series = pd.Series(data, index = ["a", "b", "c", "d", "e"])
print(data_series)

print(numerical_data_series.describe())
print(help(pd.Series))