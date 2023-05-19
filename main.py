from data import MENU, resources 

money_in_machine = 0

# TODO: Function to determine if transaction was successful, Function to return change, Function to "Make coffee": deduct resources, add money to money counter and print success.

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
    pennies_amt = int(input("How many pennies?")) * .01

    total_entered = round(quarters_amt + dimes_amt + nickels_amt + pennies_amt, 2)
    return total_entered



choice = input("Please enter a number: \n1. Espresso \n2. Latte \n3. Cappuccino\n" )

if choice == "1":
    drink_to_make = "espresso"
elif choice == "2":
    drink_to_make = "latte"
elif choice == "3":
    drink_to_make = "cappuccino"
else:
    print("That's not an option")


if enough_resources(drink_to_make):
    total_entered = count_coins()



 


#TODO: Another function? If transaction successful (zero not returned from coins inserted check function), and there are enough resources (resources function returns True) , deduct resources from the machine and tell the user: “Here is your {drink_of_choice}. Enjoy!” Print change being returned.

# TODO: Keep prompting user for choice, while loop with off flag or recursion (new "coffee-machine-on "function)

# TODO: End execution with word "off" 

# TODO: Print report with current Water, Milk, Coffee and Money values, with word "report". Prompt again.


