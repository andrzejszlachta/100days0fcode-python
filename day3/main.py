# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# number = int(input("Type a number: "))
# isEven = number % 2
#
# if isEven == 0:
#     print("Your number is even.")
# else:
#     print("Your number is odd.")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("What is age? "))
    if 45 <= age <= 55:
        print("Tickets for people 45 to 55 are free!")
    elif age >= 18:
        bill += 12
        print("Adult tickets are $12.")
    elif age >= 12:
        bill += 7
        print("Youth tickets are $7.")
    else:
        bill += 5
        print("Child tickets are $5.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes or n for No.")
    if wants_photo == "y":
        #add 3$ to bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ").lower()
#
# bill = 0
#
# if size == "s":
#     bill += 15
# else:
#     if size == "m":
#         bill += 20
#     elif size == "l":
#         bill += 25
#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     if pepperoni == "y":
#         bill += 3
#     else:
#         print("Sorry, you typed wrong size.")
#
# extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
# if extra_cheese == "y":
#     bill += 1
#
# print(f"Your final bill is: ${str(bill)}.")