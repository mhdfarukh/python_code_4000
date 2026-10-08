# 25. Write a program using continue to skip invalid temperature reading values while looping through a list.
temp_reading = [22, 35, 45, 16, 18, 55]
for i in temp_reading:
    if i == 16:
        continue
    print(i)