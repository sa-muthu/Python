# collection = single "variable" used to store multiple values
# List       = [] ordered and changeable. Duplicates OK


fruits = ["apple", "orange", "banana", "coconut"]
print(fruits)
print(fruits[0])
print(fruits[0:3]) #range
print(fruits[0:3:2]) #steps
print(fruits[::-1])

for fruit in fruits: #list every
    print(fruit)

# print(dir(fruits)) #possible operations
# print(help(fruits))

print(len(fruits)) #no of elements
print("pineapple" in fruits) #check for an element

print()

#changeable
fruits[0] = "litchi"

for fruit in fruits: 
    print(fruit)

print()

#add/ remove
fruits.append("pineapple")
fruits.remove("coconut")

for fruit in fruits: 
    print(fruit)

print()

#to insert
fruits.insert(0, "kiwi")

for fruit in fruits: 
    print(fruit)

print()

#alphabetical order
fruits.sort() #to sort them
fruits.reverse() #to reverse them (to reverse them alphabetically, use sort before reverse).


for fruit in fruits: 
    print(fruit)

print()


#to find the index
print(fruits.index("litchi"))


#to find no of elements by name
print(fruits.count("kiwi"))

#to remove all elements
fruits.clear()

for fruit in fruits: 
    print(fruit)

print()
