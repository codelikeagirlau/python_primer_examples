name = input("What is your name? ")
location = input("Where are you located? ")
age = input("How old are you? ")

# Single inverted commas
print(f"Hi my name is {name}, and I live in {location}, and my age is {age}.")

# Triple inverted commas treat whitespace literally
print(f"""My name is {name}.
I am {age} years old.""")

# Print can take many different arguments
print(f"blah blah", len(name), len(location), 7, "hello")