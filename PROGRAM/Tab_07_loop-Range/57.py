# 57. Write a program using range(start, stop, step) to print every alternate game high score value.
start_score = 10
stop_score = 500
step_score = 60
for i in range(start_score, stop_score, step_score):
    print("game high score:", i)