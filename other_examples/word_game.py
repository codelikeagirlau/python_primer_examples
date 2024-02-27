import random

# List of words for the game
word_list = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "strawberry", "kiwi"]

# Select a random word from the list
word_to_guess = random.choice(word_list)

# Maximum number of guesses allowed
max_guesses = 10

# Display the length of the word to the user as a hint
print("The word to guess has", len(word_to_guess), "letters.")

# Initialize variables
guesses = []
remaining_guesses = max_guesses

# Main game loop
while remaining_guesses > 0:
    # Prompt the user to enter a guess
    guess = input("Enter a letter or the whole word (you have {} guesses left): ".format(remaining_guesses)).lower()

    # Check if the guess is correct
    if guess == word_to_guess:
        print("Congratulations! You guessed the word correctly:", word_to_guess)
        break
    elif len(guess) == 1 and guess.isalpha():
        if guess in guesses:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            print("Correct! '{}' is in the word.".format(guess))
        else:
            print("Sorry, '{}' is not in the word.".format(guess))
            remaining_guesses -= 1
    else:
        print("Invalid input. Please enter a single letter or the whole word.")

    # Add the guess to the list of guesses
    guesses.append(guess)

    # Check if the user has used all their guesses
    if remaining_guesses == 0:
        print("Sorry, you've run out of guesses. The word was:", word_to_guess)
        break
