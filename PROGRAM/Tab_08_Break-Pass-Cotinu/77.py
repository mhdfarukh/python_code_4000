# 77. Write a program using break inside a nested loop while searching for a game high score value.
game_high_score = [250, 456, 123, 785, 400]
searching_score = 785
track = False
for score in game_high_score:
    if score == searching_score:
        track = True
        print("Found:",score)
        break
if track == False:
    print("Not found")