# 49. Write a program to loop through a nested list of electricity bills using nested for loops.
electricity_bill = [[150, 2100, 1200],[400,500,600],[2000, 4000, 5000]]
for i in electricity_bill:
    for bill in i:
        print(bill)