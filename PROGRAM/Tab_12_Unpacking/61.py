# 61. Write a program to swap two student records values using unpacking.
student1 = ["Roshan", 85, "Pharma", 25000]
student2 = ["Rahul", 90, "Bank", 20000]
print("Before")
print(student1)
print(student2)
student1 ,student2 = student2, student1
print("After")
print("swaping:",student1)
print("swaping:",student2)
