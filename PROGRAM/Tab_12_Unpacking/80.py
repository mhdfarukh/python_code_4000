# 80. Write a program to swap two delivery addresses values using unpacking.
addresses1 = ["Bouliya","Lhahartara"]
addresses2 = ["Cant","shigra"]
print("Before")
print("delivery addresses:",addresses1)
print("delivery addresses:",addresses2)

addresses1, addresses2 = addresses2, addresses1

print("After")
print("delivery addresses:",addresses1)
print("delivery addresses:",addresses2)