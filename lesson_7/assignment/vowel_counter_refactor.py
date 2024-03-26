def vowel_counter(my_variable):
    counter = 0
    vowels = "aeiou"
    for character in my_variable:
        if character.lower() in vowels:
            counter += 1

    print(f"There are {counter} vowels in the following word/phrase: {my_variable}.")

if __name__ =="__main__":
	vowel_counter("Refactor this code")