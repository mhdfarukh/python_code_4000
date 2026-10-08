# 32. Write a program using continue to skip invalid social media likes count values while looping through a list.
social_media_like = [25, 34, 37, 19, 16, 13,]
for i in social_media_like:
    if i == 16:
        continue
    print(i)