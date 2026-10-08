# 94. Write a program to unpack nested lists of product inventory into separate variables.
product_inventory = [["Electronics", "iphone",],["Anoroid", "judio"]]
(inventory1,inventory2),(inventory3,inventory4) = product_inventory
print("product inventory = 1")
print("product inventory1:",inventory1)
print("product inventory2:",inventory2)
#print("product inventory3:",inventory1)

print("product inventory = 2")
print("product inventory1:",inventory3)
print("product inventory2:",inventory4)
#print("product inventory3:",inventory2)
