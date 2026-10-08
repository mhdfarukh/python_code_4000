# 95. Write a program using a for loop to count how many traffic signal timer values satisfy a condition.
traffic_signal = [130, 25, 48, 15, 30]
count_timer = 0
for i in traffic_signal:
    if i >= 30:
        count_timer += 1
print(count_timer)