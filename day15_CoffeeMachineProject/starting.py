# Coffee machine project
from typing import Dict

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

current_balance = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_requirements):
    """Returns True if resources meet requirements, else False"""
    for ingredient in order_requirements:
        if order_requirements[ingredient] >= resources[ingredient]:
            print(f"Insufficient {ingredient}. Please select another option or replenish {ingredient}.")
            return False
    return True

def inserted_coins():
    """Returns the total value of inserted coins."""
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def payment_successful():
    """Return True if payment cost, else return False."""
    while payment < cost:
        return False
    else:
        print("Payment successful.")
        return True

power = True

while power == True:
    options = input("Select option: 1. Place an order.\n 2. Display machine status.\n 3. Power off machine.\n Your selection: ")

    # TODO Prompt user by asking "What would you like? (espresso/latte/capuccino):"
    # TODO Check resources sufficient?

    if options == "1":
        order = input("Select your order: 1. Espresso 2. Latte 3. Capuccino).\n")

        if order == "1":
            order_requirements = MENU["espresso"]
            cost = MENU["espresso"]["cost"]
            print(f"Insert ${cost}.")
            payment = inserted_coins()
            payment_successful()
            check_resources(order_requirements)

            print("Insert coins.")

        elif order == "2":
            order_requirements = MENU["latte"]
            cost = MENU["latte"]["cost"]
            print(f"Insert ${cost}.")
            payment = inserted_coins()
            payment_successful()
            check_resources(order_requirements)

            print("Insert coins.")

        elif order == "3":
            order_requirements = MENU["espresso"]
            cost = MENU["espresso"]["cost"]
            print(f"Insert ${cost}.")
            payment = inserted_coins()
            payment_successful()
            check_resources(order_requirements)

    # TODO Print report

    # elif options == "2":
        # for resource in resources:
            # print([resource])

    # TODO Turn off the Coffee Machine by entering "off" to the prompt.

    # elif options == "3":
    #     power = False
    #     return power