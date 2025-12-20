#Password Generator Project
import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

min_chars = 6

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if nr_letters + nr_numbers + nr_symbols < min_chars:
    print(f"Invalid input, password must be min. of {min_chars} characters.")
    sys.exit()

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""

if nr_letters > 0:
    for count in range(nr_letters):
        rand_letter = random.choice(letters)
        password += rand_letter
if nr_symbols > 0:
    for count in range(nr_symbols):
        rand_symbol = random.choice(symbols)
        password += rand_symbol
if nr_numbers > 0:
    for count in range(nr_numbers):
        rand_number = random.choice(numbers)
        password += rand_number

print("Password: ", password)
#Hard Level - Order of characters randomised:

pwd_list = []
for letter in password:
    pwd_list.append(letter)
random.shuffle(pwd_list)

randomized_password = ""
for letter in pwd_list:
    randomized_password += letter

print("Randomized password: ", randomized_password)
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P