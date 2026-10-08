# 25. Write a program to create a dictionary of bank transactions using curly braces with key-value pairs.
bank_transactions = {"transactions1": 25000,
                     "transactions2": 35000,
                     "transactions3": 80000
                     }
for key , value in bank_transactions.items():
    print(key , value)