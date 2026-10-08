# 63. Write a program using break inside a nested loop while searching for a shopping cart total value.
shopping_total = [200, 400, 600, 800, 150]
searching_shopping = 800
track = False
for shopping in shopping_total:
    if shopping == searching_shopping:
       track = True
       print("Found:", shopping)
       break
if track == False:
   print("Not found:")
