def div(x):
    if x==0:
        return 0
    elif x<0:
        x*=-1
    c=x+1
    for i in range(2,x):
        if x%i==0:
            c+=i
    return c
#Test:
print(div(-10))
def fact(x):
    if x==0:
        return 1
    elif x<0:
        print("Wrong input! (negetive number)")
    else:
        return x*fact(x-1)
#Test:
print(fact(5))
