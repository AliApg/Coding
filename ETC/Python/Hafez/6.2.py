l=[]
for i in range(0,10):
    l.append(int(input('Enter number {}: '.format(i+1))))
for j in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i]+=l[i+1]
            l[i+1]=l[i]-l[i+1]
            l[i]-=l[i+1]
print("Your sorted numbers:\n",l,sep='')



