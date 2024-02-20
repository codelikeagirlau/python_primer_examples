# LIST SLICING

# Slicing is a method of selecting a specific range
# of items in a list
# eg. customers[0:7]
# or in general, list_name[start:stop]
# where start and stop are whole numbers

#			0		  1			2		  3
colours = ['blue', 'green', 'purple', 'orange']

# Are these the same?
slice_1 = colours[1:3]
slice_2 = colours[:3]
slice_3 = colours[2:]

print(slice_1)
print(slice_2)
print(slice_3)
print(colours == colours[:])

# Are these the same?
slice_4 = colours[2:]
slice_5 = colours[2:3]

print(slice_4)
print(slice_5)
print(slice_4 == slice_5)