#Logical Operators = evaluate multiple conditions (or, and, not)
#                    or = at least one condition must be true
#                    and = both the conditions must be true
#                    not = inverts the condition (not False, not true)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")



is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside and is sunny.")
elif temp <= 0 and is_sunny: 
    print("It is cold outside and is sunny")
elif temp < 28 and temp > 0 and is_sunny: #elif 28 > temp > 0 and is_sunny:
    print("It is warm outside and is sunny")

if temp >= 28 and not is_sunny:
    print("It is hot outside and is not sunny.")
elif temp <= 0 and not is_sunny: 
    print("It is cold outside and is not sunny")
elif temp < 28 and temp > 0 and not is_sunny: #elif 28 > temp > 0 and is_sunny:
    print("It is warm outside and is not sunny")