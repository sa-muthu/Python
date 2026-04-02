"""
1.02.03 Variables and Assignments Demo

This script demonstrates the concepts from the "Variables and Assignments" guide in action.
You can run this file to see how Python handles assignments, typing, and memory.
"""

# ==============================================================================
# 1. Basic Variable Creation
# ==============================================================================
print("--- 1. Basic Variables ---")
x = 10
name = "Alice"
print(f"Decimal (x): {x}")
print(f"String (name): {name}")


# ==============================================================================
# 2. Dynamic Typing
# ==============================================================================
print("\n--- 2. Dynamic Typing ---")
data = 10.5
print(f"data = {data}, Type: {type(data)}")

data = "Python"
print(f"data = {data}, Type: {type(data)}")


# ==============================================================================
# 3. Memory Identity (id)
# ==============================================================================
print("\n--- 3. Memory Identity ---")
a = 500
b = 500
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")

print("Assigning b = a...")
b = a
print(f"a = {a}, id(a) = {id(a)}")
print(f"b = {b}, id(b) = {id(b)}")


# ==============================================================================
# 4. Multiple Assignment
# ==============================================================================
print("\n--- 4. Multiple Assignment ---")
p, q, r = 1, 2, 3
print(f"p: {p}, q: {q}, r: {r}")

# Swapping variables in one line!
print("Swapping p and q...")
p, q = q, p
print(f"p: {p}, q: {q}")


# ==============================================================================
# 5. Augmented Assignment
# ==============================================================================
print("\n--- 5. Augmented Assignment ---")
score = 100
print(f"Initial score: {score}")

score += 50  # score = score + 50
print(f"After score += 50: {score}")

score *= 2   # score = score * 2
print(f"After score *= 2:  {score}")


# ==============================================================================
# 6. Deleting Variables
# ==============================================================================
print("\n--- 6. Deleting Variables ---")
temp_var = "I'm about to disappear"
print(f"temp_var exists: {temp_var}")

del temp_var
print("temp_var has been deleted.")

# Accessing temp_var now would cause a NameError
# print(temp_var) 
