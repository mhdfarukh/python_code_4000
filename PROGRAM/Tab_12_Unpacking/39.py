# 39. Write a program to unpack a list of user ages using a star expression to capture the rest.
user_age = [15, 18, 22, 23, 24, 55]
age1,*age2 = user_age
print("user_age:",age1)
print("user_age:",age2)