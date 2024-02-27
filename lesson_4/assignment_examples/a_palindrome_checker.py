# Basic Palindrome Checker - Compare lists

palindrome_word = input("Welcome to the palindrome checker! Please enter a word: ")

# At this point these two lists are the same
palindrome_word_list = list(palindrome_word)
palindrome_word_list_reversed = list(palindrome_word)

# Here is where we are reversing the second list only - sort in place
palindrome_word_list_reversed.reverse()


print(palindrome_word_list)
print(palindrome_word_list_reversed)

print(palindrome_word_list == palindrome_word_list_reversed)