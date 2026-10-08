# 38. Write a program using continue to skip invalid recipe ingredient quantity values while looping through a list.
recipe_quantity = [10, 25, 30, 95, 46, 67, 40]
for i in recipe_quantity:
    if i == 95:
        continue
    print(i)