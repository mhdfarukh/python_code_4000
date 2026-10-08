# 96. Write a program using range() to generate indices for iterating over a list of restaurant bill values.
restaurant_bill = [1500, 2000, 1800, 1200]
for i in range(len(restaurant_bill)):
    print(i, restaurant_bill[i])