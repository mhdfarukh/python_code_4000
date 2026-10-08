# 69. Write a program to swap two electricity bills values using unpacking.
electricity1 = [200, 500, 4500, 800]
electricity2 = [ 5000, 4000, 4560]
print("Before")
print("electricity bills:",electricity1)
print("electricity bills:",electricity2)

electricity1 ,electricity2 = electricity2 ,electricity1

print("After")
print("electricity bills:",electricity1)
print("electricity bills:",electricity2)