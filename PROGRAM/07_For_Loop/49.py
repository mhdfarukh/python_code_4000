# 49. Write a program using a for loop to find the maximum electricity bill value in a list.
electricity_bill = [1500, 2000, 4500, 1200, 3000]
max_bill = 0
for i in electricity_bill:
    if i > max_bill:
        max_bill = i
print(max_bill)