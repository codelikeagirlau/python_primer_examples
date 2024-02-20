# Holiday Savings Calculator

money_start = float(input("How much money do you have in your savings account?: $"))
saving_years = int(input("How many (whole) years do you have to save?: "))
interest_rate = float(input("Enter your annual savings account interest rate to two decimal places (%): ")) / 100

# Check with SMEs for correct formulas and business logic! 
money_result = money_start * ((1 + interest_rate) ** saving_years)

print(f"Total savings amount after {saving_years} years: ${money_result:.2f}")

# Check if total savings means you can go on a holiday...
cost_of_holiday = 10000
afford_holiday = money_result > cost_of_holiday
print(f"Will you be able to afford your ${cost_of_holiday} holiday ? {afford_holiday}")
