# 24. Write a program using continue to skip invalid bank account balance values while looping through a list.
account_balance = [2500, 30000, 45000, 55000, 4560]
for i in account_balance:
    if i == 45000:
        continue
    print(i)