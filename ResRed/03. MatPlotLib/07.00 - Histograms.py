import matplotlib.pyplot as plt
import numpy as np

# Histogram = A visual representation of the distribution of quatitive data.
#             They group values into bins (intervals)
#             and counts how many fall in each range


scores = np.random.normal(loc = 60, scale = 50 , size = 100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins = 10,
                 color = "black",
                 edgecolor = "green")

plt.title("Iyaa")
plt.xlabel("Hmm")
plt.ylabel("Grrr")

plt.show()