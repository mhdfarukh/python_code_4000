# 36. Write a program to unpack a list of restaurant orders using a star expression to capture the rest.
restaurant_oders = ["pizaa", "Burgar", "Momoj", "chat"]
oders1,*oders2 = restaurant_oders
print("restaurant_oders:",oders1)
print("restaurant_oders:",oders2)