# 90. Write a program using a for loop to count how many library book count values satisfy a condition.
book_count = [92, 58, 78, 49, 69]
count_book = 0
for i in book_count:
    if i >= 80:
        count_book += 1
print(count_book)