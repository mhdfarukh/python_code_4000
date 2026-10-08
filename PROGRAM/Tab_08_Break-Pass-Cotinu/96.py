# 96. Write a program using continue to skip negative restaurant bill values in a list and process only positives.
restaurant_bill = [2000, 1500, -456, -1200, 5200]
for i in restaurant_bill:
    if i < 0:
        continue
    print("positives:",i)