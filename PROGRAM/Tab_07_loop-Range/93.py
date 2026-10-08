# 93. Write a program using range() to generate indices for iterating over a list of stock price values.
stock_price = [500, 450, 200, 3600, 1200]
for i in range(len(stock_price)):
    print(i, stock_price[i])