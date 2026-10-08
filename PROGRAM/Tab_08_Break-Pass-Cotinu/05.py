# 05. Write a program using break to stop a loop as soon as a target temperature reading value is found.
temp_reading = [22, 15, 34, 65, 48, 85, 75]
for i in temp_reading:
    if i == 48:
        break
    print(i)