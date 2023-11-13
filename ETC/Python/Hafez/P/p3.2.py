def om(x,y):
    c=0
    for i in range(0,y):
        c+=a[i]
    return c/y
s=int(input("Enter number of students: "))
a=[]
for i in range(1,s+1):
    j=g=0
    print("\nStudent",i)
    while j<5:
        gr=float(input("Grade {}: ".format(j+1)))
        if gr<0 or gr>20:
            print("Grades must be between 0 & 20")
            continue
        g+=gr
        j+=1
    a.append(g/5)
for i in range(0,s):
    print("\nStudent",i+1,"GPA is",a[i],end='')
print("\n\nOverall GPA for these",s,"students is",om(a,s))
