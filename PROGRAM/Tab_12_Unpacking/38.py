# 38. Write a program to unpack a list of recipe ingredients using a star expression to capture the rest.
recipe_ingredients = ["Oill", "onions", "tomatoes", "Salt", "papper"]
ingredients1,*ingredients2 = recipe_ingredients
print("recipe_ingredients:",ingredients1)
print("recipe_ingredients:",ingredients2)