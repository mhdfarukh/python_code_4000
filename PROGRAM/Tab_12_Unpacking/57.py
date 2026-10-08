# 57. Write a program to unpack a list of game scores to get the first and last value with the middle grouped.
game_score = [500, 200, 150, 420, 546]
first, *middile, last = game_score
print("first_value:",first)
print("Middile_value:",middile)
print("Last_value:",last)