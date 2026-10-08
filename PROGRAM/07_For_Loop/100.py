# 100. Write a program using a for loop to count how many delivery distance values satisfy a condition.
delivery_distance = [50, 75, 20, 40, 36]
count_distance = 0
for i in delivery_distance:
    if i >= 40:
        count_distance += 1
print(count_distance)