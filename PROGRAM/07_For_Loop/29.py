# 29. Write a program using a for loop to calculate the total of all electricity bill values in a list.
electricity_bill = [1500, 2000, 2300]
total_bill = 0
for i in electricity_bill:
    total_bill += i
print(total_bill)