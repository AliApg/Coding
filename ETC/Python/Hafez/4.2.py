def num():
    c=1
    global x
    x=float(input("1: "))
    while x!=0:
        x=float(input("{}: ".format(c+1)))
        c+=1
    print("\nThere are ",c-1," numbers in total\n",sep='')
    return c-1
def get():
    global x
    for i in range(1,x+1):
        y=float(input("{}: ".format(i)))
#def sum():
num()
get()
