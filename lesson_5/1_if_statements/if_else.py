#temperature = input("What's the temperature like outside? ")
#temperature = float(temperature)

temperature = 25

if temperature < 17:				# temperature is less than 17
    print("Wear a scarf!")
elif temperature < 25:				# we know temperature is >= 17 from the first statement not running, so it will be 17 <= temp < 25
    print("Bring a light jacket!")
elif temperature < 30:
    print("Bring a hat just in case!")
else:                               # for everything else
# elif temperature >= 25:			# we know temperature is >= 25 from the first two statements not running, so it will be >= 25
    print("Put on some sunscreen, and maybe bring a hat.")