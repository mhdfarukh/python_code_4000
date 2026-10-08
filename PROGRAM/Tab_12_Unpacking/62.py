# 62. Write a program to swap two employee data values using unpacking.
employee1 = [ "Roshan", 25000, "medical"]
employee2 = [ "Rahul", 35000, "Bank"]
print("Before")
print("employee1",employee1)
print("employee2",employee2)
employee1 , employee2 = employee2 ,employee1
print("After")
print("employee1",employee1)
print("employee2",employee2)