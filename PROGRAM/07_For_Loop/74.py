# 74. Write a program using a for loop to find the minimum water tank level value in a list.
water_tank = [1500, 1000, 500, 350, 450]
minimum_level = water_tank[0]
for i in water_tank:
    if i < minimum_level:
        minimum_level = i 
print(minimum_level)