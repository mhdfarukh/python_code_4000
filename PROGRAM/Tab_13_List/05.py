# 05. Write a program to create a nested list representing temperature readings organized in groups.
temp_readings = [[21, 22, 23],[42, 52, 63]]
for i in temp_readings:
    for j in i:
        print(j)