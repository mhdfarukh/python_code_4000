# 93. Write a program using continue to skip negative stock price values in a list and process only positives.
stock_price = [2000, -150, 640, 5000, -800, -400, 1500]
for i in stock_price:
    if i < 0:
        continue
    print("positives:",i)