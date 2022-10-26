from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
power = True

money_machine.report()
print("\n")

print("Options:\n 1. Order drink. \n 2. Report status.\n 3. Power off.")
selection = input(f"Select option:\n")

while power == True:
    options = menu.get_items()

    if selection == 3:
        power = False
    elif selection == 2:
        coffee_maker.report()
    else:
        choice = input(f"Choose from: {options}")
        drink = menu.find_drink(choice)
        print(coffee_maker.is_resource_sufficient(drink))
        print(drink)
