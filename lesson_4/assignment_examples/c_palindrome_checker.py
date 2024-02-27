# Palindrome Checker - check words OR phrases

# Prompt the user to enter a word or a phrase for palindrome checking, and convert the input to lowercase (otherwise it's not a palindrome match!)
palindrome_input = input("Welcome to the palindrome checker! Please enter a word or a phrase: ").lower()

# Remove spaces from the input palindrome word and convert it to a list of characters
characters_without_spaces = list(palindrome_input.replace(" ", ""))

# Join the characters without spaces back into a string
palindrome_input_without_spaces = "".join(characters_without_spaces)

# Reverse the characters without spaces in-place
characters_without_spaces.reverse()

# Join the reversed characters back into a string to get the reversed palindrome word
reversed_palindrome = "".join(characters_without_spaces)

# Print the original word/phrase without spaces and its reversed version
print(f"{palindrome_input_without_spaces} backwards is {reversed_palindrome}")


if palindrome_input_without_spaces == reversed_palindrome:
    print (f"{palindrome_input} is a palindrome.")

else:
    print (f"{palindrome_input} is not a palindrome.")