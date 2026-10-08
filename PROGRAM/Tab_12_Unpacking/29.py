# 29. Write a program to unpack a list of electricity bills using a star expression to capture the rest.
electricity_bill = [2000, 1500, 4560, 5000, 489]
bill1, bill2, *bill3 = electricity_bill
print("Bill:",bill1)
print("Bill:",bill2)
print("Bill:",bill3)