# 18. Write a program using break to stop a loop as soon as a target recipe ingredient quantity value is found.
recipe_quantity = [85, 54, 67, 20, 150, 200]
for i in recipe_quantity:
    if i == 150:
        break
    print(i)