# 55. Write a program using a for loop to find the maximum traffic signal timer value in a list.
traffic_signal = [15, 25, 30, 18,]
max_timer = 0
for i in traffic_signal:
    if i > max_timer:
        max_timer = i 
print(max_timer)