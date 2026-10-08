# 51. Write a program using a for loop to find the maximum exam result value in a list.
exam_result = [82, 75, 90, 65, 54, 40]
max_result = 0
for i in exam_result:
    if i > max_result:
        max_result = i
print(max_result)
