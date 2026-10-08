# 98. Write a program using continue to skip negative recipe ingredient quantity values in a list and process only positives.
recipe_quantity = [22, -10, 55, 20, -30, 45]
for i in recipe_quantity:
    if i < 0:
        continue
    print("positives:",i)