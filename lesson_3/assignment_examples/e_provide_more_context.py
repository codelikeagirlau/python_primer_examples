# Savings Calculator
greeting_name = input("Hey there! Welcome to the savings calculator app. What's your name? ")

saving_for = input(f"Nice to meet you {greeting_name}. What are you saving for?: ").lower()
savings_goal = float(input("How much will this cost?: $"))
money_start = float(input("How much money do you have in your savings account?: $"))
saving_years = int(input("How many (whole) years do you have to save?: "))
interest_rate = float(input("Enter your annual savings account interest rate to two decimal places (%): ")) / 100

money_result = money_start * ((1 + interest_rate) ** saving_years)

print(f"Total savings amount after {saving_years} years: ${money_result:.2f}")


# Check if the user can afford the savings goal
reach_goal = money_result >= savings_goal

# Instead of printing True or False to the console, I used an if/else statement to check whether the result of reach_goal is True, and display a print statement conditionally
if reach_goal == True:
    print(f"You can afford your ${savings_goal} {saving_for}!")
else:
	print(f"Sorry, you won't be able to afford your ${savings_goal:.2f} {saving_for}.")
