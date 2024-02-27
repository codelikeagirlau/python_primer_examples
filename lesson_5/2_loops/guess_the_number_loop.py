magic_number = 55

guess = input("Guess the magic number... ")

guess_value = int(guess)

while guess_value != magic_number:
	if (guess_value < magic_number):
		print("Too low, try again!")
	elif (guess_value > magic_number):
		print("Too high, try again!")
	else:
		print("You got it!")
	guess = input("Guess the magic number... ")
	guess_value = int(guess)

print("Game over")
