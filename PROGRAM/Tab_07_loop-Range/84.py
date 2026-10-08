# 84. Write a program using range() to generate indices for iterating over a list of bank account balance values.
bank_account = [500, 1500, 1200, 5000, 24000]
for i in range(len(bank_account)):
    print( i, bank_account[i])