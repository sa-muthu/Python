import matplotlib.pyplot as plt
import numpy as np

# scatter graph = shows the relationship between two variables
#                 Helps to identify a correlation (+, -, None)
#                 Example: Study hours vs Time

x = [0, 1, 2, 3, 4, 5, 6, 7, 7, 8]
y = [55, 60, 65, 62, 68, 70, 68, 65, 70, 72]

x2 = [0, 3, 4, 5, 3, 2, 5, 2, 2, 4]
y2 = [10, 60, 11, 72, 24, 32, 64, 65, 75, 72]

plt.xlabel("Hours studied")
plt.ylabel("Scores")
plt.title("Hours Studied vs Score")
plt.scatter(x, y, color = "black",
                  alpha = 0.5, #transparency
                  s = 50,  #size  
                  label = "Class A")

plt.scatter(x2, y2, color = "red",
                  alpha = 0.5, #transparency
                  s = 50, #size 
                  label = "Class B") 

plt.legend()
plt.show()
