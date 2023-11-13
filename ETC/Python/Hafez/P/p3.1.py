n=int(input("Enter a number: "))
while True:
    print("\nMenu:\n\na)Number of digits\nb)Reverse\nc)Divisors of this number (<=20)\nd)Sum of divisors\ne)New number\nf)Exit program\n")
    x=input("\nYour choice: ")
    if x=='a' or x=='b':
        an=n
        c=r=0
        while an>0:
            r*=10
            r+=an%10
            an//=10
            c+=1
        if x=='a':
            print("\n",n," has ",c," digits",sep='')
        else:
            print("\nReverse of ",n," is ",r,sep='')
    elif x=='c':
        print("\nNumber",n,"divisors are: ")
        for i in range(1,21):
            if n%i==0:
                print(i,"\t",end='',sep='')
        print()
    elif x=='d':
        print("\nSum of",n,"divisors is ",end='')
        c=0
        for i in range(1,21):
            if n%i==0:
                c+=i
        print(c)
    elif x=='e':
        n=int(input("\nEnter a new number: "))
    elif x=='f':
        print("\nThe end...")
        break
