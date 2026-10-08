# 55. Write a program to loop through a nested list of traffic signals using nested for loops.
traffic_signal = [[12, 15, 35, 10],[30, 25, 24, 26],
                  [18, 19, 17, 14],[11, 22, 33]
                  ]
for i in traffic_signal:
    for signal in i:
        print(signal)