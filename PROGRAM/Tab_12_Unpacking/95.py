# 95. Write a program to unpack nested lists of traffic signals into separate variables.
traffic_signals = [[12, 15, 16,],[30, 45, 19]]
(signal1,signal2,signal3),(signal4,signal5,signal6) = traffic_signals
print("Traffic signal = 1")
print("Traffic Signals1:",signal1)
print("Traffic Signals2:",signal2)
print("Traffic Signals3:",signal3)

print("Traffic signal = 2")
print("Traffic Signals1:",signal4)
print("Traffic Signals2:",signal5)
print("Traffic Signals3:",signal6)