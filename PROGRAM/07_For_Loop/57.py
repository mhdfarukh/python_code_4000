# 57. Write a program using a for loop to find the maximum game high score value in a list.
game_score = [250, 360, 150, 315]
max_score = 0
for i in game_score:
    if i > max_score:
        max_score = i 
print(max_score)