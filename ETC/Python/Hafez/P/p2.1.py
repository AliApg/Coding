MIN = MAX = float(input("Enter 10 numbers\n1: "))
for i in range(2, 11):
    print(i, end='')
    a = float(input(": "))
    if a > MAX:
        MAX = a
    elif a < MIN:
        MIN = a
print("Min =", MIN, "\nMax =", MAX)
