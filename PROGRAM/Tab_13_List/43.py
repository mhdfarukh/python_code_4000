# 43. Write a program to loop through a nested list of shopping cart items using nested for loops.
shopping_itmes = [["Oranges","pineapples","Bananas"],["potato","Tomato","Onion"]]

for shopping in shopping_itmes:
    for itmes in shopping:
        print(itmes)
    