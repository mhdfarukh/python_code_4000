# 01. Write a program using break to stop a loop as soon as a target student marks value is found.
student_marks = [54, 62, 23, 27, 85, 66]
for i in student_marks:
    if i == 85:
        break
    print(i)