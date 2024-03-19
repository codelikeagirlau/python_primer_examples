# Interactive App

# Initialise the dictionary
sarah_dictionary = {
    "first name": "Sarah",
    "middle name": "Louise",
    "last name": "Brown",
    "nickname": "SB",
    "occupation": "Software Engineer",
    "state": "South Australia",
    "city": "Mount Barker",
    "favourite food": "Icecream"
}

def print_dictionary(dictionary):
    print("\n---Current Dictionary:---\n")
    for key, value in dictionary.items():
        print(f"My {key} is {value}.")

# Start the application
print_dictionary(sarah_dictionary)

while True:
    action = input("\nWhat would you like to do? (add, remove, update, clear, exit): ").strip().lower()

    if action == 'add':
        key = input("Enter the key you want to add: ")
        value = input("Enter the value: ")
        sarah_dictionary[key] = value
        print(f"\nAdded {key} to the dictionary.")

    elif action == 'remove':
        key = input("Enter the key you want to remove: ")
        if key in sarah_dictionary:
            del sarah_dictionary[key]
            print(f"\nRemoved {key} from the dictionary.")
        else:
            print("\nKey not found.")

    elif action == 'update':
        key = input("Enter the key you want to update: ")
        if key in sarah_dictionary:
            value = input("Enter the new value: ")
            sarah_dictionary[key] = value
            print(f"\nUpdated {key} in the dictionary.")
        else:
            print("\nKey not found.")

    elif action == 'clear':
        sarah_dictionary.clear()
        print("\nCleared the dictionary.")

    elif action == 'exit':
        print("\nExiting the application.")
        break

    else:
        print("\nInvalid action.")

    print_dictionary(sarah_dictionary)
