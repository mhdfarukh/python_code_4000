# 14. Write a program to create a nested list representing product inventory organized in groups.
product_inventory = [["Blue", "Black"],["Rad", "yellow"],
                     ["White","Green"],["pink", "Bruan"]
                     ]
for i in product_inventory:
    for k in i:
        print(k)