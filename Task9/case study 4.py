
# Employee Payroll and Deduction Analysis

# Input employee details
emp_id = input("Enter employee ID: ")
name = input("Enter employee name: ")

basic = float(input("Enter basic salary: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime = float(input("Enter overtime pay: Rs. "))
incentives = float(input("Enter incentives: Rs. "))

# Validate salary inputs
if min(basic, allowances, overtime, incentives) < 0:
    print("Error: Salary amounts cannot be negative.")

else:
    # Calculate gross salary
    gross = basic + allowances + overtime + incentives

    # Calculate progressive deductions
    if gross <= 10000:
        deduction = 0
    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05
    else:
        deduction = (10000 * 0.05) + (
            (gross - 20000) * 0.10
        )

    # Calculate net salary
    net_salary = gross - deduction

    # Display salary statement
    print("\n===================================")
    print("       EMPLOYEE SALARY STATEMENT")
    print("===================================")
    print("Employee ID      :", emp_id)
    print("Employee Name    :", name)
    print("-----------------------------------")
    print("Basic Salary     : Rs.", round(basic, 2))
    print("Allowances       : Rs.", round(allowances, 2))
    print("Overtime Pay     : Rs.", round(overtime, 2))
    print("Incentives       : Rs.", round(incentives, 2))
    print("-----------------------------------")
    print("Gross Salary     : Rs.", round(gross, 2))
    print("Total Deductions : Rs.", round(deduction, 2))
    print("Net Salary       : Rs.", round(net_salary, 2))
    print("===================================")

