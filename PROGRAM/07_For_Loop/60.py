# 60.  Write a program using a for loop to find the maximum delivery distance value in a list.
delivery_distance = [25, 20, 150, 90, 78, 80]
max_distance = 0
for i in delivery_distance:
    if i > max_distance:
        max_distance = i 
print(max_distance)