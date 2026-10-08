# 09. Write a program to create a nested list representing electricity bills organized in groups.
electricity_bill = [[2000, 1500, 4000],[200, 500, 300]]
for i in electricity_bill:
    for h in i:
        print(h)