# 88. Write a program using continue to skip negative car speed values in a list and process only positives.
car_speed = [50, 60, 70, -20, -10, -89]
for i in car_speed:
    if i < 0:
        continue
    print("positives:",i)