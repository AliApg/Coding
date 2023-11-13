def mult(x,y):
    if y==0:
        return 0
    elif y==1:
        return x
    elif y<0:
        return -mult(x,-y)
    else:
        return x+mult(x,y-1)
#Test:
print(mult(-5,-5))
