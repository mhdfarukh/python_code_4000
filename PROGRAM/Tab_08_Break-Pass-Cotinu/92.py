# 92. Write a program using continue to skip negative social media likes count values in a list and process only positives.
social_media_likes = [12, 15, -46, -44, -72, 55, 19]
for i in social_media_likes:
    if i < 0:
        continue
    print("positives:",i)