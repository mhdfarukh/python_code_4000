# 85. Write a program using continue to skip negative temperature reading values in a list and process only positives.
temp_reading = [22, -55, -456, -78, 46, 23]
for i in temp_reading:
    if i < 0:
        continue
    print("positives:",i)