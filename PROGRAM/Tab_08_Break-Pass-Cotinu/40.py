# 40. Write a program using continue to skip invalid delivery distance values while looping through a list.
delivery_distance = [20, 40, 55, 150, 98, 88]
for i in delivery_distance:
    if i == 150:
        continue
    print(i)