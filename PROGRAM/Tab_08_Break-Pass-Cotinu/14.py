# 14. Write a program using break to stop a loop as soon as a target water tank level value is found.
weter_tank = [500, 1500, 1000, 150, 50, 25]
for i in weter_tank:
    if i == 150:
        break
    print(i)