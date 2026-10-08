# 96. Write a program using a for loop to count how many restaurant bill values satisfy a condition.
restaurant_bill = [500, 450, 1500, 4800]
count_bill = 0
for i in restaurant_bill:
    if i >= 1000:
        count_bill += 1
print(count_bill)