# 42. Write a program to loop through a nested list of employee data using nested for loops.
Employee_data = [["Iliyes", 18000, "Madicin"],["Rahul", 35000, "Bank"],
                 ["Shivam", 15000, "DRM"],["Dlieep", 35000, "Raliway"]
                 ]
for Employee in Employee_data:
    Name = Employee [0]
    Salary = Employee [1]
    Job = Employee [2]
    print(Name, Salary, Job)