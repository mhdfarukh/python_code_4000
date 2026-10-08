# 65.  Write a program using a for loop to find the minimum temperature reading value in a list.
temperature_reading = [50.2, 25.0, 56.0, 45.5]
minimum_reading = temperature_reading[0]
for i in temperature_reading:
    if i < minimum_reading:
        minimum_reading = i 
print(minimum_reading)