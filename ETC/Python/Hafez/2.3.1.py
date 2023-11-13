a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    a=a+b
    b=a-b
    a=a-b
for i in range(a,b,2):
    if a%2!=0:
        i+=1
    else:
        print(i)
