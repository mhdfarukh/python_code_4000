# 71. Write a program using a for loop to find the minimum exam result value in a list.
exam_result = [85, 98, 87, 65, 70]
minimum_result = exam_result[0]
for i in exam_result:
    if i < minimum_result:
        minimum_result = i 
print(minimum_result)