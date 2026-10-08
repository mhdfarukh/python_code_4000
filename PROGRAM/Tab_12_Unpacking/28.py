# 28. Write a program to unpack a list of car inventory using a star expression to capture the rest.
car_inventory = ["maruti","tata","mahidra","hyundai creta"]
*inventory1,inventory2,inventory3 = car_inventory
print("Car_inventory:",inventory1)
print("Car_inventory:",inventory2)
print("Car_inventory:",inventory3)