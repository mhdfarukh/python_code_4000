# 47. Write a program to unpack a list of cricket scores to get the first and last value with the middle grouped.
cricket_score = [22, 45, 94, 85, 120, 159, 456]
first_value, *middile_value, last_value = cricket_score
print("first_value:",first_value)
print("Middile_value:",middile_value)
print("Last_value:",last_value)
