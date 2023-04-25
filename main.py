MENU = {
    "espresso": {
        "ingredients": {
            "water": 100,
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
    "money": 0
}


def deduct_resources(coffee):
    if coffee == "espresso":
        resources["water"] -= 100
        resources["coffee"] -= 16
        resources["money"] += 1.5
    elif coffee == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        resources["money"] += 2.5
    elif coffee == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        resources["money"] += 3


def process_coins(coffee):
    if coffee == "espresso":
        return coin - 1.5
    elif coffee == "latte":
        return coin - 2.5
    elif coffee == "cappuccino":
        return coin - 3


def report():
    print(f'Water left :{resources["water"]}')
    print(f'Milk left :{resources["milk"]}')
    print(f'Coffee left :{resources["coffee"]}')
    print(f'Money :{resources["money"]}')


def check_resources(x, y, z):
    if x > resources["water"]:
        print("Sorry there is not enough water.")
        return False
    if y > resources["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if z > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    return True

def check_money(coin, coffee):
    if coffee == "espresso" and coin < 1.5:
        print("Sorry you don't have enough money.")
        return False
    if coffee == "cappuccino" and coin < 3:
        print("Sorry you don't have enough money.")
        return False
    if coffee == "latte" and coin < 2.5:
        print("Sorry you don't have enough money.")
        return False
    return True


while True:
    coffee = input("What would you like? (espresso/latte/cappuccino):")
    if coffee == "cappuccino":
        if not check_resources(250, 100, 24):
            continue
    elif coffee == "espresso":
        if not check_resources(250, 100, 24):
            continue
    elif coffee == "latte":
        if not check_resources(250, 100, 24):
            continue
    if coffee == "report":
        report()
        continue
    if coffee == "off":
        break
    if coffee not in MENU:
        print("Invalid choice. Please try again.")
        continue
    quarter = float(input("How many quarters?"))
    dime = float(input("How many dimes?"))
    nickel = float(input("How many nickels?"))
    pennies = float(input("How many pennies?"))
    nickel = nickel / 20
    dime = dime / 10
    quarter = quarter / 4
    pennies = pennies / 100
    coin = nickel + dime + quarter + pennies

    if coffee == "cappuccino":
        if not check_money(coin, coffee):
            break
        deduct_resources(coffee)
        coin = process_coins(coffee)
        report()
        coin = round(coin, 2)
        print(f"Here is {coin:.2f} in charge.")
        print(f"Here is {coffee} enjoy.")
    elif coffee == "espresso":
        if not check_money(coin, coffee):
            break
        deduct_resources(coffee)
        coin = process_coins(coffee)
        report()
        round(coin, 2)
        print(f"Here is {coin:.2f} in charge.")
        print(f"Here is {coffee} enjoy.")
    elif coffee == "latte":
        if not check_money(coin, coffee):
            break
        deduct_resources(coffee)
        coin = process_coins(coffee)
        report()
        round(coin, 2)
        print(f"Here is {coin:.2f} in charge.")
        print(f"Here is {coffee} enjoy.")