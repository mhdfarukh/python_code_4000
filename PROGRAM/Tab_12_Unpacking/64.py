# 64. Write a program to swap two bank transactions values using unpacking.
transactions1 = [200, 5000, 4000, 6000]
transactions2 = [700, 8000, 400, 500]
print("Before")
print("transactions1:",transactions1)
print("transactions2:",transactions2)
transactions1 , transactions2 =  transactions2, transactions1
print("After")
print("transactions1:",transactions1)
print("transactions2:",transactions2)