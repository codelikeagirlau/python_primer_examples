from employee_management import Employee, Manager

# Creating instances
employee01 = Employee("John Doe", 50000, 1000)
manager01 = Manager("Jane Smith", 70000, 1500, "Marketing")

employee01.display_info()
manager01.display_info()

# # Accessing protected attribute using the conventional way
# print(f"Employee's salary (protected attribute): ${employee01._salary}")

# # Attempting to access private attribute directly will raise an AttributeError

# print(f"Employee's bonus (private attribute): ${employee01.__bonus}")

# # Demonstrating name mangling
# # Accessing private attribute using name mangling
# print(f"Employee's bonus (name mangling): ${employee01._Employee__bonus}")

# # Accessing protected attribute from Manager subclass instance
# print(f"Manager's salary (protected attribute): ${manager01._salary}")

# # Attempting to access private attribute from Manager subclass directly will raise an AttributeError
# print(f"Manager's bonus (private attribute): ${manager01.__bonus}")

# # Demonstrating name mangling for private attribute in Manager subclass
# print(f"Manager's bonus (name mangling): ${manager01._Employee__bonus}")

