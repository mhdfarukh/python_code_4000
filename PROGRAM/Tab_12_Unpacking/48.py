# 48. Write a program to unpack a list of car inventory to get the first and last value with the middle grouped.
car_inventory = ["maruti","tata","mahidra","hyundai creta"]
first_value, *middile_value, last_value = car_inventory
print("first_value:",first_value)
print("Middile_value:",middile_value)
print("Last_value:",last_value)
