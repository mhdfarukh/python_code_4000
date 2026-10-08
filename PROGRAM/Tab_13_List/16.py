# 16. Write a program to create a nested list representing restaurant orders organized in groups.
restauant_orders = [[["cheeseburger", "Pizza"],["Chicken Wings","French Fries"]],
                    [["Salad"],["Water"]]
                    ]
for i in restauant_orders:
    for k in i:
        for j in k:
            print(j)