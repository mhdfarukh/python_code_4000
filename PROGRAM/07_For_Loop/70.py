# 70. Write a program using a for loop to find the minimum library book count value in a list.
library_book = [150, 25, 50, 65, 40]
minimum_book = library_book[0]
for i in library_book:
    if i < minimum_book:
        minimum_book = i 
print(minimum_book)