# 81. Write a program using a for loop to count how many student marks values satisfy a condition.
student_marks = [48, 43, 55, 57, 60, 78, 85]
count_marks = 0
for i in student_marks:
    if i >= 50:
        count_marks += 1 
print(count_marks)
