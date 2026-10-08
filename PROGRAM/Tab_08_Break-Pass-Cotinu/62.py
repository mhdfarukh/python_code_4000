# 62. Write a program using break inside a nested loop while searching for a employee salary value.
employee_salary = [2000, 5000, 4000, 8000] 
searching_salary = 4000
track = False
for salary in employee_salary:
    if salary == searching_salary:
       track = True
       print("found:",salary)
       break
if track == False:
    print("not found:")