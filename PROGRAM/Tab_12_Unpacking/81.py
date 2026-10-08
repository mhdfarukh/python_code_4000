# 81. Write a program to unpack nested lists of student records into separate variables.
student_records = [["Roshan", 25, "BCA", "B"],["Rahul", 85, "MCA", "A"]]
(name1 , age1 , course1, gret1),(name2 , age2 , course2, gret2) = student_records

print("Student 1:")
print("Name:",name1)
print("Age:",age1)
print("Course:",course1)
print("Gret:",gret1)

print("STUDENT = 2:")
print("Name:",name2)
print("age:",age2)
print("course:",course2)
print("gret:",gret2)

