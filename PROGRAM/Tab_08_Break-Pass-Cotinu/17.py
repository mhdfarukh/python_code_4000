# 17. Write a program using break to stop a loop as soon as a target game high score value is found.
game_scoer = [15, 99, 85, 100, 150, 145]
for i in game_scoer:
    if i == 150:
        break
    print(i)
