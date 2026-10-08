# 17. Write a program to create a nested list representing game scores organized in groups.
game_score = [[200, 500, 460],[456, 789],[750, 800]]
for i in game_score:
    for k in i:
        print(k)