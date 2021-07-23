from money_machine import MoneyMachine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from prettytable import PrettyTable
import os


def clear(): os.system('cls')


def clear_screen():
    ask = input("Screen will be cleared after input:\n").lower()
    if ask == 'y':
        clear()
    else:
        clear()


money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
table_1 = PrettyTable()
table_1.add_column("Coffee", ["latte", "espresso", "cappuccino"])
table_1.add_column("Price", ["$2.5", "$1.5", "$3"])
table_1.align = "l"
loop = True
while loop:
    print(table_1)
    choice = input("What would you like?\n").lower()
    if choice == 'off':
        loop = False
    elif choice == 'report':
        coffee.lol()
        money.report()
        clear_screen()
    elif choice == 'latte' or choice == "espresso" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)
            clear_screen()
        else:
            clear_screen()
    else:
        print("Error Error Error Error Error")
        clear_screen()
