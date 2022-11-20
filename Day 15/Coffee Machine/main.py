MENU = {
    'espresso': {
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO Transaction check
def transaction_check(dollars_):
    global profit
    if user_choice == "latte":
        if dollars_ < 2.5:
            print("Sorry that's not enough money. Money refunded.")
        elif dollars_ > 2.5:
            change = round(dollars_ - 2.5, 2)
            print(f"Here is your ${change} change")
            profit += 2.5
            resources["water"] -= 200
            resources["milk"] -= 150
            resources["coffee"] -= 24
            print("Here is your latte. Enjoy!")
    elif user_choice == "cappuccino":
        if dollars_ < 3:
            print("Sorry that's not enough money. Money refunded.")
        elif dollars_ > 3:
            change = round(dollars_ - 3, 2)
            print(f"Here is ${change} in change")
            profit += 3
            resources["water"] -= 250
            resources["milk"] -= 100
            resources["coffee"] -= 24
            print("Here is your latte. Enjoy!")
    elif user_choice == "espresso":
        if dollars_ < 1.5:
            print("Sorry that's not enough money. Money refunded.")
        elif dollars_ > 1.5:
            change = round(dollars_ - 1.5, 2)
            print(f"Here is your ${change} change")
            profit += 1.5
            resources["water"] -= 50
            resources["coffee"] -= 18
            print("Here is your latte. Enjoy!")


# TODO: 3 Resources check
def resources_check(resources_):
    if user_choice == "espresso":
        if resources_["water"] < 50 or resources_["coffee"] < 18:
            return False
        else:
            return True
    elif user_choice == "latte":
        if resources_["water"] < 200 or resources_["coffee"] < 24 or resources_["milk"] < 150:
            return False
        else:
            return True
    elif user_choice == "cappuccino":
        if resources_["water"] < 250 or resources_["coffee"] < 24 or resources_["milk"] < 100:
            return False
        else:
            return True


# TODO:1 prompt the user by asking what you like
machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
    # TODO:2 print report
    elif user_choice == "report":
        print(f' Water: {resources["water"]}ml\n Milk: {resources["milk"]}ml\n Coffee: {resources["coffee"]}g\n '
              f'Money: ${profit}')
    elif user_choice == "latte" or "cappuccino" or "espresso":
        if resources_check(resources) is False:
            print("Sorry there is not enough water.")
        else:
            print("please insert coins")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            dollars = (quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01)
            # print(dollars)
            transaction_check(dollars)
