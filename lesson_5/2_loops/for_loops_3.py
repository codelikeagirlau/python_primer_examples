grades = [45, 50, 37, 60, 70, 47, 77, 68, 90]

# Give all students 5 extra marks
for i in range(len(grades)):
	print(f"I am grading student number {i}.")
	print(f"My current grade is {grades[i]}.")
	grades[i] += 5
	print(f"My new grade is {grades[i]}.\n")

# grade is what's inside the list, but I don't know where it is in the list
for grade in grades:
	print(grade)
	grade += 5
	print(f"{grade}\n")

# Give all fail grades 5 extra marks
for i in range(len(grades)):
	if grades[i] < 50:
		grades[i] += 5

# Put grades into buckets
for i in range(len(grades)):
	if grades[i] >= 85:
		print(f"Your grade is {grades[i]}, a HD!")
	elif grades[i] >= 75:
		print(f"Your grade is {grades[i]}, a D!")
	elif grades[i] >= 65:
		print(f"Your grade is {grades[i]}, a CR!")
	elif grades[i] >= 50:
		print(f"Your grade is {grades[i]}, a Pass!")
	else:
		print(f"Your grade is {grades[i]}, fail")

print(grades)
