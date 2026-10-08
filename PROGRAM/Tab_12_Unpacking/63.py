# 63. Write a program to swap two shopping cart items values using unpacking.
shopping1 = ["jins", "pant", "shart", "Tshart", "lowar"]
shopping2 = ["pant", "shart", "jins", "lowar", ]
print("Before")
print("shopping:",shopping1)
print("shopping:",shopping2)
shopping1 , shopping2 = shopping2 , shopping1
print("After")
print("shopping_items1:",shopping1)
print("shopping_items2:",shopping2)