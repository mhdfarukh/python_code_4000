# 30. Write a program to unpack a list of library books using a star expression to capture the rest.
library_book = [12, 15, 10, 18, 20]
book1, *book2, book3 =library_book
print("library_book:",book1)
print("library_book:",book2)
print("library_book:",book3)