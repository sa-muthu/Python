response = input("Would you like some food? (Y/N): ")

if response == "Y":
    print("Server will be at your table in a minute, to take orders.")
elif response == "N":
    print("Thank You! Visit Again.")
else:
    print("Please enter a valid input (Y/N).")
