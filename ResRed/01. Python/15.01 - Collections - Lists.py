# collection = single "variable" used to store multiple values
# Set        = {} unordered, immutable(unchangeable) but can ADD/REMOVE. NO duplicates

fruits = {"apple", "banana", "coconut", "orange"} #unordered
print(fruits)

# print(dir(fruits)) #possible operations
# print(help(fruits))

print(len(fruits)) #no of elements
print("pineapple" in fruits) #check for an element

print()

# #changeable
# print(fruits[0]) #error

# for fruit in fruits: 
#     print(fruit)

# print()

#add/ remove
fruits.add("pineapple") #not append
fruits.remove("coconut")
fruits.pop() #remove the first element (random)

for fruit in fruits: 
    print(fruit)

print()

# #to insert - error
# fruits.insert(0, "kiwi")

# for fruit in fruits: 
#     print(fruit)

# print()

# #alphabetical order - error
# fruits.sort() #to sort them
# fruits.reverse() #to reverse them (to reverse them alphabetically, use sort before reverse).


# for fruit in fruits: 
#     print(fruit)

# print()


# #to find the index - error
# print(fruits.index("litchi"))


# to find no of elements by name - error
# print(fruits.count("kiwi"))

#to remove all elements
fruits.clear()

for fruit in fruits: 
    print(fruit)

print()
