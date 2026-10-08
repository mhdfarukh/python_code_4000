# 76. Write a program to swap two restaurant orders values using unpacking.
restaurant1 = ["pizaa", "Burgar", "Momoj", "chat"]
restaurant2 = ["burgar","momo"]
print("Before")
print("restaurant orders:",restaurant1)
print("restaurant orders:",restaurant2)

restaurant1, restaurant2 = restaurant2, restaurant1

print("After")
print("restaurant orders:",restaurant1)
print("restaurant orders:",restaurant2)