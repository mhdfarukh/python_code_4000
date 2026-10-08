# 98. Write a program using range() to generate indices for iterating over a list of recipe ingredient quantity values.
recipe_quantity = [10, 50, 19, 85, 45]
for i in range(len(recipe_quantity)):
    print(i, recipe_quantity[i])