# Write a program to create a nested list representing stock prices organized in groups.
stock_price = [[1200, 1500, 1400],[4500, 4800, 1520,],
               [1700, 2000, 1000],[1600, 1400]
               ]
for i in stock_price:
    for k in i:
        print(k)