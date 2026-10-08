# 65. Write a program using break inside a nested loop while searching for a temperature reading value.
temp_reading  = [22, 45, 50, 75, 95]
searching_reading = 95
track = False
for reading in temp_reading:
    if reading == searching_reading:
        track = True
        print("Found:",reading)
        break
if track == False:
    print("Not found:")
