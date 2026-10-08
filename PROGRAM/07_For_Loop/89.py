# 89. Write a program using a for loop to count how many electricity bill values satisfy a condition.
electricit_bill = [1800, 4000, 1500, 2000,]
count_bill = 0
for i in electricit_bill:
    if i >= 2000:
        count_bill += 1
print(count_bill)