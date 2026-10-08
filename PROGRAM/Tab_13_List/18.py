# 18. Write a program to create a nested list representing recipe ingredients organized in groups.
recipe_ingredients = [[[25, 50, 60],[150, 163, 15]],
                      [[10, 50, 20],[5, 4, 6]]
                      ]
for i in recipe_ingredients:
    for k in i:
        for j in k:
            print(j)