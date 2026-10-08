# 58. Write a program using a for loop to find the maximum recipe ingredient quantity value in a list.
recipe_puantity = [25, 40, 98, 54, 70]
max_puantity = 0
for i in recipe_puantity:
    if i > max_puantity:
        max_puantity = i 
print(max_puantity)