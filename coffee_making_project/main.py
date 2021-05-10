from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_is_working = True
cm=CoffeeMaker()
mm=MoneyMachine()
m=Menu()

while machine_is_working:
	options=m.get_items()
	response = input(f"What would you like? {options}")
	if response=="off":
		machine_is_working=False
	elif response=="report":
		cm.report()
		mm.report()
	else:
		drink=m.find_drink(response)
		is_enough_ingredients = cm.is_resource_sufficient(drink)
		if is_enough_ingredients:
			is_payment_successful = mm.make_payment(drink.cost)
		if is_enough_ingredients and is_payment_successful:
			cm.make_coffee(drink)