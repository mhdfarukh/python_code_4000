# 52. Write a program using a for loop to find the maximum social media likes count value in a list.
social_media = [50, 68, 90, 40, 87,]
max_likes = 0
for i in social_media:
    if i > max_likes:
        max_likes = i
print(max_likes)