# 80. Write a program using break inside a nested loop while searching for a delivery distance value.
delivery_distance = [25, 150, 49, 90]
searching_distance = 150
track = False
for distance in delivery_distance:
    if distance == searching_distance:
        track = True
        print("Found:",distance)
        break
if track == False:
    print("Not found")