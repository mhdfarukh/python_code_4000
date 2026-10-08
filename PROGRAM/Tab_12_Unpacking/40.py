# 40. Write a program to unpack a list of delivery addresses using a star expression to capture the rest.
delivery_addresses = ["Laharatara", "Bouliya", "Cant", "Sigra"]
addresses1,*addresses2 = delivery_addresses
print("delivery_addresses:",addresses1)
print("delivery_addresses:",addresses2)