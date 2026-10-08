# 87. Write a program using continue to skip negative cricket score values in a list and process only positives.
cricket_score = [25, 46, -45, 46, 89, -97, -55]
for i in cricket_score:
    if i < 0:
        continue
    print("positives:",i)