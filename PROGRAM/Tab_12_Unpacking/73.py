# 73. Write a program to swap two stock prices values using unpacking.
stock1 = [2000, 3500, 4500, 1500]
stock2 = [8000, 7500, 6450, 120]
print("Before")
print("stock prices:",stock1)
print("stock prices:",stock2)

stock1, stock2 = stock2, stock1
print("After")
print("stock prices:",stock1)
print("stock prices:",stock2)