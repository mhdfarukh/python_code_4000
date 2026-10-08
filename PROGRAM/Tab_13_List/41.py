# 41 .Write a program to loop through a nested list of student records using nested for loops.
students_recordes = [["Rohan",45, "Science"],["Sohan",16, "Math"],
                     ["Amaan", 95, "Hindi"],["Shail", 50, "English"]
                     ]
for students in students_recordes:
    
        name = students [0]
        Age = students [1]
        Subject = students [2]
        print(name, Age ,Subject)
