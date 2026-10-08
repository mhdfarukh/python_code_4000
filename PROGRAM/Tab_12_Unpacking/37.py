# 37. Write a program to unpack a list of game scores using a star expression to capture the rest.
game_score = [200, 500, 460, 750, 800]
score1,*score2 = game_score
print("game_score:",score1)
print("game_score:",score2)