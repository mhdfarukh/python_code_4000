# 43. Write a program using a for loop to find the maximum employee salary value in a list.
employee_salary = [25000, 35000, 2000]
max_salary = 0
for i in employee_salary:
    if i > max_salary:
        max_salary = i
print(max_salary)