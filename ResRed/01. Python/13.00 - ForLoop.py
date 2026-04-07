# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

for x in range(1, 11): 
    print(x)

for y in reversed(range(1, 11, 2)):
    print(y)

for z in range(1, 11):
    if z == 6:
        continue
    else:
        print(z)