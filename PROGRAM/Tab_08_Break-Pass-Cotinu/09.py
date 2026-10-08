# 09. Write a program using break to stop a loop as soon as a target electricity bill value is found.
electricity_bill = [200, 2500, 4500, 1560, 1505, 4220]
for i in electricity_bill:
    if i == 1560:
        break
    print(i)