user_monthly_salary = int(input("Enter your monthly income: "))
user_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = user_monthly_salary - user_monthly_expenses
annual_savings = monthly_savings * 12 * 0.05
projected_savings = int(monthly_savings * 12 + annual_savings)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")

