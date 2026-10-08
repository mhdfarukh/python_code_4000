# 03. Write a program to create a nested list representing shopping cart items organized in groups.
shopping_cart_items = [[[2, 10, 20, 30],[40, 50, 60, 70]],[[74, 85, 96],[65, 52]]]
for i in shopping_cart_items:
    for k in i:
        for h in k:
            print(h)