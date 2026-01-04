MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

def add_money(val):
    global profit
    profit += val

def reduce_resources(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]

def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")

def is_enough_resources(coffee):
    is_enough = True
    for ingredient in MENU[coffee]["ingredients"]:
        if resources[ingredient] < MENU[coffee]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            is_enough = False
    return is_enough

def make_coffee(coffee):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    value = round(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01, 2)
    price = MENU[coffee]["cost"]

    if value < price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        add_money(price)
        if value > price:
            print(f"Here is ${value - price} in change.")
        reduce_resources(coffee)
        print(f"Here is your {coffee}. Enjoy!")

while is_on:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if request in MENU:
        if is_enough_resources(request):
            make_coffee(request)
    elif request == "report":
        print_report()
    elif request == "off":
        print("Turning machine off.")
        is_on = False
