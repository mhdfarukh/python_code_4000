# 22. Write a program to unpack a list of employee data using a star expression to capture the rest.
employee_data = ["Srk", 55000, 50000, 35000, "network"]
name, *salary, fild = employee_data
print("Name:",name)
print("Salary:",salary)
print("Fild:",fild)