# 37. Write a program using continue to skip invalid game high score values while looping through a list.
game_score = [500, 4500, 9800, 4560, 5500]
for i in game_score:
    if i == 4560:
        continue
    print(i)