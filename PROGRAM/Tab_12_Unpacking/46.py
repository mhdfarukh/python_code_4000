# 46. Write a program to unpack a list of movie ratings to get the first and last value with the middle grouped.
movie_ratings = [22, 54, 5, 6, 3, 55]
first_value,*middlie_value,last_value = movie_ratings
print("first_vlaue:",first_value)
print("middile_value:",middlie_value)
print("Last_vlaue:",last_value)