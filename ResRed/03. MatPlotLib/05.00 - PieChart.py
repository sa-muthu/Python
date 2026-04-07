import matplotlib.pyplot as plt
import numpy as np

# Pie Chart = Circular chart divided into slices to show percentages of total.
#             Good for visualising distributions among categories

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([20, 30, 4, 10])

colors = ["red", "black", "pink", "grey"]

plt.pie(values, labels = categories,
                autopct = "%1.1f%%",
                colors = colors,
                explode = [0, 0.1, 0, 0],
                shadow = True,
                startangle = 90)

plt.title("No of Students ")

plt.show()