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
        for key, value in ingredients.items():
            if self.machine_resources[key] < value:
                print(f"Sorry there is not enough {key}.")
                return False
        return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("How many large dollars?: ")) * 1.00
        half_dollars =  int(input("How many half dollars?: ")) * 0.5
        quarters = int(input("How many quarters?: ")) * 0.25
        nickels = int(input("How many nickels?: ")) * 0.05

        sum = large_dollars + half_dollars + quarters + nickels
        return sum



    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if cost > coins:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = coins - cost

            print(f"Here is ${change:.2f} in change.")
            return True



    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for key,value in order_ingredients.items():
            self.machine_resources [key] -= value



### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

### report helper ###

def report(self):
    print(f"Bread: {self.machine_resources['bread']} slice(s)")
    print(f"Ham: {self.machine_resources['ham']} slice(s)")
    print(f"Cheese: {self.machine_resources['cheese']} pound(s)")

# Terminal Loop

while True:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        report(machine)
    elif choice in recipes:
        ingredients = recipes[choice]["ingredients"]
        if machine.check_resources(ingredients):
            cost = recipes[choice]["cost"]
            coins = machine.process_coins()
            if machine.transaction_result(coins, cost):
                machine.make_sandwich(choice, ingredients)
                print(f"{choice} sandwich is ready. Bon appetit!")
    elif choice not in recipes:
        print(f"Sorry, {choice} is not a valid choice. Please try again.")

