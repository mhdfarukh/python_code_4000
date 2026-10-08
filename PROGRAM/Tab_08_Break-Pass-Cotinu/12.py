# 12. Write a program using break to stop a loop as soon as a target social media likes count value is found.
midea_likes = [25, 50, 100, 48, 99, 75]
for i in midea_likes:
    if i == 99:
        break
    print(i)