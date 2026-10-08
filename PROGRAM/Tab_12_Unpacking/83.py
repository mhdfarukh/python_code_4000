# 83. Write a program to unpack nested lists of shopping cart items into separate variables.
shopping_items = ["jins", 1, 1200,],["Tshart", 2, 700]
(itme1, quantity1, price1),(itmes2,quantity2,price2) = shopping_items
print("SHOPPING_ITMES = 1")
print("ITEMS1:",itme1)
print("QUANTITY1:",quantity1)
print("PRICE1:",price1)

print("SHOPPING_ITMES = 2")
print("ITEMS2:",itmes2)
print("QUANTITY2:",quantity2)
print("PRICE2:",price2)

