# 89. Write a program using continue to skip negative electricity bill values in a list and process only positives.
electricity_bill = [200, -150, 540, -300, 456, -800]
for i in electricity_bill:
    if i < 0:
        continue
    print("positives:",i)