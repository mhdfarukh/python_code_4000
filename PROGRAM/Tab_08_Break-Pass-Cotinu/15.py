# 15. Write a program using break to stop a loop as soon as a target traffic signal timer value is found.
traffic_signal = [30, 25, 12, 10, 130, 150,]
for i in traffic_signal:
    if i == 130:
        break
    print(i)