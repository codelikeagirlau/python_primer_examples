from kitchen_appliances import KitchenAppliance

class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=None): # default arg immutable
        super().__init__(model_number, brand)  # Using super() is more conventional 
        if coffee_menu is None:
            coffee_menu = ['latte', 'cappuccino', 'flat white'] # creates a new list each time an instance is created
        self.coffee_menu = coffee_menu
        
    def view_menu(self): # seperated view_menu into its own method - ensapsulation, SRP
        print("Here's what's on the menu:")
        for coffee in self.coffee_menu:
            print(f"- {coffee}")

    def update_menu(self, new_coffee):
        coffee_lower = new_coffee.lower()
        if coffee_lower not in self.coffee_menu:
            self.coffee_menu.append(coffee_lower)
            print(f"\n{new_coffee} has been added to the menu.")
        else:
            print(f"\n{new_coffee} is already in the menu.")

    def make_coffee(self, coffee_type):
        coffee_lower = coffee_type.lower()
        if coffee_lower in self.coffee_menu:
            print(f"\nMaking {coffee_type}...")
            print(f"\nYour {coffee_type} is ready! Enjoy!")
        else:
            print(f"\nSorry, {coffee_type} is not available.")
            self.view_menu() 
