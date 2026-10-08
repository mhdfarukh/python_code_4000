# 16. Write a program using break to stop a loop as soon as a target restaurant bill value is found.
restaurant_bill = [200, 500, 1500, 350, 450]
for i in restaurant_bill:
    if i == 350:
        break
    print(i)
