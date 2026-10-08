# 77. Write a program using range() in reverse to count down a game high score value.
game_score = 500
for i in range(game_score, -1, -50):
    print("game score:", i)