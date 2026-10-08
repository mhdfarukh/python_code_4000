# 63. Write a program using a for loop to find the minimum shopping cart total value in a list.
shopping_card = [2500, 1500, 4500, 1200, 200 ]
minimmum_card = shopping_card[0]
for i in shopping_card:
    if i < minimmum_card:
        minimmum_card = i 
print(minimmum_card)