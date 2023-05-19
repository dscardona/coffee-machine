from data import MENU, resources 

def enough_resources(chosen_drink):
    """Receives the drink selected by the user, determines whether there are enough resources to make the drink, returns boolean."""
    recipe = MENU[chosen_drink]["ingredients"]

    needed_water = recipe["water"]
    needed_coffee = recipe["coffee"]
    needed_milk = 0
    if "milk" in recipe:
        needed_milk = recipe["milk"]

    if needed_water > resources["water"]:
        print("Sorry, there's not enough water")
        return False
    if needed_coffee > resources["coffee"]:
        print("Sorry, there's not enough coffee")
        return False
    if needed_milk > resources["milk"]:
        print("Sorry, there isn'e enough milk")
        return False

    return True

def count_coins():
    """Gets number/kind of coins entered, returns amount entered"""

    print("Please insert coins,")
    quarters_amt = int(input("How many quarters? ")) * .25
    dimes_amt = int(input("How many dimes? ")) * .10
    nickels_amt = int(input("How many nickels? ")) * .05
    pennies_amt = int(input("How many pennies? ")) * .01

    total_entered = round(quarters_amt + dimes_amt + nickels_amt + pennies_amt, 2)
    return total_entered

def print_report():
    print(f"\nAmount of water: {resources['water']}")
    print(f"\nAmount of coffee: {resources['coffee']}")
    print(f"\nAmount of milk: {resources['milk']}\n")

    print(f"Amont of money in register: {total_in_machine}\n")

money_received = 0
change_rendered = 0
total_in_machine = money_received - change_rendered
coffee_machine_on = True


while coffee_machine_on:
    choice = input("Please enter a number: \n1. Espresso \n2. Latte \n3. Cappuccino\n" )

    drink_to_make = ""
    if choice == "1":
        drink_to_make = "espresso"
    elif choice == "2":
        drink_to_make = "latte"
    elif choice == "3":
        drink_to_make = "cappuccino"
    if choice == "report":
        print_report()
    if choice == "off":
        coffee_machine_on = False
    else:
        print("That's not an option")

    total_entered = 0
    if enough_resources(drink_to_make):
        total_entered = count_coins()

    cost = MENU[drink_to_make]["cost"] 
    if cost == total_entered:
        money_received += total_entered
        print(f"Here's your {drink_to_make}. Enjoy!")
        resources["water"] -= MENU[drink_to_make]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink_to_make]["ingredients"]["coffee"]
        if "milk" in MENU[drink_to_make]["ingredients"]:
            resources["milk"] -= MENU[drink_to_make]["ingredients"]["milk"]

    elif cost < total_entered:
        money_received += cost
        change = abs(cost - total_entered)
        print(f"Here's your change: ${change}")
        change_rendered += change
        print(f"Here's your {drink_to_make}. Enjoy!")
        resources["water"] -= MENU[drink_to_make]["ingredients"]["water"]
        resources["coffee"] -= MENU[drink_to_make]["ingredients"]["coffee"]
        if "milk" in MENU[drink_to_make]["ingredients"]:
            resources["milk"] -= MENU[drink_to_make]["ingredients"]["milk"]

    else:
        print(f"Sorry, that's not enough. Here's your refund: ${total_entered}")


print(resources)


#TODO: If a resource runs out, only the message stating so should be displayed. The count_coins function shouldn't be executed

#TODO: When "report" or "off" are input, the enough_resources and count_counts functions should be ignored.