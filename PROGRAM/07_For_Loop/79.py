# 79. Write a program using a for loop to find the minimum user age value in a list.
user_age = [25, 24, 12, 26, 19]
minimum_age = user_age[0]
for i in user_age:
    if i < minimum_age:
        minimum_age = i
print(minimum_age)