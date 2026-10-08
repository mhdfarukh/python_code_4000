# 12. Write a program to create a nested list representing social media followers organized in groups.
social_media_followers = [[[85, 45, 46,],[98, 34, 25]],
                          [[100, 75, 96],[13, 29, 59]]
                          ]
for i in social_media_followers:
    for j in i:
        for k in j:
            print(k)