import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([12, 23, 35, 20])
y2 = np.array([21, 32, 53, 2])
y3 = np.array([3, 5, 8, 2])

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.title("MAMA MIA",fontsize = 20,
                     family = "Arial",
                     fontweight = "bold",
                     color = "Black")

plt.xlabel("Year", fontsize = 10,
                   family = "Arial",
                   fontweight = "bold",
                   color = "Blue")

plt.ylabel("Wtv", fontsize = 10,
                  family = "Arial",
                  fontweight = "bold",
                  color = "Blue")

plt.xticks(x)

plt.tick_params(axis = "y",
                color = "Pink")

plt.subplots_adjust(bottom = 0.5,
                    left = 0.5)

plt.show()