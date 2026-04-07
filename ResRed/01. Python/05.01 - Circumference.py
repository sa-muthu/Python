#Circumference = 2 pi r

import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"Circumference of the Circle of radius {radius}cm is: {round({circumference}, 2)}cm")