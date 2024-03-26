# Checks whether each letter in the word is a vowel
def vowel_counter(word):
    vowels = "aeiou"
    counter = 0

    for character in word.lower():
        if character in vowels:
            counter += 1
    return counter
