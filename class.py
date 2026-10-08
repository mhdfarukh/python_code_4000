# n = 2456
# count = 0
# while n>0:
#      n = n// 10
#      count = count + 1
# print(count)

n = 121
chack = n
rev = 0
while n>0:
    rem = n%10
    rev = rev * 10+rem
    n = n//10
if rev ==chack:
    print("plordum")
else:
    print("not plordum")