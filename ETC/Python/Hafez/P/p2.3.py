og=ou=f=p=c=j=1;b=[]
print("For 5 students:\n")
for i in range(1,6):
    gr=un=0
    a=[]
    n=int(input("Enter number of student {} grades: ".format(i)))
    while j<=n:
        g=float(input("Grade {}: ".format(j)))
        if g>20 or g<0:
            print("Grades must be between 0 & 20!")
            continue
        j+=1
        u=int(input("Unit of grade {}: ".format(j)))
        gr+=g*u
        un+=u
    a.append(gr/un)
    a.append(un)
    b.append(a)
    og+=gr/un
    ou+=un
    print()
for i in range(0,5):
    print("Grade point average of student",i+1,"with",b[i][1],"unites is",b[i][0],end='')
    if b[i][0]<10:
        print(" ==> Fail")
        f+=1
    elif b[i][0]>=12:
        print(" ==> Pass")
        p+=1
    else:
        print(" ==> Conditioned")
        c+=1
print("\nOverall GPA of these 5 students with",ou,"units is",og/5,"\nThere is",p,"pass,",f,"fail and",c,"conditioned")
