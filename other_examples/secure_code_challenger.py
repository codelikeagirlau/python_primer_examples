import random
import os 

print("Secure Code Challenger")

num_of_guesses = 0
secure_code = int(input("set your 4-digit secure code:"))

while True:
  code_guess = random.randint(0000,9999)
  print("code tried:", code_guess)
  os.system("clear")
  num_of_guesses = num_of_guesses + 1
  if code_guess == secure_code:
    print("your code:", code_guess)
    print(num_of_guesses, "passwords guessed")
    break

