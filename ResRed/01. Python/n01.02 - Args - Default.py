# default arguments = A default value for certain parameters
#                     default is used  when that argument is omitted
#                     make your function more flexible, reduces no of arguments
#                     1. postional, 2. Default, 3. keyword, 4. Arbitary

# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500)) - throws error

def net_price(list_price, discount = 0.30, tax = 18):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500)) 