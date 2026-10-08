# 57. Write a program to loop through a nested list of game scores using nested for loops.
game_scores = [[200, 100, 150, 98],[1500, 1600, 1400],
               [1000, 1012, 468, 456],[7897, 4567, 461]
               ]
for i in game_scores:
    for game in i:
        print(game)