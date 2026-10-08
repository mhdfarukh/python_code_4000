# 04. Write a program using break to stop a loop as soon as a target bank account balance value is found.
bank_account = [1800, 4500, 4000, 6500, 555, 410, 500]
for i in bank_account:
    if i == 6500:
        break
    print(i)
