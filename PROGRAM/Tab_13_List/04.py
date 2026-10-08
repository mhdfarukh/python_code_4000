# 04. Write a program to create a nested list representing bank transactions organized in groups.
def nested():
    bank_transactions = [[200, 300, 400],[500, 600, 2000]]
    for i in bank_transactions:
       for k in i:
          print(k)
nested()