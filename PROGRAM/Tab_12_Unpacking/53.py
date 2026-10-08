# 53. Write a program to unpack a list of stock prices to get the first and last value with the middle grouped.
stock_prices = [500, 400, 150, 5000, 1560]
first, *middile, last = stock_prices
print("first_value:",first)
print("Middile_value:",middile)
print("Last_value:",last)