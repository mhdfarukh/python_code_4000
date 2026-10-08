# 34. Write a program using a for loop to calculate the total of all water tank level values in a list.
water_tank_level = [500, 1000, 250, 300]
total_level = 0
for i in water_tank_level:
    total_level += i 
print(total_level)