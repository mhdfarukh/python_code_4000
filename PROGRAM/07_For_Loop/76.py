# 76. Write a program using a for loop to find the minimum restaurant bill value in a list.
restaurant_bill = [500, 150, 5000, 2000, 1000]
minimum_bill = restaurant_bill[0]
for i in restaurant_bill:
    if i < minimum_bill:
        minimum_bill = i
print(minimum_bill)