# 71. Write a program to swap two exam results values using unpacking.
def swep():
    exam1 = [85, 74, 96]
    exam2 = [41, 52, 63, 98]
    print("Before")
    print("exam results1:",exam1)
    print("exam results2:",exam2)

    exam1 ,exam2 = exam2 ,exam1

    print("After")
    print("exam results1:",exam1)
    print("exam results2:",exam2)
swep()