# 44. Write a program using a for loop to find the maximum shopping cart total value in a list.
shopping_cart = [200, 2500, 1500, 2300]
max_total = 0
for i in shopping_cart:
    if i > max_total:
        max_total = i
print(max_total)
