# 54. Write a program to unpack a list of product inventory to get the first and last value with the middle grouped.
product_inventory = ["Electronics", "iphone", "Anoroid", "judio"]
first, *middile, last = product_inventory
print("first_value:",first)
print("Middile_value:",middile)
print("Last_value:",last)