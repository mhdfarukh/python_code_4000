# 75. Write a program using a for loop to find the minimum traffic signal timer value in a list.
traffic_signal = [120, 30, 52, 60]
minimum_timer = traffic_signal[0]
for i in traffic_signal:
    if i < minimum_timer:
        minimum_timer = i
print(minimum_timer)