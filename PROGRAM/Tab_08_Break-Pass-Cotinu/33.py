# 33. Write a program using continue to skip invalid stock price values while looping through a list.
stock_price = [500, 800, 4500, 6700, 2100, 3500]
for i in stock_price:
    if i == 2100:
        continue
    print(i)