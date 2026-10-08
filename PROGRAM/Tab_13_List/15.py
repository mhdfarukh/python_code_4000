# 15. Write a program to create a nested list representing traffic signals organized in groups.
traffic_signals = [[10, 30, 5],[15, 18, 14],
                   [8, 9, 19],[1, 2, 3]
                   ]
for i in traffic_signals:
    for k in i:
        print(k)