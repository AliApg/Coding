import math
print("We have: ax^2+bx+c")
a=float(input("Enter the value of 'a': "))
b=float(input("Enter the value of 'b': "))
c=float(input("Enter the value of 'c': "))
if a!=0:
    d=b**2-4*a*c
    if d>=0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print("x=",x1,end='')
        if x1!=x2:
            print("   OR   x=",x2)
    else:
        print("Equation (",a,"x^2+",b,"x+",c,") does not have an answer!(delta<0)",sep='')
elif b!=0:
    x=-c/b
    print("x=",x,end='')
else:
    print("Equation (",a,"x^2+",b,"x+",c,") does not have an answer!(a=b=0)",sep='')