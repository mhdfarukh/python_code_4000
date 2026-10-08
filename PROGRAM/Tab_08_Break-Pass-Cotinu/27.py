# 27. Write a program using continue to skip invalid cricket score values while looping through a list.
cricket_score = [85, 97, 93, 45, 120, 54, ]
for i in cricket_score:
    if i == 120:
        continue
    print(i)