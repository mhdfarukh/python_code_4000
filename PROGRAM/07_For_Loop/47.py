# 47. Write a program using a for loop to find the maximum cricket score value in a list.
cricket_score = [120, 98, 193, 85, 112]
max_score = 0
for i in cricket_score:
    if i > max_score:
        max_score = i 
print(max_score)