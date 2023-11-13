class game:
    def __init__(self,n):
        self.name=n
        self.TF=[]
    def guss(a,b):
        j=[a,b]
        j*=5
        for i in j:
            x=-1
            print()
            while x<=0 or x>10:
                x=int(input("{}'s guss number {}: ".format(i.name,len(i.TF)+1)))
            if x==randint(1,10):
                i.TF.append('Right')
            else:
                i.TF.append('Wrong')
    def result(a,b):
        x=a.TF.count('Right')
        y=b.TF.count('Right')
        print('\n==============Winner==============\n')
        if x>y:
            print(a.name,'won with',x,'currect gusses!\n\n==============Results==============')
        elif x<y:
            print(b.name,'won with',y,'currect gusses!\n\n==============Results==============')
        else:
            print('It was a draw between',a.name,'and',b.name,'with',x,'currect gusses for each player!\n\n==============Results==============')
        print(a.name,' gusses (',x,' currect/ ',5-x,' incorrect):\n',a.TF,'\n\n',b.name,' gusses (',y,' currect/ ',5-y,' incorrect):\n',b.TF,sep='')
from random import *
player1=game(input("*GUSSING GAME*\n\nFirst player's name: "))
player2=game(input("Second player's name: "))
print("\nCHOOSE A NUMBER FROM '1' TO '10'")
if randint(1,2)==1:
    print(player1.name,'WILL START THE GAME!')
    game.guss(player1,player2)
else:
    print(player2.name,'WILL START THE GAME!')
    game.guss(player2,player1)
game.result(player1,player2)
