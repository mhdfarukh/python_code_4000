# 44. Write a program to loop through a nested list of bank transactions using nested for loops.
bank_transactions = [[120, 150, 450],[1000, 2000, 3000],
                     [5000, 2500, 35000],[4850,9000, 10000]
                     ]
for bank in bank_transactions:
    for money in bank:
        print(money)