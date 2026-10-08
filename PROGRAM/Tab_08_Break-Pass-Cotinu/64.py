# 64. Write a program using break inside a nested loop while searching for a bank account balance value.
account_balance = [500, 1506, 4561, 125, 2000]
searching_balance = 125
track = False
for balance in account_balance:
    if balance == searching_balance:
        track = True
        print("Found:",balance)
        break
if track == False:
    print("Not found:")