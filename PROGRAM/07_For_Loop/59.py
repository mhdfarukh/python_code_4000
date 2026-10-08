# 59. Write a program using a for loop to find the maximum user age value in a list.
user_age = [18, 12, 20, 25, 22,]
max_age = 0
for i in user_age:
    if i > max_age:
        max_age = i
print(max_age)