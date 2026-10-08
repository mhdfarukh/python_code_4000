# 90. Write a program using continue to skip negative library book count values in a list and process only positives.
library_book = [22, 13, -45, 44, -85, -99]
for i in library_book:
    if i < 0:
        continue
    print("positives:",i)