import os
os.system('cls')
from machine_data import *
from art import logo


def show_resources():
    """Shows the current supplies of the machine"""
    for name, value in resources.items():
        if name == "coffee":
            print(f"{name.capitalize()}: {value}gr")
        else:
            print(f"{name.capitalize()}: {value}ml")
    print(f"Money: ${profit}")


def is_resource_sufficient(drink_requirements):
    """Compares the user's drink requirements with current suplies of the machine"""
    drink_requirements = MENU[drink_requirements]
    ingredient_for_drink = drink_requirements['ingredients']

    for ingredient in ingredient_for_drink:
        if resources[ingredient] >= ingredient_for_drink[ingredient]:
            print(f"Check {ingredient}")
        else:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True
    

def process_coins():
    """Asks the user to insert coins and returns the sum of the order"""
    total = 0
    coins = {
        "ten pesos": 10,
        "five pesos": 5,
        "two pesos": 2,
        "one peso": 1
    }

    for coin in coins:
        user_coins = int(input(f"How many {coin}?: "))
        total += (user_coins * coins[coin])
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    Compares the user money input against the coffee cost and establishes that 
    transaction can be made
    """
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit  # variable from machine data
        change = money_received - drink_cost

        print(f"Here is ${change} in change.")
        profit += drink_cost

        return True


def make_coffee(drink_name, order_ingredients):
    """Deliver coffee order only if there are enough ingredients"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]

    print(f"Here is your {drink_name} ☕. Enjoy!")

machine_operating = True
while machine_operating:
    print(logo)
    order = input("What would you like? (espresso/latte/cappuccino):\t").lower()

    if order == 'off':
        machine_operating = False
    elif order == 'report':
        show_resources()
    elif order in ['espresso', 'latte', 'cappuccino']:
        if is_resource_sufficient(drink_requirements=order): 
            user_paid = process_coins()
            if is_transaction_successful(money_received=user_paid, drink_cost=MENU[order]['cost']):
                make_coffee(drink_name=order, order_ingredients=MENU[order]['ingredients'])
    else:
        continue
