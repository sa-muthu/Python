"""
2.00 Output and Comments

This script demonstrates two fundamental aspects of Python programming: 
outputting data using the `print()` function, and writing code comments to 
explain your logic.
"""

# ==============================================================================
# Part 1: Using print() to Output Values
# ==============================================================================

# 1. Basic Usage
# The print() function is the simplest way to display output in Python.
print("Hello, world")

print("\n---")

# 2. Printing Variables
# You can pass variables directly into the print() function
name = "Muthu"
age = 20

print(name)
print(age)

print("\n---")

# 3. Printing Multiple Values
# Print multiple items by separating them with commas. By default, it adds a space.
print("Name:", name, "Age:", age)

print("\n---")

# 4. Using f-strings (Recommended)
# F-strings provide a cleaner and more modern way to format strings.
print(f"Name: {name}, Age: {age}")

print("\n---")

# 5. Controlling Separators (sep)
# The `sep` parameter changes the character that separates multiple items.
print("2026", "04", "02", sep="-")

print("\n---")

# 6. Controlling Line Endings (end)
# By default, print() ends with a newline (\n). Use `end` to change this.
print("Hello", end=" ")
print("World")

print("\n---")

# 7. Printing Special Characters
# Use escape characters like \n (new line) and \t (tab).
print("Line1\nLine2")
print("Tab\tSpace")

print("\n---")

# 8. Printing Expressions
# print() evaluates expressions before printing the result.
print(2 + 3)

print("\n---")

# 9. Printing Formatted Numbers
# Control number formatting, like decimal places, inside f-strings.
pi = 3.14159
print(f"Pi rounded: {pi:.2f}")

print("\n---")

# 10. Common Beginner Mistakes
# - Missing quotes: print(Hello)  # This will cause an error if Hello is not a string variable!
# - Forgetting commas: print("Age:" age)  # This is a syntax error!


# ==============================================================================
# Part 2: Working with Comments
# ==============================================================================

# 1. Single-line Comments (#)
# Use the # symbol for short explanations on a single line.
x = 10  # Assign 10 to x. Everything after # is ignored.

# 2. Multi-line Strings as Comments (''' or """)
# Python does not officially have a dedicated syntax for multi-line comments. 
# We use triple quotes to write a multi-line string that is ignored by Python.
"""
This looks like a multi-line comment,
but it is actually a multi-line string.
Python creates the string but ignores it since it's not assigned.
"""

# 3. The Proper Way to Write Multi-line Comments
# The recommended way (PEP 8) is to use multiple # lines instead:

# This is a proper multi-line comment
# explaining something in detail
# across several lines

# 4. Docstrings
# Triple quotes are meant for docstrings, which document functions and classes.
def add(a, b):
    """Return the sum of a and b."""
    return a + b


