# 97. Write a program using continue to skip negative game high score values in a list and process only positives.
game_high_score = [520, 500, 150, -456, -789, -156]
for i in game_high_score:
    if i < 0:
        continue
    print("positives:",i)