# 88. Write a program to unpack nested lists of car inventory into separate variables.
car_inventory = ["Suzuki Swift", 580000],["Ford Ecosport", 5750000]
(name1,price1),(name2,price2) = car_inventory
print("CAR INVENTORY = 1")
print("Name:",name1)
print("Price:",price1)

print("CAR INVENTORY = 2")
print("Name:",name2)
print("Price:",price2)