# 36. Write a program using continue to skip invalid restaurant bill values while looping through a list.
restaurant_bill = [250, 480, 4500, 650, 15000, 654]
for i in restaurant_bill:
    if i == 15000:
        continue
    print(i)