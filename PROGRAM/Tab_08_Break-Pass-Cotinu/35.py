# 35. Write a program using continue to skip invalid traffic signal timer values while looping through a list.
traffic_timer = [30, 35, 25, 16, 18, 19, 17]
for i in traffic_timer:
    if i == 35:
        continue
    print(i)