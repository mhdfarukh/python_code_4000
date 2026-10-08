# 42. Write a program to unpack a list of employee data to get the first and last value with the middle grouped.
employee_data = ["Rahul", 25000, "Bank", "Bouliya"]
fist_value,*middil_value,last_value = employee_data
print("fist_value:",fist_value)
print("middli_value:",middil_value)
print("last_value:",last_value)
