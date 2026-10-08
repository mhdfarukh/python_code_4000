# 66. Write a program using a for loop to find the minimum movie rating value in a list.
movie_rating = [360, 300, 150, 250, 200]
minimum_rating = movie_rating[0]
for i in movie_rating:
    if i < minimum_rating:
     minimum_rating = i 
print(minimum_rating)