# collection = single "variable" used to store multiple values
# Tuples        = () ordered, unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")

# print(dir(fruits)) #possible operations
# print(help(fruits))

print(len(fruits)) #no of elements
print("pineapple" in fruits) #check for an element

print()

# only two attribute is possible
# print(fruits.index("apple"))
# print(fruits.count("coconut"))


for fruit in fruits:
    print(fruit)