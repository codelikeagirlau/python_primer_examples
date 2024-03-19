from random_meal import random_meal

diet_type = 'omnivore'
meal = random_meal(diet_type)

print("\n")
print(f"Your {diet_type} meal is {meal['protein']} with {', '.join(meal['veg'])} and {meal['starch']}")