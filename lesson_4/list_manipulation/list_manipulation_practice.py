# CHANGING A SPECIFIC ELEMENT OF A LIST
pets = ['ant', 'bird', 'cat', 'dog']

# replace bird with snake
pets[1] = 'snake'
print(pets)

# CHANGING MULTIPLE ELEMENTS

pets[1:3] = ['tiger', 'lion']
print(pets)

# Sublists can be replaced by a sublist of a bigger size
pets[1:3] = ['tiger', 'lion', 'jaguar']
print(pets)

# Sublists can be replaced by a sublist of a smaller size
pets[1:3] = ['bird']
print(pets)




# ADDING ELEMENTS TO A LIST
pets = ['ant', 'bird', 'cat', 'dog']
farm_animals = ['goat', 'sheep']

# 1. Concatenation with +
all_animals = pets + farm_animals
print(all_animals)

# 2. Extending with extend()
pets.extend(farm_animals)
print(pets)

# 3. Appending with append()
pets = ['ant', 'bird', 'cat', 'dog']
pets.append('emu')
pets.append(['echidna', 'platypus'])
print(pets)

# 4. Inserting with insert()
pets.insert(2, 'pig')
pets.insert(['echidna', 'platypus'])
print(pets)





# REMOVING ELEMENTS FROM A LIST
pets = ['ant', 'bird', 'cat', 'dog']
farm_animals = ['goat', 'sheep']

# 1. Removing with remove()
pets.remove('cat')
print(pets)

# 2a. Removing with pop() and an index
pets = ['ant', 'bird', 'cat', 'dog']
pet = pets.pop(2)
print(pet)
print(pets)

# 2b. Removing with pop() and no index
pets = ['ant', 'bird', 'cat', 'dog']
pet = pets.pop()
print(pet)
print(pets)

# 3a. Removing one item with delete
pets = ['ant', 'bird', 'cat', 'dog']
del pets[1]
print(pets)

# 3b. Removing multiple items with delete and a slice range
pets = ['ant', 'bird', 'cat', 'dog']
del pets[1:3]
print(pets)