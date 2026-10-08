# 99. Write a program using a for loop to count how many user age values satisfy a condition.
user_age = [25, 68, 49, 22]
count_age = 0
for i in user_age:
    if i >= 30:
        count_age += 1
print(count_age)