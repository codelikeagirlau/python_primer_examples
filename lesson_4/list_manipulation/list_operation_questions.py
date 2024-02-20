# Using this list, let's answer some questions

#			0			1			2			3		4			5
#			-6			-5			-4			-3		-2			-1
cities = ['sydney', 'melbourne', 'adelaide', 'perth', 'darwin', 'brisbane']

# What will these statements evaluate to?

# Check your answers with a print statement
# eg. print(question_1)
question_1 = 'hobart' in cities
question_2 = 'adelaide' in cities
question_3 = 'melbourne' not in cities

question_4 = cities[0]
question_5 = cities[-4]

question_6 = cities[1:3]

question_7 = 'hobart' in cities and 'perth' not in cities
question_8 = 'sydney' in cities == cities[-5]
question_9 = cities[1:7] # this doesn't throw an error!
question_10 = cities[-5] + cities[5] # weird string stuff

print(question_1)
print(question_2)
print(question_3)
print(question_4)
print(question_5)
print(question_6)
print(question_7)
print(question_8)
print(question_9)
print(question_10)