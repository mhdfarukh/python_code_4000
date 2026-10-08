# 87. Write a program using a for loop to count how many cricket score values satisfy a condition.
cricket_score = [98, 85, 74, 102, 75]
count_score = 0
for i in cricket_score:
    if i >= 90:
        count_score += 1
print(count_score)