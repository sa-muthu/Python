# List Comprehensions = A way to create lists in Python
#                       Compact and easier to read than tradional loops 
#                       [expression for value in iterable if condition]

# doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles) - alot to write

# shortcut!

# doubles = [expression for value in iterable]
doubles = [x*2 for x in range(1, 11)]
print(doubles)

# examples
triples = [y*3 for y in range(1, 11)]
print(triples)

squares = [z*z for z in range(1, 11)]
print(squares)


#strings

fruits = ["apple", "orange", "banana", "coconut"]
# uppercase_fruits = fruits.upper() # assign to new or reassign
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
# or just fruits = [fruit.upper() for fruit in  ["apple", "orange", "banana", "coconut"]]

fruits_chars = [fruit[0] for fruit in fruits]
print(fruits_chars)


# conditions

numbers = [1, -2, 3, -4, 5, -6]
pos_num = [num for num in numbers if num >= 0]
print(pos_num)

neg_num = [num for num in numbers if num < 0]
print(neg_num)

even_num = [num for num in numbers if num % 2 == 0]
print(even_num)

odd_num = [num for num in numbers if num % 2 != 0]
print(odd_num)


# example

grades = [85, 42, 79, 90, 56, 61, 30]
pass_grade = [grade for grade in grades if grade >= 60]
print(pass_grade)
