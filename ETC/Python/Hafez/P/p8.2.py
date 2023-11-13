def sub(x,y):
    for i in range(1,x+1):
        if x%i==0:
            y.add(i)
a_sub=set()
b_sub=set()
a=int(input('Enter first number: '))
while a<=0:
    if a==0:
        a=int(input('\7Number cannot be 0!\nEnter first number again: '))
    else:
        print(a,'is negative so insted we use',-a)
        a*=-1
        break
b=int(input('\nEnter second number: '))
while b<=0:
    if b==0:
        b=int(input('\7Number cannot be 0!\nEnter second number again: '))
    else:
        print(b,'is negative so insted we use',-b)
        b*=-1
        break
#======================================================
from os import *
sub(a,a_sub)
sub(b,b_sub)
gmd=max(a_sub.intersection(b_sub))
system('cls')
print(a,' divisors: ',a_sub,'\n',b,' divisors: ',b_sub,'\n\nGreatest common divisor: '
      ,gmd,'\nLeast common multiple: ',(a*b)//gmd,'\n',sep='')
system("pause")
