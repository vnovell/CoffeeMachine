# Coffee Machine project
# Exercise proposed the App Brewery's '100 Days of Code - The Complete Python Pro Bootcamp'
#
# Choose between 3 hot flavours: espresso, latte or capuccino (or type 'report' for a resources report)
# Check if there's resources enough to make the order
# Insert coins
# Process coins (with refund and change, if needed)
# Makes coffee (adds money, reduces resources)

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
    "water": 300,  # 300
    "milk": 200,  # 200
    "coffee": 100,  # 100
}

coin_types = [
    {
        'name': 'quarters',
        'value': 0.25,
        'quantity': 0
    },
    {
        'name': 'dimes',
        'value': 0.10,
        'quantity': 0
    },
    {
        'name': 'nickels',
        'value': 0.05,
        'quantity': 0
    },
    {
        'name': 'pennies',
        'value': 0.01,
        'quantity': 0
    },
]

from art import logo

machine_money = float(0)
inserted_coins = float(0)
stop = False


# TODO: 1. print report
def report():
    """Returns a report of Coffee Machine's resources"""

    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print("Money:  ${:.2f}".format(machine_money))


# TODO: 2. check if resources are sufficient
def check_resources():
    """Check if there is enough resources to make the coffee"""

    global stop
    missing = []

    for items_in_resources in resources:
        if resources[items_in_resources] < MENU[choice]["ingredients"][items_in_resources]:
            missing.append(items_in_resources)

    if missing:
        stop = True
        print(f"Sorry there's not enough: {', '.join(missing)}.")

    return stop


# TODO: 3. process coins (give refund, return change)

def process_coins():
    """Process the coins: gives change, tells if coins are not enough, gives refund."""

    global inserted_coins
    print("Insert coins.")

    for coin in coin_types:

        while True:
            try:
                coin['quantity'] = input(f"How many {coin['name']}? ")
                inserted_coins += (float(coin['quantity']) * float(coin['value']))
                break
            except ValueError:
                print('Invalid option, try again.')
                continue

    print(f"Inserted coins: ${inserted_coins:.2f}")

    if inserted_coins < MENU[choice]["cost"]:
        print(f"Sorry, that's not enough money. Money refunded: ${inserted_coins:.2f}")
        inserted_coins = 0
        order()

    elif inserted_coins >= MENU[choice]["cost"]:
        if inserted_coins > MENU[choice]["cost"]:
            change = inserted_coins - MENU[choice]["cost"]
            inserted_coins = inserted_coins - change  # TODO 7. return
            print(f"Here is ${change:.2f} in change")

        print(f"Charged: ${inserted_coins:.2f}")

    return inserted_coins


# TODO: 4. order

def order():
    """Gets the order."""

    global choice
    global inserted_coins

    choice = str(input('What would you like? (espresso/latte/cappuccino)').lower())

    if choice == "report":
        report()
        order()

    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        print(f"{choice} price: ${MENU[choice]['cost']:.2f}")
        stop = check_resources()
        if stop is not True:
            make_coffee()

    else:
        print("ERROR: Invalid option")
        order()


# TODO: 5. make coffee (reduce resources, add money)

def make_coffee():
    """Makes coffee, reduces resources, adds money."""

    global choice
    global machine_money

    if "water" in MENU[choice]["ingredients"].keys():
        resources['water'] -= MENU[choice]["ingredients"]["water"]

    if "milk" in MENU[choice]["ingredients"].keys():
        resources['milk'] -= MENU[choice]["ingredients"]["milk"]

    if "coffee" in MENU[choice]["ingredients"].keys():
        resources['coffee'] -= MENU[choice]["ingredients"]["coffee"]

    machine_money += process_coins()
    print(f"Here's your {choice} Enjoy!")
    print(logo)


while stop is not True:
    order()
