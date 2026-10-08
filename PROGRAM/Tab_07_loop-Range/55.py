# 55. Write a program using range(start, stop, step) to print every alternate traffic signal timer value.
start_timer = 1
stop_timer = 30
step_timer = 2
for i in range(start_timer, stop_timer, step_timer):
    print("traffic signal timer:", i)