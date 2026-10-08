# 89. Write a program using range() to generate indices for iterating over a list of electricity bill values.
electricity_bill = [4500, 3000, 1200, 2600, 1800]
for i in range(len(electricity_bill)):
    print(i, electricity_bill[i])