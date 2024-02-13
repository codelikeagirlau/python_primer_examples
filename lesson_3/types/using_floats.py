my_number = 3
print(type(my_number))

my_float = float(my_number)
print(my_float)

# HOW TO USE: https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,number%20with%20two%20decimal%20places.
# 
# str.format(number)
formatted_float = "{:.5f}".format(my_float)
print(formatted_float)