# Basic Palindrome Checker - Compare Strings

palindrome_word = input("Welcome to the palindrome checker! Please enter a word: ")

# At this point these two lists are the same
palindrome_word_list = list(palindrome_word)
palindrome_word_list_reversed = list(palindrome_word)

# Here is where we are reversing the second list only - sort in place
palindrome_word_list_reversed.reverse()

# Convert the lists back to strings for comparison
palindrome_word_reversed = ''.join(palindrome_word_list_reversed)

print(f"Palindrome word to check: {palindrome_word}")
print(f"Palindrome word reversed: {palindrome_word_reversed}")

print(palindrome_word == palindrome_word_reversed)