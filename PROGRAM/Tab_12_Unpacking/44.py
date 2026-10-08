# 44. Write a program to unpack a list of bank transactions to get the first and last value with the middle grouped.
bank_transactions = [200, 150, 5000, 3500, 1500]
first_value, *middile_value, Last_value = bank_transactions
print("first_value:",first_value)
print("middile_value:",middile_value)
print("Last_value:",Last_value)