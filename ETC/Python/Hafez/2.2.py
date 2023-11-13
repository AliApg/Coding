name=input("Username: ")
pas=int(input("Password"))
if name=="Amirata" and pas==123456:
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    print(a,"+",b,"=",a+b)
    print(a,"-",b,"=",a-b)
    print(a,"*",b,"=",a*b)
    print(a,"/",b,"=",a/b)
else:
    print("Wrong username or password")
