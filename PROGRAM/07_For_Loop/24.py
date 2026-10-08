# 24. Write a program using a for loop to calculate the total of all bank account balance values in a list.
account_balance = [ 2000, 4000, 54000]
total_balance = 0
for i in account_balance:
    total_balance += i
print(total_balance)