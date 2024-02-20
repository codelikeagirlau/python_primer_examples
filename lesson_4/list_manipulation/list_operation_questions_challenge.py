# CHALLENGE QUESTIONS

# Have a hand at these challenge questions. Think about what the question is
# asking, and what type the answer will evaluate to. Then check your answers
# with a print statement.

cities = ['sydney', 'melbourne', 'adelaide', 'perth', 'darwin', 'brisbane']

# eg. print(challenge_1)
challenge_1 = 'darwin' in cities[1:4]
challenge_2 = cities[2:] == cities[:2]
challenge_3 = cities[:]

# Zena's challenge
challenge_4 = cities[0:] == cities[:]

# Steph's challenge
challenge_5 = 'melbourne' in cities[:-4]

# Shreya's challenge
del cities[:-3]
challenge_6 = 'sydney' in cities[:2]

# Namira's challenge
cities = ['sydney', 'melbourne', 'adelaide', 'perth', 'darwin', 'brisbane']
cities[4:5] == ['Gold Coast', 'Canberra']
challenge_7 = cities[:1] != cities[0]

print(challenge_4)
print(challenge_5)
print(challenge_6)
print(challenge_7)