# 22. Write a program using continue to skip invalid employee salary values while looping through a list.
employee_salary = [2000, 25000, 32000, 5000, 1500]
for i in employee_salary:
    if i == 5000:
        continue
    print(i)