### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###
sandwich_machine = SandwichMachine(resources)

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    ### print(f"User choice: {choice}") ###

    if choice == "off":
        print("Turning off the machine.")
        break
    elif choice == "report":
        print(f"Bread: {sandwich_machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {sandwich_machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {sandwich_machine.machine_resources['cheese']} ounce(s)")
    elif choice in ["small", "medium", "large"]:
        sandwich = recipes[choice]
        if sandwich_machine.check_resources(sandwich["ingredients"]):
            coins_inserted = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins_inserted, sandwich["cost"]):
                sandwich_machine.make_sandwich(choice, sandwich["ingredients"])
    else:
        print("Invalid choice, please try again.")