import data
import sandwich_maker
import cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()


def main():
    # Terminal Loop
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            sandwich_maker_instance.report()
        elif choice in recipes:
            ingredients = recipes[choice]["ingredients"]
            if sandwich_maker_instance.check_resources(ingredients):
                cost = recipes[choice]["cost"]
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
                    print(f"{choice} sandwich is ready. Bon appetit!")
        else:
            print(f"Sorry, {choice} is not a valid choice. Please try again.")


if __name__ == "__main__":
    main()
