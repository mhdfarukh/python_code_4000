# 82. Write a program using a for loop to count how many employee salary values satisfy a condition.
employee_salary = [8000, 6000, 4000, 1000 ,7000]
count_salary = 0
for i in employee_salary:
    if i >= 5000:
        count_salary += 1
print(count_salary)