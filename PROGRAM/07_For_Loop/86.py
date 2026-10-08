# 86. Write a program using a for loop to count how many movie rating values satisfy a condition.
movie_rating = [99, 87, 42, 49, 68]
count_rating = 0
for i in movie_rating:
    if i >= 50:
        count_rating += 1
print(count_rating)