# 55. Write a program to unpack a list of traffic signals to get the first and last value with the middle grouped.
traffic_signals = [15, 16, 30, 45, 19, 18, 20]
first, *middile, last = traffic_signals
print("first_value:",first)
print("Middile_value:",middile)
print("Last_value:",last)