# 58. Write a program to loop through a nested list of recipe ingredients using nested for loops.
recipe_ingredients =  [["cheeseburger", "Pizza"],["Chicken Wings","French Fries"],
                    ["Salad"],["Water"]
                    ]
for i in recipe_ingredients:
    for recipe in i:
        print(recipe)