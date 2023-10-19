from menu import MENU, resources
from art import LOGO


def report():
    for i in resources:
        print(f"{i.upper()}: {resources[i]}")


def calculate_coins(penny, nickel, dime, quarter):
    penny_total = 1 * penny / 100
    nickel_total = 5 * nickel / 100
    dime_total = 10 * dime / 100
    quarter_total = 25 * quarter / 100
    return penny_total + nickel_total + dime_total + quarter_total


def make_coffee(user_coffee):
    coffee = MENU.get(user_coffee)
    ingredients = coffee.get("ingredients")
    for i in ingredients:
        if resources[i] < ingredients[i]:
            print(f"Sorry, don't have enough {i}")
            return False
    cost = coffee.get("cost")
    print(f"Cost: {cost}")
    coins = take_cash()
    user_amount = calculate_coins(coins[0], coins[1], coins[2], coins[3])
    if user_amount >= cost:
        resources["water"] -= ingredients["water"]
        resources["coffee"] -= ingredients["coffee"]
        if user_coffee != "espresso":
            resources["milk"] -= ingredients["milk"]
        resources["money"] += cost
        calculate_money(user_amount, cost)
        print(f"Enjoy your {user_coffee}")
    else:
        print("Sorry, that's not enough money. Money refunded")
    return user_amount


def take_cash():
    print("Please insert coins: ")
    coins = ["quarters", "dimes", "nickles", "pennies"]
    user_coins = []
    for i in coins:
        user_coins.append(int(input(f'How many {i}: ')))
    return user_coins


def calculate_money(user_amount, cost):
    refund = user_amount - cost
    print(f"Here is {format(refund, '.2f')} in change. ")


def coffee_machine():
    print(LOGO)
    while True:
        user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_coffee == 'report':
            report()
        elif user_coffee in ['latte', 'espresso', 'cappuccino']:
            make_coffee(user_coffee)
        else:
            print("Invalid coffee")


coffee_machine()
