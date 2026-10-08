# 21. Write a program to unpack a list of student records using a star expression to capture the rest.
student_records = ["Roshan", 25464, 25, 52, 55, 48, 90]
name, roll_no,  *marks = student_records
print("Name:",name)
print("Roll_No:",roll_no)
print("Course:",marks)