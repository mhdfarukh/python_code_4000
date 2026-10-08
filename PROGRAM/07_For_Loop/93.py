# 93. Write a program using a for loop to count how many stock price values satisfy a condition.
stock_price = [800,900, 500, 4600, 125]
count_price = 0
for i in stock_price:
    if i >= 1000:
        count_price += 1
print(count_price)