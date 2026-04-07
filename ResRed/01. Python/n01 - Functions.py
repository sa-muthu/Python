#function = A block of reusable code
#           place () after the function name to invoke it


# # to print 3 time you do or use loop
# print("Happy birthday to you!")
# print("You oldie!")
# print("Happy Birthday")

# print("Happy birthday to you!")
# print("You oldie!")
# print("Happy Birthday")

# print("Happy birthday to you!")
# print("You oldie!")
# print("Happy Birthday")

# but meh

def happy_birthday():
    print("Happy birthday to you!")
    print("You oldie!")
    print("Happy Birthday")
    print()

happy_birthday()
happy_birthday()
happy_birthday()


# adding parameters and arguments

def happy_birthday(name):
    print(f"Happy birthday to {name}!")
    print("You oldie!")
    print("Happy Birthday")
    print()

happy_birthday("steve")
happy_birthday("bro")
happy_birthday("Joe")
  

# two params

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age}!")
    print("Happy Birthday")
    print()

happy_birthday("steve", 12)
happy_birthday("bro", 13)
happy_birthday("Joe", 15  )


# example 
def display_invoice(username, amount, due_date) :
    print(f"Hello {username}")
    print(f"Your bill of ${amount: 2f} is due: {due_date}")

display_invoice("JoeSchmo", 100.01, "01/02")
print()


# return statements
# return = statement used to end a function
#          and send a result back to the caller


def add(x, y):
    z = x + y
    return z

def sub(x, y):
    z = x - y
    return z

def mul(x, y):
    z = x * y
    return z

print(add(3, 4))
print(sub(3, 4))
print(mul(3, 4))
print()

# examples

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

print(create_name("spongebob",))