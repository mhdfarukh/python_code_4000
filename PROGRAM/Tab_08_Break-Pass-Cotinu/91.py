# 91. Write a program using continue to skip negative exam result values in a list and process only positives.
exam_result = [58, 46, -78, 55, -79, -67]
for i in exam_result:
    if i < 0:
        continue
    print("positives:",i)