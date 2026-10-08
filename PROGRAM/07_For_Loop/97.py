# 97. Write a program using a for loop to count how many game high score values satisfy a condition.
game_score = [400, 650, 200, 310,]
count_score = 0
for i in game_score:
    if i >= 500:
        count_score += 1
print(count_score)