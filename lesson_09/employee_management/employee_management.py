#OOP PRINCIPLES

# Abstraction
# Inheritance
# Encapsulation
# Polymorphism 

class Employee:
	def __init__(self, name, salary):
		self.name = name  # Public attribute
		self._salary = salary  # Protected attribute 
    
	def display_info(self):
		print(f"\nEmployee Profile:")
		print(f"- Name: {self.name}")
		print(f"- Salary: ${self._salary}")  # Accessing protected attribute
		

class Worker(Employee):
	def __init__(self, name, salary, level):
		super().__init__(name, salary)
		self.level = level

	def display_info(self):
		super().display_info()  # Call the parent's display_info method
		print(f"- Level: {self.level}")

class Manager(Employee):
	def __init__(self, name, salary, department, bonus):
		super().__init__(name, salary)
		self.department = department
		self.__bonus = bonus  # Private attribute (name mangling)
	
	def display_info(self):
		super().display_info() 
		print(f"- Department: {self.department}")
		print(f"- Bonus: ${self.__bonus}")  # Accessing private attribute
		

class CSuite(Manager):
	def __init__(self, name, salary, department, bonus, title):
		super().__init__(name, salary, department, bonus)
		self.title = title

	def display_info(self):
		super().display_info()  
		print(f"- Title: {self.title}")
