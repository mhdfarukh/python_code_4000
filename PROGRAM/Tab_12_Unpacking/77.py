# 77. Write a program to swap two game scores values using unpacking.
score1 = [220, 450, 48, 98]
score2 = [200, 300, 150]
print("Before")
print(" game scores:",score1)
print(" game scores:",score2)

score1, score2 = score2, score1

print("After")
print(" game scores:",score1)
print(" game scores:",score2)