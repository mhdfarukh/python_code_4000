# 72. Write a program to swap two social media followers values using unpacking.
followers1 = [58, 47, 69, 98]
followers2 = [24, 27, 73, 96, 100]
print("Before")
print("social media followers:",followers1)
print("social media followers:",followers2)

followers1, followers2 = followers2, followers1

print("After")
print("social media followers:",followers1)
print("social media followers:",followers2)