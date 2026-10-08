# 73. Write a program using range() in reverse to count down a stock price value.
stock_price = 2000
for i in range(stock_price, -1, -100):
    print("stock price:", i)