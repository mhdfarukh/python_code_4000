# 33. Write a program using a for loop to calculate the total of all stock price values in a list.
all_stock = [2500, 3500, 5000]
total_price = 0
for i in all_stock:
    total_price += i
print(total_price)