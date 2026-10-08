# 34. Write a program using continue to skip invalid water tank level values while looping through a list.
weter_tank = [120, 500, 1500, 1000, 245, 3500]
for i in weter_tank:
    if i == 245:
        continue
    print(i)