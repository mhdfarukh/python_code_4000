# 81. Write a program using continue to skip negative student marks values in a list and process only positives.
student_marks = [25, 58, -25, 56, -55, 99, -15]
for i in student_marks:
    if i < 0:
        continue
    print(i)
