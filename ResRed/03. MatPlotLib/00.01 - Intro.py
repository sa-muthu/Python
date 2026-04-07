# import matplotlib as mp

# print(mp.__version__) 

import matplotlib.pyplot as plt

x = [2023, 2024, 2025, 2026] # x coordinate
y = [12, 24, 10, 21] # y coordinate

plt.plot(x, y)
# plt.plot(y) # x is default with increment of 1
plt.show()

# can use numpy array - faster and customiseable
import numpy as np
x = np.array([2023, 2024, 2025, 2026]) # x coordinate
y = np.array([12, 24, 10, 21]) # y coordinate
plt.plot(x, y)
plt.show()