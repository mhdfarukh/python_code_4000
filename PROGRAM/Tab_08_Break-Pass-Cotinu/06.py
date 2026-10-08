# 06. Write a program using break to stop a loop as soon as a target movie rating value is found.
movie_rating = [8, 7, 5, 6, 45, 24, 55, 60]
for i in movie_rating:
    if i == 24:
        break
    print(i)