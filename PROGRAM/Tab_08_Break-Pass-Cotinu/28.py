# 28. Write a program using continue to skip invalid car speed values while looping through a list.
car_speed = [20, 30, 40, 50, 120, 200]
for i in car_speed:
    if i == 120:
        continue
    print(i)