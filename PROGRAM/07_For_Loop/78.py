# 78. Write a program using a for loop to find the minimum recipe ingredient quantity value in a list.
recipe_ingredient = [150, 45, 22, 56, 68,]
minimum_quantity =recipe_ingredient[0]
for i in recipe_ingredient:
    if i < minimum_quantity:
        minimum_quantity = i 
print(minimum_quantity)