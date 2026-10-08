# 66. Write a program using break inside a nested loop while searching for a movie rating value.
movie_rating = [15, 45, 60, 75]
seraching_rating = 600
track = False
for rating in movie_rating:
    if rating == seraching_rating:
        track = True
        print("Found:",rating)
        break
if track == False:
    print("Not found")