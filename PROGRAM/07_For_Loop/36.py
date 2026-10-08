# 36. Write a program using a for loop to calculate the total of all restaurant bill values in a list.
restaurant_bill = [2500, 1500, 2000]
total_bill = 0
for i in restaurant_bill:
    total_bill += i
print(total_bill)