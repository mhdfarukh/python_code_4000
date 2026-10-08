# 19. Write a program to create a nested list representing user ages organized in groups.
user_age = [[[25, 46, 12],[13,15]],
            [[19, 20],[17, 10]]
            ]
for i in user_age:
    for k in i:
        for j in k:
            print(j)