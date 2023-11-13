t=('a',10,'b',20,'c',30,'d',40,'e',50)
u=[]
j=s=0
x=''
for i in range(0,len(t),2):
    print('item:',t[i],'\tcost:',t[i+1])
print('\nEnter the items you want to purches\n')
while x!='End':
    x=input('Item {}: '.format(j+1))
    if x!='End':
        for y in range(0,len(t),2):
            if x==t[y]:
                cost=t[y+1]
                y=-1
                break
        if y!=-1:
            print('This item is not in the list!')
            continue
    u.append(x)
    s+=cost
    cost=0
    j+=1
del u[-1]
print('\nTotal cost of your purcheses is: ',s,'\n\nitems you purchesed:\n',u,sep='')
    
