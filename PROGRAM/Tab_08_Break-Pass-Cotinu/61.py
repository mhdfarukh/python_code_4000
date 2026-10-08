# 61. Write a program using break inside a nested loop while searching for a student marks value.
student_marks =[75, 85, 90, 45]
num_marks = 90 # ye vo number hai jo dundna h.
track = False
for marks in student_marks:
    if marks == num_marks:
      track = True
      print("found:",marks)
      break
if track == False:
   print("not found:")