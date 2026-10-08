# 62. Write a program using a for loop to find the minimum employee salary value in a list.
employee_salary = [4800, 35000, 30000, 2500, 20000]
minimum_salary = employee_salary[0]
for i in employee_salary:
    if i < minimum_salary:
        minimum_salary = i 
print(minimum_salary)