# 56. Write a program using a for loop to find the maximum restaurant bill value in a list.
restaurant_bill = [1500, 1800, 2000, 150 ]
max_bil = 0
for i in restaurant_bill:
    if i > max_bil:
        max_bil = i
print(max_bil)