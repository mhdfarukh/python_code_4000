# 22. Write a program using a for loop to calculate the total of all employee salary values in a list.
employee_salary = [25000, 20000, 15000]
total_salary = 0
# ye varibale me har number ko ak ak baar jodega.
# (0 + 25000 = 25000)
# (25000 + 20000 = 45000)
for i in employee_salary:
# ye ak ak numbers jodne ke liy aage bhajta hai or ye ghum kar i me aajata hai
     total_salary += i
print(total_salary)
    