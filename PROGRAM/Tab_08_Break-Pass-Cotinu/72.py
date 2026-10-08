# 72. Write a program using break inside a nested loop while searching for a social media likes count value.
social_media_likes = [123, 45, 98, 75, 99, 59]
searching_likes = 99
track = False
for likes in social_media_likes:
    if likes == searching_likes:
        track = True
        print("Found:",likes)
        break
if track == False:
    print("Not found")