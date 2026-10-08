# 67. Write a program using break inside a nested loop while searching for a cricket score value.
cricket_score = [54, 90, 80, 75, 102]
searching_score = 75
track = False
for score in cricket_score:
    if score == searching_score:
        track = True
        print("Found:",score)
        break
if track == False:
    print("Not found")