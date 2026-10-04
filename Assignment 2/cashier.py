class Cashier:
    def __init__(self):
        pass

    def ask_input(self, prompt):
        """Keep asking for the coins until user enters a whole number that isn't negative, avoiding crashes"""
        while True:
            res = input(prompt)
            try:
                count = int(res)
            except ValueError:
                print("Please enter a whole number.")
                continue
            if count < 0:
                print("You cannot enter a negative number of coins.")
                continue
            return count

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = self.ask_input("How many large dollars?: ") * 1.00
        half_dollars = self.ask_input("How many half dollars?: ") * 0.5
        quarters = self.ask_input("How many quarters?: ") * 0.25
        nickels = self.ask_input("How many nickels?: ") * 0.05

        total = large_dollars + half_dollars + quarters + nickels
        return total

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
