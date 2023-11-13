storage={}
i=0
while i<5:
    name=input('Enter item {} name: '.format(i+1))
    avl=float(input('Enter availability of {}: '.format(name)))
    if avl<0:
        avl=float(input('Availability can not be negetive!\nEnter availability of {}: '.format(name)))
        continue
    storage[name]=avl
    i+=1
for j in storage:
    if storage[j]<=5:
        print(storage[j],'is low please order!')
