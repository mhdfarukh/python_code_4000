# 85. Write a program to unpack nested lists of temperature readings into separate variables.
temp_reading = ["monday", 40],["suanday", 35]
(day1,temp1),(day2,temp2) = temp_reading
print("TEMP_READING = 1")
print("Day1:",day1)
print("Temperature:",temp1)

print("TEMP_READING = 2")
print("Day2:",day2)
print("Temperature2:",temp2)