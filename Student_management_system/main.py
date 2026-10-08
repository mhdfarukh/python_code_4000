students = []
print("=============================")
print("STUDENT MANAGEMENT SYSTEM")
print("=============================")

print("1. Add Student")
print("2. View Student")
print("3. Search Student")
print("4. Update Student")
print("5. Delete Student")
print("6. Exit")

print("\n--- Add Student ---")
name = input("Enter Student name:")
roll_no = input("Enter Student Roll Number:")
course = input("Enter Student Course:")
marks = input("Enter Student Marks:")

# print("\nStudent Added Successfully!")
# print("Name:", name)
# print("Roll No:", roll_no)
# print("Course:", course)
# print("Marks:", marks)
student = {
    "name": name,
    "roll_no": roll_no,
    "course": course,
    "Marks": marks
}
students.append(student)
print("\nStudent Added Successfully!")

print("\n--- View Student ---")
for student in students:
    print("Name:",student["name"])
    print("Roll No:",student["roll_no"])
    print("Course:",student["course"])
    print("Marks:",student["Marks"])
    print("-----------------------------------")