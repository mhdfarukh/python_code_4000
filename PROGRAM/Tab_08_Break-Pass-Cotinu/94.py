# 94. Write a program using continue to skip negative water tank level values in a list and process only positives
water_tank = [22, -45, -55, -19, 50, 100]
for i in water_tank:
    if i < 0:
        continue
    print("positives:",i)