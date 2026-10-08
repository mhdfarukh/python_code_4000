# 25. Write a program to unpack a list of temperature readings using a star expression to capture the rest.
temp_reading = [22, 12, 16, 15, 45]
reading1, *reading2, reading3 = temp_reading
print("Reading:", reading1)
print("Reading:",reading2)
print("Reading:",reading3)