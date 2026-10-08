# 68. Write a program using break inside a nested loop while searching for a car speed value.
car_speed = [15, 20, 45, 50, 60, 80]
searching_speed = 60
track = False
for speed in car_speed:
    if speed == searching_speed:
        track = True
        print("Found:",speed)
        break
if track == False:
    print("Not found")