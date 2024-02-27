# define fabric options
fabric_options = ["cotton", "linen", "denim"]

# define garment options
cotton_garments = ["tshirt", "shorts"]
linen_garments = ["dress", "pants", "skirt"]
denim_garments = ["jeans", "vest", "jacket"]

print("Welcome to the pattern finder, here are the fabric options:")


for i, fabric in fabric_options:
	print(fabric)

# create infinite loop to prompt user to choose fabric and garment until match is made	
while True:
	fabric_choice = input("please enter your fabric choice: ")

	#check if fabric is in list
	if fabric_choice not in fabric_options:
		print("invalid fabric choice")
		continue

	garment_choice = input("please enter the garment you want to make: ").lower()

	# render a conditional message based on the garmet/fabric match
	if fabric_choice == "cotton" and garment_choice not in cotton_garments: 
		print("you can't make that with cotton fabric")
		continue
	elif fabric_choice == "linen" and garment_choice not in linen_garments:
		print(f"you can't make that with {fabric_choice} fabric")
		continue
	elif fabric_choice == "denim" and garment_choice not in denim_garments:
		print(f"you can't make that with {fabric_choice} fabric")
		continue
	else:
		print(f"Great choice! you are making a {fabric_choice} {garment_choice}. You can find the pattern here: https://patterns.com/{fabric_choice}/{garment_choice} ")
	break

