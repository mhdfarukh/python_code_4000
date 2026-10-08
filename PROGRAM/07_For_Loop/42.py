# 42. Write a program using a for loop to find the maximum student marks value in a list.
student_marks = [75, 45, 87, 69, 42]
max_marks = 0
for i in student_marks:
    if i > max_marks:
        max_marks = i 
print(max_marks)

