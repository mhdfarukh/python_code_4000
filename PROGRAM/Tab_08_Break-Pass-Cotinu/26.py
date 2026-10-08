# 26. Write a program using continue to skip invalid movie rating values while looping through a list.
movei_rating = [24, 51, 18, 16, 1, 55]
for i in movei_rating:
    if i == 1:
        continue
    print(i)