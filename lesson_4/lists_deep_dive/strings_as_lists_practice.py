company = 'Code Like A Girl'

# SINGLE LETTER
letter = company[5]
# print(letter)

# SLICING
slice_1 = company[5:]
# print(slice_1)

# FINDING
position = company.find('Like')
print(position)
#				5			9
print(company[5:9])
print(company[position:position+4])

# REPLACING
new_company = company.replace('Code', 'Throw')
# print(new_company)