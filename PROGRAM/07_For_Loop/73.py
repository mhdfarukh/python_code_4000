# 73. Write a program using a for loop to find the minimum stock price value in a list.
stock_price = [5500, 2000, 4500, 1500, 4000]
minimum_price = stock_price[0]
for i in stock_price:
    if i < minimum_price:
        minimum_price = i 
print(minimum_price)