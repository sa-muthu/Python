import matplotlib.pyplot as plt
import numpy as np

# Figure = the entire canvas
# Ax     = A single plot (subplot)

# print(plt.subplots(3, 2))


figure, axes = plt.subplots(2, 2) 

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

axes[0, 0].plot(x, x*2, color = "black")
axes[0, 0].set_title ("x*2")

axes[0, 1].bar(x, x**2, color = "red")
axes[0, 1].set_title ("x**2")

axes[1, 0].barh(x, x**3, color = "green")
axes[1, 0].set_title ("x**3")

axes[1, 1].scatter(x, x**4, color = "blue")
axes[1, 1].set_title ("x**4")

plt.tight_layout()
plt.show()