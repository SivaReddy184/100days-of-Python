from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    drink = input(f"What would you like? ({menu.get_items()}): ")
    if drink == "off":
        is_on = False
    elif drink == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        choice = menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)



