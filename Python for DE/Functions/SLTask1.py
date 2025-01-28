def calculate_salary(base_salary, bonus_percent=10, deductions=5):
    bonus = (bonus_percent / 100) * base_salary
    deduction = (deductions / 100) * base_salary
    annual_salary = base_salary + bonus - deduction
    return annual_salary

# Examples of calling the function with different arguments

# Using only the mandatory argument
salary1 = calculate_salary(50000)
print(f"Salary with default bonus and deductions: {salary1}")

# Using positional arguments
salary2 = calculate_salary(50000, 15, 8)
print(f"Salary with positional arguments: {salary2}")

# Using keyword arguments
salary3 = calculate_salary(base_salary=60000, bonus_percent=20, deductions=10)
print(f"Salary with keyword arguments: {salary3}")

# Mixing positional and keyword arguments
salary4 = calculate_salary(45000, deductions=7)
print(f"Salary with mixed arguments: {salary4}")
