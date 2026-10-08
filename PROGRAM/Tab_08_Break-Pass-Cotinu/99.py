# 99. Write a program using continue to skip negative user age values in a list and process only positives.
user_age = [-12, 20, -17, 23, 55]
for i in user_age:
    if i < 0:
        continue
    print("positives:",i)