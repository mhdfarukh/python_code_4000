# 83. Write a program using a for loop to count how many shopping cart total values satisfy a condition.
shopping_cart = [500, 200, 450, 600, 100]
count_cart = 0
for i in shopping_cart:
    if i >= 300:
        count_cart += 1
print(count_cart)