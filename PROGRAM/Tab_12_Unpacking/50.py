# 50. Write a program to unpack a list of library books to get the first and last value with the middle grouped.
library_book = [22, 52, 45, 48, 76, 58, 98]
first_value,*middile_value,last_value = library_book
print("first_value:",first_value)
print("Middile_value:",middile_value)
print("Last_value:",last_value)