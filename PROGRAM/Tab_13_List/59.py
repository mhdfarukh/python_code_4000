# 59. Write a program to loop through a nested list of user ages using nested for loops.
user_age = [["Age:1",12, 16, 15, 13],["Age:2",17, 18, 19, 20],
            ["Age:3",21, 22, 23, 24],["Age:4",25, 26, 27, 28]
            ]
for i in user_age:
    for age in i:
        print(age)