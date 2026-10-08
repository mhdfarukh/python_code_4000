# 27. Write a program to unpack a list of cricket scores using a star expression to capture the rest.
cricket_score = [12, 15, 25, 55, 94, 102]
score1, score2, *score3 = cricket_score
print("Score:",score1)
print("Score:",score2)
print("Score:",score3)