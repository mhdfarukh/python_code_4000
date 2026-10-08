# 13. Write a program using break to stop a loop as soon as a target stock price value is found.
stock_price = [500, 1000, 1500, 2500, 100]
for i in stock_price:
    if i == 2500:
        break
    print(i)