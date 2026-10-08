# 43. Write a program to unpack a list of shopping cart items to get the first and last value with the middle grouped.
shopping_items = ["jins", "pant", "shart", "Tshart", "lowar"]
first_value, *middile_value, last_value =shopping_items
print("first_value:",first_value)
print("middile_value:",middile_value)
print("Last_value:",last_value)
