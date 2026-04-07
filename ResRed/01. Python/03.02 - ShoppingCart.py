item = input(("Enter item name: "))
price = float(input(f"Enter price of {item}: "))
qty = float(input(f"How many {item}s would you like to buy: "))

total = price * qty

print(f"Total price: {total}")