# from day10 import art
#
# operators = "+\n-\n*\n/"
#
# def get_result(f_num, operator, sec_num):
#     result = 0
#     if operator == "+":
#         result = f_num + sec_num
#     elif operator == "-":
#         result = f_num - sec_num
#     elif operator == "*":
#         result = f_num * sec_num
#     elif operator == "/":
#         result = f_num / sec_num
#
#     print(f"{f_num} {operator} {sec_num} = {result}")
#
#     keep_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.: ")
#     if keep_result == "y":
#         get_result(result, input("Pick an operation: "), int(input("What's the next number?: ")))
#     elif keep_result == "n":
#         get_result(int(input("What's the first number?: ")), input("+\n-\n*\n/\nPick an operation: "), int(input("What's the next number?: ")))
#
# print(art.logo)
# get_result(int(input("What's the first number?: ")), input("+\n-\n*\n/\nPick an operation: "), int(input("What's the next number?: ")))

from day10 import art

def add(n1, n2):
    return n1+n2
def subtract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def start_calculator(keep_result = "n", result = 0):
    if keep_result == "y":
        first_num = result
    else:
        print(art.logo)
        first_num = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operator = input("Pick an operation: ")
    while operator not in operations:
        print("Pick correct symbol.")
        operator = input("Pick an operation: ")
    sec_num = float(input("What's the next number?: "))

    result = operations[operator](first_num, sec_num)
    print(f"{first_num} {operator} {sec_num} = {result}")

    keep_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.: ")
    if keep_result == "y":
        start_calculator(keep_result, result)
    elif keep_result == "n":
        start_calculator()

start_calculator()
