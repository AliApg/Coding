#---------------------------------With list---------------------------------
def rep(a):
    c=[0]
    c[0]=a[0]
    a[0]=a[1]
    a[1]=c[0]
x=[]
x.append(input('Enter first variable: '))
x.append(input('Enter second variable: '))
rep(x)
print('\nyour input\nx= ',(type(x[1]))(x[1]),'\ty= ',(type(x[0]))(x[0]),
      '\n\nResult\nx= ',(type(x[0]))(x[0]),'\ty= ',(type(x[1]))(x[1]),sep='')
#---------------------------------With tuple---------------------------------
def rept(a):
    c=(a[1],a[0])
    return c
x=[]
x.append(input('Enter first variable: '))
x.append(input('Enter second variable: '))
print(rept(x))
