# List of garments
list_of_garments = ["dress", "t-shirt", "pants", "skirt", "coat", "jumper"]

# Print the list
print(list_of_garments)

# Sort the list in alphabetical order
list_of_garments.sort()

# Print the sorted list
print(f"garments in alphabetical order: {list_of_garments}")

# Find the length of the list
list_length = len(list_of_garments)

# Print the length of the list
print(f"There are {list_length} garments available for production")

# Ask for user input
required_garment = input("What garment would you like to make: ").lower()

# Check if the input string is in the list
is_in_list = required_garment in list_of_garments

# Print the result
print(f"you can make a {required_garment}: {is_in_list}")

### 

# Garments to add
new_garments = ["hat", "scarf", "gloves"]

# Add new garments to the list using extend() method
list_of_garments.extend(new_garments)

# Print the updated list
print(list_of_garments)

####

