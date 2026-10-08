# 75. Write a program using break inside a nested loop while searching for a traffic signal timer value.
traffic_signal_timer = [12, 15, 30, 25, 29, 18]
searching_timer = 29
track = False
for timer in traffic_signal_timer:
    if timer == searching_timer:
        track = True
        print("Found:",timer)
        break
if track == False:
    print("Not found")