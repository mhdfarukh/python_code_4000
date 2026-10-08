# 61. Write a program using a for loop to find the minimum student marks value in a list.
student_marks = [45, 78, 75, 85, 82, 65]
minimum_marks = student_marks [0]
for i in student_marks:
    if i < minimum_marks:
        # ye chak kare ga ki i minimum se chota hai.
        minimum_marks = i 
        # chota hai to minimum ko bataye ga  
print(minimum_marks)