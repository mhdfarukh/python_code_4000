# 31. Write a program to unpack a list of exam results using a star expression to capture the rest.
exma_results = [22, 25, 54, 85, 65, 98]
results1, *results2 =exma_results
print("exam_results:",results1)
print("exam_results:",results2)