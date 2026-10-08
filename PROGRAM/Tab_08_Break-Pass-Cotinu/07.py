# 07. Write a program using break to stop a loop as soon as a target cricket score value is found.
cricket_score = [45, 55, 60, 68, 90, 98, 75]
for i in cricket_score:
    if i in cricket_score:
        if i == 90:
            break
        print(i)