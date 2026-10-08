# 10. Write a program using break to stop a loop as soon as a target library book count value is found.
library_book = [20, 10, 15, 50, 45, 75]
for i in library_book:
    if i == 45:
        break
    print(i)