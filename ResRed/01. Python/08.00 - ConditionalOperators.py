# Conditional/Ternary operator = A one-line shortcut for the if-else statement
#                                Print or assign one of the two values based on a condition
#                                X if condition else Y

num1 = 5
num2 = 7
age = 19
user_role = "admin"

print("Positive" if num1 > 0 else "Negative")

print("Even" if num1 % 2 == 0 else "ODD")

max_num = num1 if num1 > num2 else num2
print(max_num)

min_num = num1 if num1 < num2 else num2
print(min_num)

status = "Adult" if age >= 18 else "child"
print(status)

access = "Access Granted" if user_role == "admin" else "Access Denied."