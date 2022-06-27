from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
order = Menu()
resource_suf = CoffeeMaker()
payment = MoneyMachine()

while on:
    choice = input("Which drink do you want? espresso, latte or cappuccino")
    drink = order.find_drink(choice)
    if choice == "off":
        on = False
    elif choice == 'report':
        resource_suf.report()
        payment.report()
    elif choice in order.get_items():
        if resource_suf.is_resource_sufficient(drink):
            if payment.make_payment(drink.cost):
                resource_suf.make_coffee(drink)
            else:
                print("Insufficient payment")
        else:
            print("There are not enough ingredients")





