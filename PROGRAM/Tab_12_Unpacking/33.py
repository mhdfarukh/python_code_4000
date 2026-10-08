# 33. Write a program to unpack a list of stock prices using a star expression to capture the rest.
stock_price = [200, 1500, 2000, 3000, 1450,]
price1, *price2 = stock_price
print("stock_price:",price1)
print("stock_price:",price2)