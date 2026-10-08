# 29. Write a program using continue to skip invalid electricity bill values while looping through a list.
electricity_bill = [1700, 2000, 1500, 4500, 5500]
for i in electricity_bill:
    if i == 2000:
        continue
    print(i)