from menu import Menu, MenuItem
from coffe_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machime = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? {option}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        money_machime.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffe_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machime.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffe_maker.make_coffee(drink)
