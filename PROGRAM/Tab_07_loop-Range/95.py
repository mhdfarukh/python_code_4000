# 95. Write a program using range() to generate indices for iterating over a list of traffic signal timer values.
traffic_signal = [30, 12, 15, 20, 18]
for i in range(len(traffic_signal)):
    print(i, traffic_signal[i])