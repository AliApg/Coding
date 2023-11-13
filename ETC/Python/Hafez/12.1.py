n=5;  front=rear=0;  qu=[]
def insert(x):
    global rear
    global n
    if rear==n:
        print('Full')
    else:
        qu.append(x)
        rear+=1
def remove():
    global front
    global n
    if qu.count(None)==n/2 or len(qu)==0:
        print('Empty')
    else:
        qu[front]=None
        front+=1
        n+=1
#================================
remove()
for i in range(6):
    insert(i+1)
for j in range(7):
    remove()
insert(3)
insert(3)
insert(3)
