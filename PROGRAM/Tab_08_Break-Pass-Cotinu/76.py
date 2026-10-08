# 76. Write a program using break inside a nested loop while searching for a restaurant bill value.
restaurant_bill = [150, 25, 500, 160]
searching_bill = 500
track = False
for bill in restaurant_bill:
    if bill == searching_bill:
        track = True
        print("Found:",bill)
        break
if track == False:
    print("Not found")