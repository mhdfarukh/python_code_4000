# 66. Write a program to swap two movie ratings values using unpacking.
movie1 = [22, 55, 46, 10,]
movie2 = [ 44, 75, 99, 20]
print("Before")
print("movie ratings:",movie1)
print("movie ratings:",movie2)
movie1 ,movie2 = movie2, movie1
print("After")
print("movie ratings:",movie1)
print("movie ratings:",movie2)