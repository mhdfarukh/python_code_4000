# 25. Write a program to create a dictionary of temperature readings using curly braces with key-value pairs.
temp_reading = {"reading1": 25.0,
                "reading2": 55.0,
                "reading3": 65.4,
                "reading4": 75.0
                }
for key , value in temp_reading.items():
    print(key, value)