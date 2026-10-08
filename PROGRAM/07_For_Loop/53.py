# 53. Write a program using a for loop to find the maximum stock price value in a list.
stock_price = [2500, 4000, 1800, 2000]
max_price = 0
for i in stock_price:
    if i > max_price:
        max_price = i 
print(max_price)