# Demonstrates the basic functionality

# note dictionary formatting
sarah_dictionary = {
    "first name": "Sarah",
    "middle name": "Louise",
    "last name": "Brown",
    "nickname": "SB",
    "occupation": "Software Engineer",
    "state": "South Australia",
    "city": "Mount Barker",
    "favourite food" : "Icecream"
}

print("\n---Original Dictionary:---\n")

#  iterates through each key-value pair in sarah_dictionary & prints a string for each 
for key, value in sarah_dictionary.items():
    print (f"My {key} is {value}.")

# this also works but it is less efficient
# for key, value in sarah_dictionary.items():
#     print (f"My {key} is  {sarah_dictionary[key]}.")

# Remove an item
sarah_dictionary.pop("nickname")

# Add a new item
sarah_dictionary["favourite colour"] = "pink"

# Update an item
sarah_dictionary["favourite food"] = "chocolate"

# Add multiple items
dictionary_additions = {"partner":"Alex","child":"Bo"}
sarah_dictionary.update(dictionary_additions)

print("\n---Modified Dictionary:---\n")

for key, value in sarah_dictionary.items():
    print (f"My {key} is {value}.")

# Clear the dictionary

sarah_dictionary.clear()

print("\n---Cleared Dictionary:---\n")

print(sarah_dictionary)