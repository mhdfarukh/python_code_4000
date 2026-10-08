# 23. Write a program to unpack a list of shopping cart items using a star expression to capture the rest.
shopping_items = ["shart","pant","Tshart"]
*itmes1, itmes2, itmes3 = shopping_items
print("Shart:", itmes1, "Pant:",itmes2, "Tshart:",itmes3)
