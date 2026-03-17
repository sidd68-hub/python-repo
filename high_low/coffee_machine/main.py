import menu

resource = menu.resource
resource_water = resource['water']
resource_coffee = resource['coffee']
resource_milk = resource['milk']


def check_water(coffee_type):
    if(menu.resource['water'] < resource_water):
        print("Sorry, there is no enough water!")
        return False
    else:
        return True


def check_milk(coffee_type):
    if(menu.resource['milk'] < resource_milk):
        print("Sorry, there is no enough milk!")
        return False
    else:
        return True

def check_coffee(coffee_type):
      if(menu.resource['coffee'] < resource_coffee):
        print("Sorry, there is no enough coffee!")
        return False
      else:
        return True


def check_for_espresso():
    is_water = check_water("espresso")
    is_coffee = check_coffee("espresso") 
    if(is_water and is_coffee):
        print(f"The Espresso will cost ${menu.MENU["espresso"]["cost"]}")
        return True
    return False 

def check_for_latte():
    is_water = check_water("latte")
    is_coffee = check_coffee("latte") 
    is_milk = check_milk("latte") 
    if(is_water and is_coffee and is_milk == True):
        print(f"The Latte will cost $ {menu.MENU["latte"]["cost"]}")
        return True
    return False 

def check_for_cappuccino():
    is_water = check_water("cappuccino")
    is_coffee = check_coffee("cappuccino")
    is_milk = check_milk("cappuccino")  
    if(is_water and is_coffee and is_milk == True):
        print(f"The Cappuccino will cost ${menu.MENU["cappuccino"]["cost"]}")
        return True
    return False

def check_price(coffee_type):
    quarter = int(input("How much quarters?: "))
    dimes = int(input("How much dimes?: "))
    nickles = int(input("How much nickles?: "))
    pennies = int(input("How much pennies?: "))
    total = (0.25 * quarter) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    if total < menu.MENU[coffee_type]['cost']:
        print("Sorry, that's not enough money. Money Refunded ")
    elif total > menu.MENU[coffee_type]['cost']:
        change = total -  menu.MENU[coffee_type]['cost']
        print(f"Here is $ {change} in change.")
        print(f"Here is you {coffee_type} enjoy.")
        global resource_coffee, resource_milk,resource_water 
        resource_coffee -= menu.MENU[coffee_type]['ingredients']['coffee']
        resource_milk -= menu.MENU[coffee_type]['ingredients']['milk']    
        resource_water -= menu.MENU[coffee_type]['ingredients']['water']        
    else:
        resource_coffee -= menu.MENU[coffee_type]['coffee']
        resource_milk -= menu.MENU[coffee_type]['milk']    
        resource_water -= menu.MENU[coffee_type]['water']   
        print(f"Here is you {coffee_type} enjoy.")       




is_exit = False

while not is_exit:
    coffee = str(input("What would you like? (espresso/latte/cappuccino): ").lower())
    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        if(coffee == "espresso"):
            is_resources_available = check_for_espresso()
            if(is_resources_available == True):
                check_price("espresso")
        elif coffee == "cappuccino":
            is_resources_available = check_for_cappuccino()
            if(is_resources_available == True):
                check_price("cappuccino")
        else:
            is_resources_available = check_for_latte()
            if(is_resources_available == True):
                check_price("latte")

    elif coffee.lower() == "report":
        print(f"Report: Water : {resource_water}ml, Coffee : {resource_coffee}ml, Milk : {resource_milk}ml")

    elif coffee.lower() == "exit":
       is_exit = True

    else:        
        print("Please Enter Valid coffee type")    