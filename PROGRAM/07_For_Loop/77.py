# 77. Write a program using a for loop to find the minimum game high score value in a list.
game_score = [1500, 500, 200, 1000, 640]
minimum_score = game_score[0]
for i in game_score:
    if i < minimum_score:
      minimum_score = i 
print(minimum_score)