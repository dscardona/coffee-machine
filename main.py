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

    # return True
    return print("True")


choice = input("Please enter a number: \n1. Espresso \n2. Latte \n3. Cappuccino\n" )

if choice == "1":
    drink_to_make = "espresso"
elif choice == "2":
    drink_to_make = "latte"
elif choice == "3":
    drink_to_make = "cappuccino"
else:
    print("That's not an option")

enough_resources(drink_to_make)


# TODO: Prompt user to insert coins, how many quarters, dimes, nickels, and pennies.
        # TODO:Check if there's enough Water, Milk, and Coffee to make user's selected drink. Let user know if resources arent sufficient "Sorry, there's not enough water"
        # Function to determine if there are enough resources, returns boolean. returns true or false.

        #TODO: If there are enough resources, prompt user to insert coins. Calculate value of the coins inserted.
            # TODO: Check if user didn't insert enough coins: “Sorry that's not enough money. Money refunded.” Prompt again. return 0.
 
            #TODO: If enough coins, returns amount inserted.

            #TODO: Function to return negative value if too much money was inserted. 
        

        #TODO: Another function? If transaction successful (zero not returned from coins inserted check function), and there are enough resources (resources function returns True) , deduct resources from the machine and tell the user: “Here is your {drink_of_choice}. Enjoy!” Print change being returned.

    # TODO: Keep prompting user for choice, while loop with off flag or recursion (new "coffee-machine-on "function)

# TODO: End execution with word "off" 

# TODO: Print report with current Water, Milk, Coffee and Money values, with word "report". Prompt again.


