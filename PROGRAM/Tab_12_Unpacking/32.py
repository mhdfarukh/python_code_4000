# 32. Write a program to unpack a list of social media followers using a star expression to capture the rest
social_media_followers = [15, 48, 75, 42, 95, 83]
followers1, *followers2 =social_media_followers
print("social_media_followers:",followers1)
print("social_media_followers:",followers2)
