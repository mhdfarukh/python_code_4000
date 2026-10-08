# 31. Write a program using continue to skip invalid exam result values while looping through a list.
exam_result = [45, 49, 55, 98, 75, 85]
for i in exam_result:
    if i == 49:
        continue
    print(i)