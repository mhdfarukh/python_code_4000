# 68. Write a program to swap two car inventory values using unpacking.
car1 = ["maruti","tata","mahidra","hyundai creta"]
car2 = ["Tata", "maruti", "mahidra"]
print("Before")
print("car_inventory:",car1)
print("car_inventory:",car2)
car1 , car2 = car2, car1
print("After")
print("car_inventory:",car1)
print("car_inventory:",car2)
