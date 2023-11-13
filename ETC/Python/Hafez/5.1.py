def charnum(x,y):
    c=0
    for i in x:
        if y==i:
            c+=1
    return c
def charloc(x,y):
    for i in range(0,len(x)):
        if y==x[i]:
            print(i+1,end=' ')
    return ''
a=input("Enter a string: ")
b=input("Enter a character: ")
print(b,"has been repeated",charnum(a,b),"times")
print(b,"was located in:")
print(charloc(a,b))
