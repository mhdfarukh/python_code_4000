# 92. Write a program using a for loop to count how many social media likes count values satisfy a condition.
social_media = [50, 55, 48, 98, 78, 76,]
count_like = 0
for i in social_media:
    if i >= 60:
        count_like += 1
print(count_like)