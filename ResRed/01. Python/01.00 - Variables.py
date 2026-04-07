# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

#strings
first_name = "Muthu"
color = "Black"
email = "Mut123@mail.com"

print(first_name)
print(f"Hello {first_name}, you like {color}.") #called as fstring
print(f"Your mail is {email}.")


#integers (number)
age = 19
qty = 30

print(f"You are {age} years old.")
print(f"You've bought {qty} items.")


#float (number with decimal)
price = 10.99
gpa = 8.9

print(f"Price = ${price}")
print(f"Your gpa is {gpa}")


#boolean
is_student = False
for_sale = False

print(f"Are you a student?: {is_student}")
if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")