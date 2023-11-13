cstmr=[None]*20;counter=0;L=-1
from random import *
from os import *
print("Enter 'END' when you're done")
while counter!=10:
    flag=False
    ID=input('\nEnter your ID number (Number of available spots: {}): '.format(10-counter))
    while ID.upper()!='END' and(ID.isdigit()==False or len(ID)!=10):
        ID=input('\n\aWrong ID number (ID number must be a 10 digit number)!\nTry again: ')
    if ID.upper()=='END':
        break
    for i in cstmr[1::2]:
        if i==ID:
            flag=True
            break
    if flag==True:
        print('\n\aThis ID already exists!')
        continue
    name=input(f'Enter your name (ID {ID}): ').strip()
    while name=='':
        name=input(f'\n\aName cannot beempty!\nTry again (ID {ID}): ').strip()
    counter+=1
    if L==9:
        '''for j in reversed(range(len(cstmr))):
            if cstmr[j]!=None:
                cstmr=([None]*(20-len(cstmr[:j+1])))+cstmr[:j+1]
                L=(len(cstmr[:j+1])//2)+1'''
        while None in cstmr:
            cstmr.remove(None)
        L=(len(cstmr)//2)-1
        cstmr=([None]*(20-len(cstmr)))+cstmr
    L=randint(L+1,9)
    cstmr[(-L*2)+18:(-L*2)+20]=[name,ID]
system('cls')
print('*COSTUMERS IN THE THEATER*\n' )
for i in reversed(range(0,len(cstmr),2)):
    if cstmr[i]!=None:
        print(f'{(-i+20)//2}. {cstmr[i+1]} => {cstmr[i]}')
print()
system('pause')