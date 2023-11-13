a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
    a=a+b
    b=a-b
    a=a-b
if a%2!=0:
    a+=1
for i in range(a,b,2):
    print(i)
