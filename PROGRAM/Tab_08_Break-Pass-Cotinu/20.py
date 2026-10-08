# 20. Write a program using break to stop a loop as soon as a target delivery distance value is found.
delivery_distance = [20, 50, 45, 80, 94, 100, 150, 350]
for i in delivery_distance:
    if i == 150:
        break
    print(i)