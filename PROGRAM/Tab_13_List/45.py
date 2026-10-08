# 45. Write a program to loop through a nested list of temperature readings using nested for loops.
trmp_readings = [[22.0, 55.1, 12.0],[10.2, 35.5, 34],
                 [75.0, 49.2, 60.0,],[44.4,55.5,66.6]
                 ]
for temp in trmp_readings:
    for reading in temp:
        print(reading)