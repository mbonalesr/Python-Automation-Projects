import os
os.system('cls')
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

logo = '''

  ______   ______    _______  _______  _______  _______    .___  ___.      ___       ______  __    __   __  .__   __.  _______ 
 /      | /  __  \  |   ____||   ____||   ____||   ____|   |   \/   |     /   \     /      ||  |  |  | |  | |  \ |  | |   ____|
|  ,----'|  |  |  | |  |__   |  |__   |  |__   |  |__      |  \  /  |    /  ^  \   |  ,----'|  |__|  | |  | |   \|  | |  |__   
|  |     |  |  |  | |   __|  |   __|  |   __|  |   __|     |  |\/|  |   /  /_\  \  |  |     |   __   | |  | |  . `  | |   __|  
|  `----.|  `--'  | |  |     |  |     |  |____ |  |____    |  |  |  |  /  _____  \ |  `----.|  |  |  | |  | |  |\   | |  |____ 
 \______| \______/  |__|     |__|     |_______||_______|   |__|  |__| /__/     \__\ \______||__|  |__| |__| |__| \__| |_______|
                                                                                                                                                                                                                                                                                                                                                               

'''

my_coffee = CoffeeMaker()
my_menu = Menu()
my_cashier = MoneyMachine()

machine_working = True

while machine_working:
    print(logo)
    order = input(f"What would you like? {my_menu.get_items()}:\t").lower()

    if order == 'off':
        print("Turning OFF")
        machine_working = False
    elif order == 'report':
        os.system('cls')
        my_coffee.report()
        my_cashier.report()
    elif order in ['espresso', 'latte', 'cappuccino']:
        drink = my_menu.find_drink(order)
        if my_coffee.is_resource_sufficient(drink=drink):
            if my_cashier.make_payment(cost=drink.cost):
                my_coffee.make_coffee(order=drink)
    else:
        continue
    