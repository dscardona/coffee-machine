from data import MENU, resources 
profit = 0

def enough_resources(chosen_drink_ingredients):
    """Receives the ingredients of the drink selected by the user, determines whether there are enough resources to make the drink, returns boolean."""
    for item in chosen_drink_ingredients:
        if chosen_drink_ingredients[item] > resources[item]:
            print(f"\nSorry, there is not enough {item}.\n")
            return False
        return True

def process_coins():
    """Returns the total calculated fron coins inserted."""

    print("Please insert coins,")
    quarters_amt = int(input("How many quarters? ")) * .25
    dimes_amt = int(input("How many dimes? ")) * .10
    nickels_amt = int(input("How many nickels? ")) * .05
    pennies_amt = int(input("How many pennies? ")) * .01

    total_entered = round(quarters_amt + dimes_amt + nickels_amt + pennies_amt, 2)
    return total_entered

def print_report():
    print(f"\nAmount of water: {resources['water']}")
    print(f"Amount of coffee: {resources['coffee']}")
    print(f"Amount of milk: {resources['milk']}\n")

    print(f"Amount of money in register: {profit}\n")

def successful_transaction(money_received, drink_cost):
    # """Returns True if amount sufficient and False if it isnt't."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"\nHere is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("\nSorry, that isn't enough. Money refunded. \n")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕\n")


coffee_machine_on = True

while coffee_machine_on:
    choice = input("Please enter a number: \n1. Espresso \n2. Latte \n3. Cappuccino\n" )

    if choice == "off":
        coffee_machine_on = False
    elif choice == "report":
        print_report()
    else:
        if choice == "1":
            choice = "espresso"
        elif choice == "2":
            choice = "latte"
        elif choice == "3":
            choice = "cappuccino"
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = process_coins()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
