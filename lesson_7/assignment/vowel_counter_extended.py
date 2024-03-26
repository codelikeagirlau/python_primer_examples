def vowel_counter(name):
    # Initialise the vowel count dictionary
    results = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Convert the name to lowercase to ensure case-insensitive comparison
    lower_name = name.lower()

    # Count each vowel in the name
    for letter in lower_name:
        if letter in results:
            results[letter] += 1

    # Print the results in a readable format
    for vowel, count in results.items():
        if count == 1:
            print(f"There is {count} '{vowel}' in the name {name}.")
        else:
            print(f"There are {count} '{vowel}'s in the name {name}.")

