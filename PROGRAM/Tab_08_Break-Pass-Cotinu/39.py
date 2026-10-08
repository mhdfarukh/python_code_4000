# 39. Write a program using continue to skip invalid user age values while looping through a list.
user_age = [12, 15, 18, 25, 35, 99, 28]
for i in user_age:
    if i == 99:
        continue
    print(i)