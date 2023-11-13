def divsum(x,y):
    if x<0:
        x*=-1
    elif x==0:
        return 0.0
    c=y//x
    return x*((1+c)*c)/2
import os
print(((open("Yo.txt","rt")).read()).format(divsum(3,1000)+divsum(5,1000)-divsum(15,1000)))
os.system('pause')
