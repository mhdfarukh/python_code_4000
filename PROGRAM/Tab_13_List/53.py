# 53. Write a program to loop through a nested list of stock prices using nested for loops.
stock_prices = [["price:1", 2000, 500, 600, 150],["price:2",1500, 1800, 400, 2450],
                ["price:3",1200, 6500, 3500],["price:4",700, 800, 900, 650]
                ]
for i in stock_prices:
    for price in i:
        print(price)