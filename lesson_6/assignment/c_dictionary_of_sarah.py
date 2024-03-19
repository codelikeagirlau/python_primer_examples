# Dictionary using a sub-dictionary structure with nested dictionaries

sarah_dictionary = {
    "name": {
        "first": "Sarah",
        "middle": "Louise",
        "last": "Brown",
        "nickname": "SB"
    },
    "location": {
        "state": "South Australia",
        "city": "Mount Barker"
    },
    "profile": {
        "occupation": "Software Engineer",
        "favourite food": "Icecream"
    }
}


# Iterate through each key-value pair in sarah_dictionary & prints a string for each
for key, nested_dict in sarah_dictionary.items():
    print(f"My {key}:")
    for sub_key, value in nested_dict.items():
        print(f"  {sub_key.capitalize()} is {value}.")

# natural_sentence = (
#     f"My name is {sarah_dictionary['name']['first']} {sarah_dictionary['name']['middle']} {sarah_dictionary['name']['last']}, "
#     f"but you can call me {sarah_dictionary['name']['nickname']}. "
#     f"I live in {sarah_dictionary['location']['city']}, which is in the state of {sarah_dictionary['location']['state']}. "
#     f"I work as a {sarah_dictionary['profile']['occupation']} and my favourite food is {sarah_dictionary['profile']['favourite food']}."
# )

# print(natural_sentence)