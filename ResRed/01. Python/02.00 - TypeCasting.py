# TypeCasting = The process of converting a varible from one date type to another
#               str(), int(), float(), bool()

name = "Muthu S A"
age = 19
gpa = 8.89
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)
print(type(gpa))

age = float(age)
print(age)
print(type(age))

str(age)
print(age)
print(type(age))

age += 1 #not possible with str, only with float and int
age += "1" #not possible with int and float, only with str (string concatanation)

name = bool(name)
print(name) #always gives true for str, except if there is no string at all, it'll give false
print(type(name))