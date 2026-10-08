# 54. Write a program using a for loop to find the maximum water tank level value in a list.
water_tank = [500, 350, 500, 450]
max_level = 0
for i in water_tank:
    if i > max_level:
        max_level = i 
print(max_level)
