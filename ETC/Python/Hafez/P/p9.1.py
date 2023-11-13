class game:
    def __init__(self,n):
        self.name=n.strip()
        self.TF=[]
    def guess(a,b,c,l,u):   #(obj1   ,   obj2   ,   Number of gusses for each obj   ,   Start number   ,   End number)
        system('cls')
        game.Num=c
        if randint(1,2)==2:
            d=a; a=b; b=d
        print("CHOOSE A NUMBER FROM '",l,"' TO '",u,"'\n",a.name,' WILL START THE GAME!',sep='')
        j=[a,b]*c
        for i in j:
            print()
            x=input("{}'s guess number {}: ".format(i.name,len(i.TF)//3+1))
            while x.isdigit()==False or int(x)<l or int(x)>u:
                x=input("\n\aWrong input! Your guess must be from {} to {}.\nTry again ({}'s guess number {}): ".format(l,u,i.name,len(i.TF)//3+1))
            i.TF+=[int(x),randint(l,u)]
            if int(x)==i.TF[-1]:
                i.TF.append('Right')
                continue
            i.TF.append('Wrong')
    def result(a,b):
        x=a.TF.count('Right')
        y=b.TF.count('Right')
        system('cls')
        if x>y:
            z=(a.name,'won with',x,'currect guesses!')
        elif x<y:
            z=(b.name,'won with',y,'currect guesses!')
        else:
            z=('It was a draw between',a.name,'and',b.name,'with',x,'currect guesses for each player!')
        z=((str(z)[1:-1]).replace("'",'')).replace(',','')
        print('\n','='*((len(z)-6)//2),'Winner','='*(len(z)-6-((len(z)-6)//2)),'\n\n',z,'\n\n','='*len(z),sep='',end='\n\n')
        system('pause')
        system('cls')
        z=max(len(a.name),len(b.name))
        print('\n','='*((z//2)+14),'Results','='*(z+13-(z//2)),sep='')
        for i in [a,b]:
            print('\n',i.name,' guesses (',i.TF.count('Right'),' currect/ ',game.Num-i.TF.count('Right'),' incorrect):\n',sep='')
            for j in range(0,len(i.TF),3):
                print('Guess number {}:  {}  ({}: {})'.format(j//3+1,i.TF[j],i.TF[j+2],i.TF[j+1]))
#===================================================================================================
from os import *
from random import randint
player1=game(input("*GUESSING GAME*\n\nFirst player's name: "))
player2=game(input("Second player's name: "))
game.guess(player1,player2,5,1,5)
game.result(player1,player2)
print()
system("pause")
