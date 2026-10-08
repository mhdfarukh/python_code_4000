# 41. Write a program to unpack a list of student records to get the first and last value with the middle grouped.
student_records = ["Roshan",21450,"Pharma",25, "A+"]
fist_value, *middle_value, last_value = student_records
print("fist_value:",fist_value)
print("middile_value:",middle_value)
print("last_value:",last_value)
