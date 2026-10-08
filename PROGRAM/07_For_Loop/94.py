# 94. Write a program using a for loop to count how many water tank level values satisfy a condition.
weter_tank = [1000, 1500, 200, 500]
count_weter = 0
for i in weter_tank:
    if i >= 1000:
        count_weter += 1
print(count_weter)
