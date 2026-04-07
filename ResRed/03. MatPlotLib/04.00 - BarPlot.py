import matplotlib.pyplot as plt
import numpy as np

# Bar Plot = compare categories of data by representing each category with a bar

categories = ["Grains", "Fruits", "Veggies", "Proteins", "Dairies", "Sweets"]
values = [4, 3, 2, 5, 3, 1]

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

# plt.bar(categories, values, color = "black")
plt.barh(categories, values, color = "black")


plt.show()