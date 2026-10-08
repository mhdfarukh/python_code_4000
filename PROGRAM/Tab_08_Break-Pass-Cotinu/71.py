# 71. Write a program using break inside a nested loop while searching for a exam result value.
exam_result = [25, 45, 46, 75, 85]
searching_result = 90
track = False
for result in exam_result:
    if result == searching_result:
        track = True
        print("Found:",result)
        break
if track == False:
    print("Not found:")
