palindrome_word = input("Welcome to the palindrome checker! Please enter a word: ")

# Convert the input word to a list of characters
palindrome_word_list = list(palindrome_word)

# Create a reversed version of the list using slicing
# Slicing with [::-1] reverses the list by starting from the end (index -1) and moving backwards to the beginning
palindrome_word_list_reversed = palindrome_word_list[::-1]

print(palindrome_word_list)
print(palindrome_word_list_reversed)

print(palindrome_word_list == palindrome_word_list_reversed)
