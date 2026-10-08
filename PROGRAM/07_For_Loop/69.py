# 69. Write a program using a for loop to find the minimum electricity bill value in a list.
electricity_bill = [4500, 1200, 1000, 1500, 2500]
minimum_bill = electricity_bill[0]
for i in electricity_bill:
    if i < minimum_bill:
        minimum_bill = i 
print(minimum_bill)