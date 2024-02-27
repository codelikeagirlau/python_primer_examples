magic_number = 55

guess = input("Guess the magic number... ")

guess_value = int(guess)

if (guess_value < magic_number):
        print("Too low, try again!")
elif (guess_value > magic_number):
        print("Too high, try again!")
else:
        print("You got it!")

print("Game over")


# A note on optimising the algorithm
# if (guess_value == magic_number)
# 	print("You got it!")
# elif (guess_value <= magic_number):
# 	print("Too low, try again!")
# else:
# 	print("Too high, try again!")
