# 96. Write a program to unpack nested lists of restaurant orders into separate variables.
restaurant_orders = [["Pizz","Burgar"],["Pasta","Magi"]]
(Orders1,Orders2),(Orders3,Orders4) = restaurant_orders
print("restaurant_orders = 1")
print("restaurant_orders",Orders1)
print("restaurant_orders",Orders2)

print("restaurant_orders = 2")
print("restaurant_orders",Orders3)
print("restaurant_orders",Orders4)