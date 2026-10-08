# 70. Write a program using break inside a nested loop while searching for a library book count value.
library_book = [25, 34, 49, 15, 10]
searching_book = 15
track = False
for book in library_book:
    if book == searching_book:
        track = True
        print("Found:",book)
        break
if track == False:
    print("Not found")
