# 21. Write a program using a for loop to calculate the total of all student marks values in a list.
student_marks = [75, 54, 82, 98, 86, 65]
total_marks = 0
for i in student_marks:
    total_marks += i
print(f"The total of all student marks: {total_marks}")