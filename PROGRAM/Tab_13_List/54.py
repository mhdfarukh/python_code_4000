# 54. Write a program to loop through a nested list of product inventory using nested for loops.
product_inventory = [["Blue", "Black"],["Rad", "yellow"],
                     ["White","Green"],["pink", "Bruan"]
                     ]
for i in product_inventory:
    for product in i:
        print(product)