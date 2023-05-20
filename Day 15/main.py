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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(coffee):
    """Checks if there are sufficient resources for the item provided to be made"""

    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False

    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False

    elif choice != "espresso":
        if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True

    else:
        return True


def get_coins(coffee):
    """Prompts the user to insert coins and calculates the total. Returns the change if any. Returns all amount if cost of coffee is greater."""

    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))

    total_money = round(
        0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies, 2
    )
    print(total_money)
    if total_money > MENU[coffee]["cost"]:
        change = total_money - MENU[coffee]["cost"]
        print(f"Here's your change ${round(change,2)}")
        return int(MENU[coffee]["cost"])
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def resources_used(coffee):
    """Subtracts the resources used for making the coffee from the main resources list."""

    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    if coffee != "espresso":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]


import os

os.system("cls")

is_on = True
money_made = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money_made}"
        )

    elif choice in MENU:
        is_available = check_resources(choice)
        if is_available:
            money_made += get_coins(choice)
            resources_used(choice)
            print(f"Here is your {choice}. Enjoy!")
