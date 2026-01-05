from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    request = input(f"What would you like? ({menu.get_items()}): ").lower()
    if request == "off":
        print("Turning machine off.")
        is_on = False
    elif request == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(request) is not None:
        coffee = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(coffee):
            if money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)