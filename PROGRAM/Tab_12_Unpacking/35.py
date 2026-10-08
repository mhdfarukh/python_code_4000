# 35. Write a program to unpack a list of traffic signals using a star expression to capture the rest.
traffic_signals = [10, 20, 50, 35]
siganls1,*siganls2 = traffic_signals
print("traffic_signal:",siganls1)
print("traffic_signal:",siganls2)