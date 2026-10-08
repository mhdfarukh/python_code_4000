# 70. Write a program to swap two library books values using unpacking.
library1 = [22, 10, 15, 19]
library2 = [10, 17, 15]
print("Before")
print(" library books:",library1)
print(" library books:",library2)

library1 ,library2 = library2 ,library1

print("After")
print(" library books:",library1)
print(" library books:",library2)