while True:
    s=float(input("Enter your raw salary: "))
    if s<0:
        print("Your salary cannot be anegetive number!")
        continue
    break
sf=s
while True:
    a=float(input("Enter your age: "))
    if a<15:
        print("Your age must be 15 or above!")
        continue
    break
while True:
    e=float(input("Enter your work experence: "))
    if e+15>a:
        print("Yor experience cannot be greater than your age -15!")
        continue
    break
if a>=57 and e>25:
    sf*=1.25
elif a>=47 and e>20:
    sf*=1.2
elif a>=37 and e>15:
    sf*=1.15
elif a>=27 and e>10:
    sf*=1.1
print("Your final salary is",sf)
