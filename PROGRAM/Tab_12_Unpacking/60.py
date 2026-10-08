# 60. Write a program to unpack a list of user ages to get the first and last value with the middle grouped.
user_age = [55, 94, 66, 35, 19, 35]
first, *middile, last = user_age
print("first_value:",first)
print("Middile_value:",middile)
print("Last_value:",last)