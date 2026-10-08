# 29. Write a program to create a dictionary of electricity bills using curly braces with key-value pairs.
electricity_bill = {"bill1": 3500,
                    "bill2": 4500,
                    "bill3": 5000
                    }
for key , value in electricity_bill.items():
    print(key, value)