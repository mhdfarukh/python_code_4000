# 50. Write a program using a for loop to find the maximum library book count value in a list.
library_book = [25, 12, 65, 45]
max_count = 0
for i in library_book:
    if i > max_count:
        max_count = i
print(max_count)