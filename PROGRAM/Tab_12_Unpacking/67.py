# 67. Write a program to swap two cricket scores values using unpacking.
Score1 = [22, 55, 46, 10, 13]
score2 = [88, 44, 75, 99, 20]
print("Before")
print("cricket_score:",Score1)
print("cricket_score:",score2)
Score1 ,Score2 = score2, Score1
print("After")
print("cricket_score:",Score1)
print("cricket_score:",Score2)