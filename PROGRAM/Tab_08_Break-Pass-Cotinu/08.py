# 08. Write a program using break to stop a loop as soon as a target car speed value is found.
car_speed = [25, 50, 48, 90, 100, 105, 200]
for i in car_speed:
    if i == 100:
        break
    print(i)