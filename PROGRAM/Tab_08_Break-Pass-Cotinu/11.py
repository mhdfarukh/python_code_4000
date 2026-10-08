# 11. Write a program using break to stop a loop as soon as a target exam result value is found.
exam_result = [10, 35, 25, 1, 24, 18]
for i in exam_result:
    if i == 1:
        break
    print(i)