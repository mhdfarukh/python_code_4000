# 73. Write a program using break inside a nested loop while searching for a stock price value.
stock_price = [2000, 2500, 2450, 8540, 5000]
searching_price = 2451
track = False
for price in stock_price:
    if price == searching_price:
        track = True
        print("Found:",price)
        break
if track == False:
    print("Not found")