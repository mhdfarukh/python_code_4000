# 82. Write a program using continue to skip negative employee salary values in a list and process only positives.
employee_salary = [-200, -156, 2500, 5000, 8000, -4589]
for i in employee_salary:
    if i < 0:
        continue
    print("Positiver number",i)