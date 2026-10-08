# 34. Write a program to unpack a list of product inventory using a star expression to capture the rest.
product_inventory = ["Electronics", "iphone", "Anoroid", "judio"]
product1,*product2 = product_inventory
print("Product1:",product1)
print("Product1:",product2)