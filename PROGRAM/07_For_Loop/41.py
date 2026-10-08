# 41. Write a program using a for loop to find the maximum bank account balance value in a list.
account_balance = [200, 2000, 500]
max_balance = 0
# ye har balance me ak ak baar 0 se jodega.
for i in account_balance:
    #  ye ak ak numbers jodne ke liy aage bhajta hai or ye ghum kar i me aajata hai
    if i > max_balance: # ye chak kar rha h ki i > max se bada hai ki nhi.
        max_balance = i
print(max_balance)