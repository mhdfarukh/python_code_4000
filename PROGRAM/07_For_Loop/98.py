# 98. Write a program using a for loop to count how many recipe ingredient quantity values satisfy a condition.
recipe_ingredient = [45, 98, 85, 75,]
count_quantity = 0
for i in recipe_ingredient:
    if i >= 90:
        count_quantity += 1
print(count_quantity)