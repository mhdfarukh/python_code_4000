# 23. Write a program using continue to skip invalid shopping cart total values while looping through a list.
shopping_card = [500, 200, 4000, 5000, 150, 340]
for i in shopping_card:
    if i == 500:
        continue
    print(i)
