# 03. Write a program using break to stop a loop as soon as a target shopping cart total value is found.
shopping_card = [200, 500, 8400, 4500, 610, 450]
for i in shopping_card:
    if i == 4500:
      break
    print(i)