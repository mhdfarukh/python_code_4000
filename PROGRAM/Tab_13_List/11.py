# 11. Write a program to create a nested list representing exam results organized in groups.
exam_results = [
    [[14, 25, 36,],[85, 74, 94]],
    [[90, 76, 82, 71],[37, 38, 39]]
]
for i in exam_results:
    for j in i:
        for h in j:
         print(h)