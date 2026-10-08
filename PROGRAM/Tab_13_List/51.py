# 51. Write a program to loop through a nested list of exam results using nested for loops.
exam_results = [[85, 45, 65, 32],[99, 75, 58, 66],
                [88, 55, 22, 37],[69, 67, 82]
                ]
for i in exam_results:
    for exam in i:
        print(exam)