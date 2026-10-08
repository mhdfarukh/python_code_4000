# 48. Write a program using a for loop to find the maximum car speed value in a list.
car_speed = [54, 95, 120, 99, 100]
max_speed = 0
for i in car_speed:
    if i > max_speed:
        max_speed = i 
print(max_speed)