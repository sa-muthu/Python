#nested loop = A loop within another loop (outer, inner)
#              outer loop:
#                  inner loop:

# for x in range(1, 10):
#     print(x, end = "") #in default end = "\n"

# to repeat the above 3 times.

for x in range(3):
    for y in range(1, 10):
        print(y, end = "") #in default end = "\n"
    print()