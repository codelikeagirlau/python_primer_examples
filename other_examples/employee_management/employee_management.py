# OOP Principles
## Abstraction
## Inheritence
## Encapsulation
## Polymorphism


class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name  # Public attribute
        self._salary = salary  # Protected attribute 
        self.__bonus = bonus  # Private attribute (name mangling)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self._salary}")  # Accessing protected attribute
        print(f"Bonus: ${self.__bonus}")  # Accessing protected attribute

class Manager(Employee):  # Manager inherits from Employee
    def __init__(self, name, salary, bonus, department):
        super().__init__(name, salary, bonus)
        self.department = department

    def display_info(self):  # Polymorphism: override display_info method from parent
        super().display_info()  # Call the parent's display_info method
        print(f"Department: {self.department}")
        print(f"Manager's Salary (protected attribute): ${self._salary}")  # Accessing protected attr
        print(f"Manager's Bonus (protected attribute): ${self.Employee.__bonus}")  # Accessing protected attribute
        
		