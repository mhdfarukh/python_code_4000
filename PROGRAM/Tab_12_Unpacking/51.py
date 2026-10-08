# 51. Write a program to unpack a list of exam results to get the first and last value with the middle grouped.
exam_results = [85, 84, 96, 71, 82, 93]
first_value,*middile_value,last_value =exam_results
print("first_value:",first_value)
print("Middile_value:",middile_value)
print("Last_value:",last_value)