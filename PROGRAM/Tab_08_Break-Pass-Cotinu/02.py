# 02. Write a program using break to stop a loop as soon as a target employee salary value is found.
employee_salary = [1500, 2000, 5000, 8000, 4500]
for i in employee_salary:
    if i == 5000:
        break
    print(i)
