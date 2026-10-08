# 49. Write a program to unpack a list of electricity bills to get the first and last value with the middle grouped.
electricity_bill = [2000, 5200, 1560, 200, 800, 4600]
first_value, *middlie_value, last_value = electricity_bill
print("first_value:",first_value)
print("Middile_value:",middlie_value)
print("Last_value:",last_value)
