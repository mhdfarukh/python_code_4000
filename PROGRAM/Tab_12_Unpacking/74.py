# 74. Write a program to swap two product inventory values using unpacking.
product1 = ["Electronics", "iphone","Anoroid"]
product2 = ["Anoroid", "judio"]
print("Before")
print("product inventory:",product1)
print("product inventory:",product2)

product1, product2 = product2, product1

print("After")
print("product inventory:",product1)
print("product inventory:",product2)