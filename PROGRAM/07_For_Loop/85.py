# 85. Write a program using a for loop to count how many temperature reading values satisfy a condition.
temp_reading = [55.2, 46.2, 89.5, 22.2 ]
count_reading = 0
for i in temp_reading:
    if i >= 47.2:
        count_reading += 1
print(count_reading)