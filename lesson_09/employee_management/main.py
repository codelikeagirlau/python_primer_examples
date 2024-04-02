from employee_management import Worker, Manager, CSuite

employee01 = Worker("Sarah", 70000, 1)
employee02 = Manager("Bethany", 90000, "Marketing", 1000)
employee03 = CSuite("Jo", 100000, "Marketing", 4000, "CMO")

employee01.display_info()
employee02.display_info()
employee03.display_info()

print(f"\n--- Directly Accessing protected and private attributes via name mangling; proceed with caution...")
print(f"\n- {employee02.name}'s salary (protected attribute): ${employee01._salary}")
print(f"- {employee02.name}'s bonus (private attribute): ${employee02._Manager__bonus}")

