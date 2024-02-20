# LIST METHODS
#
# List methods are built in Python methods which can
# operate on lists. They enable us to do higher level
# list manipulation, such as sorting or reversing
# lists, calculating the length of a list, and
# counting the number of occurrences of a specific
# value in a list.
#
# More list methods can be found on the W3Schools site
# https://www.w3schools.com/python/python_lists_methods.asp

# SORT - numbers sort ascendingly
numbers = [12, 23, -3, -3.45, 0, 195]
numbers.sort()
print(numbers)

# SORT - strings sort alphabetically
pets = ['fish', 'rabbit', 'dog', 'cat']
pets.sort()
print(pets)

# SORT - sorting only works on lists which contain one
#        type or similar types (ie. ints & floats are ok)
mixed = [12, 'bird', -3, 'cat', 0]
# mixed.sort() # this will throw an error.

# REVERSE
pets.reverse()
print(pets)

# LENGTH
print(len(pets))

# COUNT
# ie. How many of these?
ratings = [2, 3, 1, 4, 2, 4, 5, 3, 1, 5, 2]
number = 3
count = ratings.count(number)
print(f'We have {count} {number}s in our ratings')