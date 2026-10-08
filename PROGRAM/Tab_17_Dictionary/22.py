# 22. Write a program to create a dictionary of employee data using curly braces with key-value pairs.
employee_data = {"Employee Name:": "Rohan",
                 "Employee Id:": 15200,
                 "Salary:": 25000,
                 "Department:": "IT"
                 }
for key , value in employee_data.items():
    print(key , value)