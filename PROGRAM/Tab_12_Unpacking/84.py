# 84. Write a program to unpack nested lists of bank transactions into separate variables.
Bank_transactions = ["shivam", "diposit", 1500,],["Rahul", "withdraw", 50,]
(name1, type1, amount1),(name2, type2,amount2) = Bank_transactions
print("BANK_TRANSACTIONS = 1")
print("Name1:",name1)
print("Type1:",type1)
print("Amount1:",amount1)

print("BANK_TRANSACTIONS = 2")
print("Nanme2:",name2)
print("Type2:",type2)
print("Amount2:",amount2)