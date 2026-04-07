# Iterables = An object/collection that can return its elements one at a time.
#             allowing it to be iterated over a loop


#List

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
print()

for number in reversed(numbers):
    print(number)
print()

for number in numbers:
    print(number, end = "-")



#Tuples

numbers = {1, 2, 3, 4, 5}

for number in numbers:
    print(number)
print()

# for number in reversed(numbers):
#     print(number)
# print() - throws error

for number in numbers:
    print(number, end = "-")



# Sets

numbers = {1, 2, 3, 4, 5}

for number in numbers:
    print(number)
print()

# for number in reversed(numbers):
#     print(number)
# print() - throws error

for number in numbers:
    print(number, end = "-")



# Dictionaries

my_dict = {"A": 1, "B": 2, "C": 3}

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key} = {value}")