# 56. Write a program to unpack a list of restaurant orders to get the first and last value with the middle grouped.
restaurant_oders = ["pizaa", "Burgar", "Momoj", "chat"]
first, *middile, last = restaurant_oders
print("first_value:",first)
print("Middile_value:",middile)
print("Last_value:",last)