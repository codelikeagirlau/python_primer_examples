import math

# Accept user inputs
garment_name = input("Enter the name of your garment: ").lower()
num_garments = int(input("Enter the number of garments to make: "))
meters_per_garment = float(input("Enter the approximate meters of fabric per garment: ")) 
roll_length = float(input("Enter the length of each fabric roll (in meters): "))
roll_cost = float(input("Enter the cost of one fabric roll: $"))

# Calculate total meters required
total_meters_required = num_garments * meters_per_garment

# Calculate number of rolls required
num_rolls_required = math.ceil(total_meters_required / roll_length)

# Calculate total cost
total_cost = num_rolls_required * roll_cost


# Print the result
if num_rolls_required > 1:
    roll_string = "rolls"
else:
    roll_string = "roll"

if num_garments > 1:
    garment_string = f"{garment_name}s"
else:
    garment_string = garment_name

print(f"The total cost to make {num_garments} {garment_string} is ${total_cost:.2f} and you will need to purchase {num_rolls_required} {roll_string}.")
