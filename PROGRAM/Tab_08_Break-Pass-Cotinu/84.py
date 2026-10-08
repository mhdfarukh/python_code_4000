# 84. Write a program using continue to skip negative bank account balance values in a list and process only positives.
account_balance = [-200, 5000, 2000, -800, ]
for i in account_balance:
    if i < 0:
        continue
    print("positives:",i)