# 95. Write a program using continue to skip negative traffic signal timer values in a list and process only positives.
traffic_siganl_timer = [12, 16, 30, -15, -19, -17]
for i in traffic_siganl_timer:
    if i < 0:
        continue
    print("positives:",i)