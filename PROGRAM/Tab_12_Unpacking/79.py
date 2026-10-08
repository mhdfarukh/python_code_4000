# 79. Write a program to swap two user ages values using unpacking.
user1 = [25, 24, 34, 67,]
user2 = [12, 15, 18]
print("Before")
print("user ages:",user1)
print("user ages:",user2)

user1, user2 = user2, user1

print("After")
print("user ages:",user1)
print("user ages:",user2)