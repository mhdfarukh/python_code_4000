# 69. Write a program using break inside a nested loop while searching for a electricity bill value.
electricity_bill = [2000, 445, 5000, 6540, 200]
searching_bill = 6540
track = False
for bill in electricity_bill:
    if bill == searching_bill:
        track = True
        print("Found:",bill)
        break
if track == False:
    print("Not found")