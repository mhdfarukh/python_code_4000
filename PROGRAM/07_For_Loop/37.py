# 37. Write a program using a for loop to calculate the total of all game high score values in a list.
game_score = [120, 35, 500, 150]
total_score = 0
for i in game_score:
    total_score += i 
print(total_score)