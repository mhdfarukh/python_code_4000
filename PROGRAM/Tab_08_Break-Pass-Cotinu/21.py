# 21. Write a program using continue to skip invalid student marks values while looping through a list.
student_marks = [22, 42, 48, 56, 85, 71, 99]
for i in student_marks:
    if i == 56:
        continue
    print(i)