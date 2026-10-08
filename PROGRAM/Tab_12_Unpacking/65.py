# 65. Write a program to swap two temperature readings values using unpacking.
temperature1 = [22, 25, 23, 14]
temperature2 = [74, 45, 56, 10]
print("Before")
print("temperature1:",temperature1)
print("temperature2:",temperature2)
temperature1 , temperature2 = temperature2 , temperature1
print("After")
print("temperature1:",temperature1)
print("temperature1:",temperature2)