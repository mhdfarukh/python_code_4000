# 80. Write a program using a for loop to find the minimum delivery distance value in a list.
delivery_distance = [98, 95, 85, 25, 48, 49]
minimum_distance = delivery_distance[0]
for i in delivery_distance:
    if i < minimum_distance:
        minimum_distance = i
print(minimum_distance)