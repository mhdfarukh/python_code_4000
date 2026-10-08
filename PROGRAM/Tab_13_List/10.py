# 10. Write a program to create a nested list representing library books organized in groups.
library_book = [[25, 30, 10],[8, 5, 2]],[[52, 45, 40],[15, 19, 14]]
for i in library_book:
    for j in i:
        for k in i:
            print(k)