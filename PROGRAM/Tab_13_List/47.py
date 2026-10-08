# 47. Write a program to loop through a nested list of cricket scores using nested for loops.
cricket_scores = [[150, 98, 75],[100, 200, 250],[85,65, 95],[360, 240, 175]]
for i in cricket_scores:
    for scores in i:
        print(scores)