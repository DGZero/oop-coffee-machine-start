import menu
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
machine = MoneyMachine()


is_on = True

while is_on:
    coffee_options = input(f"What would you like? ({Menu.get_items(menu)}): ")
    if coffee_options == "off":
        is_on = False
    elif coffee_options == "report":
        coffee_maker.report()
        machine.report()
    else:
        drink = Menu.find_drink(menu,coffee_options)
        if coffee_maker.is_resource_sufficient(drink) and machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            





