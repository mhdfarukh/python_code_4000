# 100. Write a program using continue to skip negative delivery distance values in a list and process only positives.
delivery_distance = [50, 20, 60, -90, -80, -150]
for i in delivery_distance:
    if i < 0:
        continue
    print("positives:",i)