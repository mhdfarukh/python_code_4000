# 24. Write a program to unpack a list of bank transactions using a star expression to capture the rest.
bank_transactions = [2000, 1500, 1800, 1000]
transactions1,transactions2,transactions3, *transactions4 = bank_transactions
print("Transactoins:",transactions1)
print("Transactoins:",transactions2)
print("Transactoins:",transactions3)
print("Transactoins:",transactions4)