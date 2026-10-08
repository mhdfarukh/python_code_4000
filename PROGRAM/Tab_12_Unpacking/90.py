# 90. Write a program to unpack nested lists of library books into separate variables.
library_book = ["book1",150],["book2",500]
(name1,price1),(name2,price2) = library_book
print("LIBRARY BOOK = 1")
print("Name:",name1)
print("Price:",price1)

print("LIBRARY BOOK = 2")
print("Name:",name2)
print("Price:",price2)