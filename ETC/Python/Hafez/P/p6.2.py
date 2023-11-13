ns=int(input('Enter number of students: '))
print()
sn=[]
sm=[]
A=[]
B=[]
C=[]
for i in range(ns):
    sn.append(input('Suudent {} name: '.format(i+1)))
print()
j=0
while j<ns:
    mean=float(input("Enter {}'s GPA: ".format(sn[j])))
    if mean<10 or mean>20:
        print('GPA can not be lower than 10 or greater than 20!')
        continue
    j+=1
    sm.append(mean)
for i in range(ns):
    if sm[i]<15:
        C.append(sn[i])
    elif sm[i]>=17:
        A.append(sn[i])
    else:
        B.append(sn[i])
print('\nExelent GPA(20-17):',A,'\nAvrage GPA(17-15):',B,'\nLow GPA(15-10):',C,sep='\n')
