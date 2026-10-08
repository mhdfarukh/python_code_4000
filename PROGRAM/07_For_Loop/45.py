# 45. Write a program using a for loop to find the maximum movie rating value in a list.
movie_rating = [250, 150, 500, 550, 600]
max_rating = 0
for i in movie_rating:
    if i > max_rating:
        max_rating = i
print(max_rating)