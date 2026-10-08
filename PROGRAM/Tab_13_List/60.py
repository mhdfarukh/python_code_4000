# 60. Write a program to loop through a nested list of delivery addresses using nested for loops.
delivery_addresses = [["Taj mahal","Dharmapuri,forest colony"],
                      ["Qutub minar","kalka Das Mag, mehrauli Delhi"]
                      ]
for i in delivery_addresses:
    for addresses in i:
        print(addresses)