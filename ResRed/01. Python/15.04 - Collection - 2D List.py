fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrot", "potatoes"]
meat =       ["chicken", "fish", "pork"]

groceries = [fruits, vegetables, meat]

print(groceries)
print()

print(groceries[0])
print()

print(groceries[1][2])
print()


# groceries can be written as

groceries2 = [["apple", "orange", "banana", "coconut"], ["celery", "carrot", "potatoes"], ["chicken", "fish", "pork"]]

if groceries == groceries2:
    print("yes")
else:
    print("no")

print()


for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()

#the same can be used for sets{tuple} or wtv