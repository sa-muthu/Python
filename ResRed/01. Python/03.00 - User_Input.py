# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

input("What is your name?: ")

age = input("What is your age?: ")

#age = age + 1, gives error, input is stored as str

age = int(age)

age = age + 1

print(f"Hi, you are {age} years old")

salary = int(input("What is your salary?: "))
print (f"Salary = {salary + 1000}")