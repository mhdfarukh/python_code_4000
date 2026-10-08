# 82. Write a program to unpack nested lists of employee data into separate variables.
Employee_data = ["Vivek",52000, "gormant", "Day"],["Akash","IT",30000, "ID12456"]
(name1, salary1, job1, shift1),(name2, job2, salary2, UserID2) = Employee_data

print("EMPLOYEE =1:")
print("Name1:",name1)
print("SALARY1:",salary1)
print("JOB1:",job1)
print("SHIFT1:",shift1)

print("EMPLOYEE = 2:")
print("Name2:",name2)
print("JOB2:",job2)
print("SALARY2:",salary2)
print("USER_ID2:",UserID2)