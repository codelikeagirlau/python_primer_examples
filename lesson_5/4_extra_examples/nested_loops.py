# A list of lists! This list contains 10 lists, each containing
# ten numbers. I've formatted it like this so it's easy to read,
# and because visualising it like a grid can be helpful!

# We will use it to demonstrate why you may want to
# have a loop inside a loop.
my_list = [
	[0,   1,  2,  3,  4,  5,  6,  7,  8,  9],
	[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
	[20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
	[30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
	[40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
	[50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
	[60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
	[70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
	[80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
	[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]

# Just to get us comfortable with what's going on, let's print
# some stuff!

# my_list[0] is a list, containing the numbers 0-9
print(my_list[0])

# my_list[9] is a list, containing the numbers 90-99
print(my_list[9])

# Each item here is a list. This will print all of the lists that
# my_list contains.
for item in my_list:
	print(item)

# Here's where the nested loop comes in... what if I want to print
# every number in this
for item in my_list:
	# remember item is a list
	for number in item:
		print(number)

# Why don't you try using indexes now? It is a little tricky but I
# think you can do it. :) I'll get you started:

# We can index in on two levels :O
# First, my_list[0] returns a list, as we know. Then the second index
# goes into that list!
print(my_list[0][0])

# Some more examples...
print(my_list[5][4])
print(my_list[3][7])

# you may be sensing a theme now about how to do this :)
