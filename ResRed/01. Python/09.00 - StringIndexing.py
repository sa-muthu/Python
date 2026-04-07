name = input("Enter your full name:")

print(len(name)) #gives length of the string
print(name.find("u")) #first occureence
print(name.rfind("u")) #last occurrence
print(name.capitalize) #capitalise
print(name.upper()) #all upper
print(name.lower()) #all lower
print(name.isdigit()) #if all digit, is true
print(name.isalpha()) #if all alphabetical character (space is not alpha)
print(name.count("u")) #count no of u
print(name.replace("u", ""))

print(help(str))