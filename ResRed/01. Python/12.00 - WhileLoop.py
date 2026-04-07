# while loop = execute some code WHILE some conditions remains true

name = input("Enter your name: ")

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello, {name}!")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello, {name}!")




age = int(input("Enter your age: "))

while age < 0:
    print("Name can not be negative, mister/miss.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")




food = input("Enter your favourite car (Enter 'q' to quit): ")

while not food == 'q':
    print(f"Woah! {food} is amazing, What else is your favourite: ")
    food = input("Enter your favourite car (Enter 'q' to quit): ")

print("Thank you!")




num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num > 10:
    num = input(print(f"Invalid, Please enter a valid number between 1 to 10: "))

print(f"Entered number is {num}")