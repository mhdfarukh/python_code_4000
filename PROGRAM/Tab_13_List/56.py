# 56. Write a program to loop through a nested list of restaurant orders using nested for loops.
restaurant_orders = [["Burger"],["Pizaa"],
                     ["momoj"],["Roll"]
                     ]
for i in restaurant_orders:
    for orders in i:
        print(orders)