from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


continue_loop = True

while continue_loop:
  order = input(f"what would you like to order? {menu.get_items()} ")
  drink = menu.find_drink(order)

  if order == "report":
    coffee_maker.report()
    money_machine.report()
  elif order == "off":
    continue_loop = False
  elif drink == None:
    continue_loop = True
  else: 
    if (coffee_maker.is_resource_sufficient(drink)):
      if(money_machine.make_payment(drink.cost)):
        coffee_maker.make_coffee(drink)

  print("\n\n")