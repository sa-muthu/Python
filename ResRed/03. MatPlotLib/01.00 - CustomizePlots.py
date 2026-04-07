import matplotlib.pyplot as plt
import numpy as np

# x = np.array([2023, 2024, 2025, 2026]) # x coordinate
# y = np.array([12, 24, 10, 21]) # y coordinate

# plt.plot(x, y, marker = "o",
#                markersize = 20, # or ms
#                markerfacecolor = "red",# or hex code - only works on filled markers
#                markeredgecolor = "black", 
#                linestyle = "dashed", # default is solid # none will not show any
#                linewidth = 2,  # default is 1
#                color = "pink")
# plt.show()

x = np.array([2023, 2024, 2025, 2026]) # x coordinate
y1 = np.array([12, 24, 10, 21]) # y coordinate
y2 = np.array([15, 25, 1, 2])

# plt.plot(x, y1, marker = "o",
#                markersize = 20, # or ms
#                markerfacecolor = "red",# or hex code - only works on filled markers
#                markeredgecolor = "black", 
#                linestyle = "dashed", # default is solid # none will not show any
#                linewidth = 2,  # default is 1
#                color = "pink")

# plt.plot(x, y2) # to make it similar you can copy paste the above for y2 but meh too much work

line_style = dict(marker = "o",
                  markersize = 20, # or ms
                  markerfacecolor = "red",# or hex code - only works on filled markers
                  markeredgecolor = "black", 
                  linestyle = "dashed", # default is solid # none will not show any
                  linewidth = 2)  # default is 1
                # color = "pink") # cancel as default

# plt.plot(x, y1, **line_style)
# plt.plot(x, y2, **line_style)

plt.plot(x, y1, colour = "red", **line_style)
plt.plot(x, y2, colour = "blue", **line_style)

plt.show()