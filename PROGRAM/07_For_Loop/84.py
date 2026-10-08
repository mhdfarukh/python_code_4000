# 84. Write a program using a for loop to count how many bank account balance values satisfy a condition.
account_balance = [4500, 5000, 500, 6500, 2000]
count_balance = 0
for i in account_balance:
    if i >= 3000:
        count_balance += 1
print(count_balance)