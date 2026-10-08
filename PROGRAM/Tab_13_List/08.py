# 08. Write a program to create a nested list representing car inventory organized in groups.
car_inventory = [
                 ["Camry", "Corolla"], ["RAV4", "Highlander"],
                 ["Mustang", "Fusion"], ["Explorer", "Escape"]
                 ]
for i in car_inventory:
    for j in i:
        for h in i:
            print(h)