from data import meal_components
import random

def random_meal(diet_type):
	protein = random.choice(meal_components['protein'][diet_type])
	starch = random.choice(meal_components['starch'])
	veg = random.sample(meal_components['veg'], 3)

	return {
		'protein': protein,
		'starch' : starch,
		'veg': veg
	}


