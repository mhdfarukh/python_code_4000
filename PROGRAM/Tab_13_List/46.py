# 46. Write a program to loop through a nested list of movie ratings using nested for loops.
movie_reating = [[10, 5, 9],[15, 20, 25],
                 [19, 30, 35],[8, 17, 4]
                 ]
for movie in movie_reating:
    for reating in movie:
        print(reating)