# 88. Write a program using a for loop to count how many car speed values satisfy a condition.
car_speed = [90, 40, 50, 75, 110, 150]
count_speed = 0
for i in car_speed:
    if i >=100:
        count_speed += 1
print(count_speed)