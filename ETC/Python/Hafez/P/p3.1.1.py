def a(x):
    c=0
    while x>0:
        x//=10
        c+=1
    return c
def b(x):
    r=0
    while x>0:
        r*=10
        r+=x%10
        x//=10
    return r
def c(x):
    for i in range(1,21):
        if x%i==0:
            print(i,"\t",end='',sep='')
    return 0
def d(x):
    c=0
    for i in range(1,21):
        if x%i==0:
            c+=i
    return c
S=0
n=int(input("Enter a number: "))
if n<0:
    n*=-1
    S=1
while True:
    print("\nMenu:\n\na)Number of digits\nb)Reverse\nc)Divisors of this number (<=20)\nd)Sum of divisors\ne)New number\nf)Exit program\n")
    x=input("\nYour choice: ")
    if x=='a':
        if S==1:
            print("-",end='')
        print(n," has ",a(n)," digits",sep='')
    elif x=='b':
        print("\nReverse of ",end='')
        if S==1:
            print("-",end='')
        print(n,"is ",end='')
        if S==1:
            print("-",end='')
        print(b(n))
    elif x=='c':
        print("\nNumber",n,"divisors are: ")
        c(n)
        print()
    elif x=='d':
        print("\nSum of",n,"divisors is ",d(n))
    elif x=='e':
        S=0
        n=int(input("\nEnter a new number: "))
        if n<0:
            n*=-1
            S=1
    elif x=='f':
        print("\nThe end...")
        if S==1:
            n*=-1
        break
