from kitchen_appliances import SmartCoffeeMachine

coffee_machine = SmartCoffeeMachine(model_number=5000, brand="Java Jolt Elite")

action_options = [
    f"{coffee_machine.brand} {coffee_machine.model_number} options:",
    "1. View coffee menu",
    "2. Make coffee",
    "3. Add a new coffee to the menu",
    "4. Run a report",
    "5. Exit"
]

def run_coffee_machine():
    while True:
        print("\n")
        print("\n".join(action_options))
        
        choice = input("\nPlease select the number corresponding to your choice: ")
        if choice == '1':
            coffee_machine.view_menu()
        elif choice == '2':
            coffee_type = input("Which coffee would you like to make? ")
            coffee_machine.make_coffee(coffee_type)
        elif choice == '3':
            new_coffee = input("Enter the new coffee type to add to the menu: ")
            coffee_machine.update_menu(new_coffee)
        elif choice == '4':
            coffee_machine.report()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please choose a valid action.")
            
        input("\nPress any key to return to the main menu...")



run_coffee_machine()
