# 48. Write a program to loop through a nested list of car inventory using nested for loops.
car_inventory = [
                 ["Camry", "Corolla"], ["RAV4", "Highlander"],
                 ["Mustang", "Fusion"], ["Explorer", "Escape"]
                 ]
for i in car_inventory:
    for car in i:
        print(car)