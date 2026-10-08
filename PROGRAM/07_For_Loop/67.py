# 67. Write a program using a for loop to find the minimum cricket score value in a list.
cricket_score = [360, 200, 150, 98, 225, 264]
minimum_score = cricket_score[0]
for i in cricket_score:
    if i < minimum_score:
        minimum_score = i 
print(minimum_score)