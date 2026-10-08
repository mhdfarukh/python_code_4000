# 45. Write a program using range(start, stop, step) to print every alternate temperature reading value.
start_reading = 40
stop_reading = 75
step_reading = 5
for i in range(start_reading, stop_reading, step_reading):
    print("temperature reading:", i)