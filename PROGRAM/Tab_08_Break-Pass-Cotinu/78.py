# 78. Write a program using break inside a nested loop while searching for a recipe ingredient quantity value.
recipe_quantity = [22, 15, 46, 59, 85]
searching_quantity = 59
track = False
for quantity in recipe_quantity:
    if quantity == searching_quantity:
        track = True
        print("Found:",quantity)
        break
if track == False:
    print("Not found")