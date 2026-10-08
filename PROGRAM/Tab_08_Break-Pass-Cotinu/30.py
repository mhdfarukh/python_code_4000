# 30. Write a program using continue to skip invalid library book count values while looping through a list.
library_book = [25, 30, 55, 16, 18, 75]
for i in library_book:
    if i == 16:
        continue
    print(i)