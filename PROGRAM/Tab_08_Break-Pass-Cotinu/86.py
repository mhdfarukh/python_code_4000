# 86. Write a program using continue to skip negative movie rating values in a list and process only positives.
movie_rating = [2, 5, -8, -9, 6, -7]
for i in movie_rating:
    if i < 0:
        continue
    print("positives:",i)
