# 91. Write a program using a for loop to count how many exam result values satisfy a condition.
exam_result = [95, 87, 59, 36, 61, 44]
count_result = 0
for i in exam_result:
    if i >= 65:
        count_result += 1
print(count_result)