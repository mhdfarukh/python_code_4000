# 72. Write a program using a for loop to find the minimum social media likes count value in a list.
social_media = [58, 87, 22, 98, 99]
minimumm_likes = social_media[0]
for i in social_media:
    if i < minimumm_likes:
        minimumm_likes = i 
print(minimumm_likes)