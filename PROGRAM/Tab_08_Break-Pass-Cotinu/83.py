# 83. Write a program using continue to skip negative shopping cart total values in a list and process only positives.
shopping_card = [150, -152, 254, 524 -25, -456]
for i in shopping_card:
    if i < 0:
        continue

    print("positives:",i)