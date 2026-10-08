# 64.  Write a program using a for loop to find the minimum bank account balance value in a list.
account_balance = [45000, 25000, 1560, 15220, 1200]
minimum_balance = account_balance[0]
for i in account_balance:
    if i < minimum_balance:
        minimum_balance = i 
print(minimum_balance)