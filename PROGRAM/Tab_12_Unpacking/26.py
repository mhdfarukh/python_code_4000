# 26. Write a program to unpack a list of movie ratings using a star expression to capture the rest.
movie_rating = [12, 15, 19, 8, 5, 4]
*rating1, rating2, rating3 = movie_rating
print("Rating:",rating1)
print("Rating:",rating2)
print("Rating:",rating3)