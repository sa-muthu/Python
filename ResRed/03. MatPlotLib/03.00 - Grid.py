import matplotlib.pyplot as plt
import numpy as np

# grid () = Helps make plots easier to read by adding reference lines.

x =[1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 10, 15, 20, 25, 30, 35, 40, 45]

plt.grid() # or (axis = "x")
plt.grid(axis = "x",
         linewidth = 2,
         color = "Blue",
         linestyle = "dashed")

plt.plot(x,y)
plt.show()