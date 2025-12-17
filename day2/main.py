print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? %"))
people = int(input("How many people to split the bill? "))

result = round((bill + (bill * tip/100))/people, 2)

print("Each person should pay: $" + str(result))
