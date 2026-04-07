#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[4])
print(credit_number[5:9]) #starting index is inclusive, ending index is exclusive
print(credit_number[:4])
print(credit_number[5:])
print(credit_number[-4])
print(credit_number[::2])

#get last four digits of credit card
print(credit_number[-4:])