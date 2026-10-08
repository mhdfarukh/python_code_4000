# 58. Write a program to unpack a list of recipe ingredients to get the first and last value with the middle grouped.
recipe_ingredients = ["Oill", "onions", "tomatoes", "Salt", "papper"]
first, *middile, last = recipe_ingredients
print("first_value:",first)
print("Middile_value:",middile)
print("Last_value:",last)