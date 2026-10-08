# 97. Write a program using range() to generate indices for iterating over a list of game high score values.
game_score = [500, 100, 150, 300]
for i in range(len(game_score)):
    print(i, game_score[i])