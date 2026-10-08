# 45. Write a program to unpack a list of temperature readings to get the first and last value with the middle grouped.
temp_readings = [22, 52, 85, 46, 76, 99]
first_value,*middile_value,Last_value = temp_readings
print("first_value:",first_value)
print("middlie_value:",middile_value)
print("Last_vlaue:",Last_value)