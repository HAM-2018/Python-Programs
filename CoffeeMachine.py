
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = 0

def is_resource_sufficient(order):
    for item in order:
        if resources[item] < order[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_order(order, drink_name):
    if is_resource_sufficient(order):
        for item in order:
            resources[item] -= order[item]
        print(f"Here is your {drink_name}")
        return drink_name
    return None

def refill_machine():
    resources.update({
        "water": 300,
        "milk": 200,
        "coffee": 100,
    })
    print("Machine refilled.")

def charge_money(drink_name):
    global bank
    bank += MENU[drink_name]["cost"]


is_On = True

while is_On:
    choice = int(input(
        "Please make a selection:\n"
        "1) Cappuccino - $5.00\n"
        "2) Latte - $5.00\n"
        "3) Espresso - $3.00\n"
        "4) Refill Machine\n"
        "5) Exit \n\n"
        "What will it be?  "
    ))

    if choice == 5:
        is_On = False
        continue

    match choice:
        case 1:
            drink_name = "cappuccino"
            process_order(MENU[drink_name]["ingredients"], drink_name)
            charge_money(drink_name)
        case 2:
            drink_name = "latte"
            process_order(MENU[drink_name]["ingredients"], drink_name)
            charge_money(drink_name)
        case 3:
            drink_name = "espresso"
            process_order(MENU[drink_name]["ingredients"], drink_name)
            charge_money(drink_name)
        case 4:
            refill_machine()
        case _:
            print("Invalid selection.")

    print(f"Current profit: ${bank}")
