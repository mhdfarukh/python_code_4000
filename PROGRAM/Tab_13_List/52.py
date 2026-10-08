# 52. Write a program to loop through a nested list of social media followers using nested for loops.
social_media_followers = [["follower:1",150, 160, 98],["follower:2", 90, 200, 400],
                          ["follower:3", 800, 900, 1000],["follower:4",110, 210, 305]
                          ]
for i in social_media_followers:
    for followers in i:
        print(followers)