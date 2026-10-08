# 68. Write a program using a for loop to find the minimum car speed value in a list.
car_speed = [120, 100, 75, 96, 82]
minimum_speed = car_speed[0]
for i in car_speed:
    if i < minimum_speed:
        minimum_speed = i 
print(minimum_speed)