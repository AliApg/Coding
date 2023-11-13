def fact(x):
    y=1
    while x>1:
        y*=x
        x-=1
    return y
a=int(input("Enter a number: "))
if a>0:
    print("Ans=",fact(a))
elif a==0:
    print("Ans= 1")
else:
    print("Wrong input! (Negetive number)")