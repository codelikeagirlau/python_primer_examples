example_string = "I have a message for you"

print(example_string)

uppercase_string = example_string.upper()

print(uppercase_string)

lowercase_string = example_string.lower()

print(lowercase_string)

length_of_string = len(example_string)

print(length_of_string)

# print("The message has a length of " + length_of_string + "characters") # this should not work
print(f"The message has a length of {length_of_string} characters")