# Hypotenuse fo a triangle c = root (a^2 + b^2)

import math

base = float(input("Enter the measurement of first side: "))
adjacent = float(input("Enter the measurement of second side: "))

hypotenuse = pow(pow(base, 2) + pow(adjacent, 2), 0.5)
# hypotenuse = math.sqrt(pow(base, 2) + pow(adjacent, 2))


print(f"Hypotenuse = {hypotenuse}")