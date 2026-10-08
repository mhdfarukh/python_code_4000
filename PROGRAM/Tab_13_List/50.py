# 50. Write a program to loop through a nested list of library books using nested for loops.
library_book = [[25, 30, 40],[45, 50, 60]]
for i in library_book:
    for book in i:
        print(book)