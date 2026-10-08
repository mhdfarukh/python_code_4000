# 46. Write a program using a for loop to find the maximum temperature reading value in a list.
temerature_reading = [25.2, 15.2, 35.4, 13.5,]
max_reading = 0
for i in temerature_reading:
    if i > max_reading:
        max_reading = i
print(max_reading)