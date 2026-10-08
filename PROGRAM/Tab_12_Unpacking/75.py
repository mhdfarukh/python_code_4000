# 75. Write a program to swap two traffic signals values using unpacking.
traffic1 = [12, 15, 14, 18, 16]
traffic2 = [10, 9, 30, 15]
print("Before")
print(" traffic signals:",traffic1)
print(" traffic signals:",traffic2)

traffic1, traffic2 = traffic2, traffic1

print("After")
print(" traffic signals:",traffic1)
print(" traffic signals:",traffic2)