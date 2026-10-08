# 74. Write a program using break inside a nested loop while searching for a water tank level value.
water_tank_level = [22, 45, 48, 79, 55, 80]
searching_level = 55
track = False
for level in water_tank_level:
    if level == searching_level:
        track = True
        print("Found:",level)
        break
if track == False:
    print("Not found")