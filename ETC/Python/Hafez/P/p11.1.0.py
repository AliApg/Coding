def ReportList(x):
    if x==cars:
        alter=['License plate','Owner','Entry date','Entry time']+cars[:]
        Max=len(alter[1])
        for i in x[1::4]:
            if len(i)>Max:
                Max=len(i)
        for i in range(1,len(alter),4):
            alter[i]=' '*((Max-len(alter[i]))//2)+alter[i]+' '*(Max-len(alter[i])-((Max-len(alter[i]))//2))
            #OR   alter[i]=alter[i].ljust(Max,' ')
        print(' '*((Max+15)//2),'CARS  IN  THE  PARKING  LOT',' '*(Max+15-((Max+15)//2)),
              '\n','='*(Max+43),'\n',alter[0],' | ',alter[1],' | ',alter[2],' | ',alter[3],'\n','-'*(Max+43),sep='')
        for i in range(4,len(alter),4):
            print(' ',alter[i],'  | ',alter[i+1],' | ',alter[i+2],' |  ',alter[i+3],sep='')
        print('-'*(Max+43))
    elif x==del_cars:
        alter=['License plate','Owner','Entry date','Entry time','Exit date','Exit time']+del_cars[:]
        Max=len(alter[1])
        for i in x[1::6]:
            if len(i)>Max:
                Max=len(i)
        for i in range(1,len(alter),6):
            alter[i]=' '*((Max-len(alter[i]))//2)+alter[i]+' '*(Max-len(alter[i])-((Max-len(alter[i]))//2))
            #OR   alter[i]=alter[i].ljust(Max,' ')
        print(' \n'*((Max+26)//2),'CARS  THAT  WERE  IN  THE  PARKING  LOT',' '*(Max+26-((Max+26)//2)),'\n',
              '='*(Max+68),'\n',alter[0],' | ',alter[1],' | ',alter[2],' | ',alter[3],' | ',alter[4],'  | ',alter[5],'\n','-'*(Max+68),sep='')
        for i in range(6,len(alter),6):
            print(' ',alter[i],'  | ',alter[i+1],' | ',alter[i+2],' |  ',alter[i+3],'  | ',alter[i+4],' | ',alter[i+5],sep='')
        print('-'*(Max+68))
#=======================================================================================================
cars=[];del_cars=[]
from os import system
from datetime import datetime
while ('IN' in locals())==False or IN!='4':
    system('cls')
    IN=input('**CAR  PARKING   MENU**\n\n1. Car entry\n2. Car exit\n3. Parking report\n4. End program\n\nChoose a number from 1 to 4: ')
    while IN.isdigit()==False or not(0<int(IN)<5):
        IN=input('\aWrong input!\nChoose a number from 1 to 4: ')
    system('cls')
    if IN=='1':           #Car entry
        if len(cars)==40:
            print('\aParking lot is full!\n')
            system('pause')
        else:
            print("An example for a car's license plate number: 00A000 IR00\nEnter 'End' when you're done")
            while len(cars)<40:
                flag=False
                lp=input("\nEnter your car's license plate number (car number {}): ".format(len(cars)//4+1))
                while lp!='End' and (len(lp)!=11 or lp[2].isalpha()==False or lp[-4:-2].isalpha()==False or lp[0:2].isdigit()==False
                                     or lp[0:2].isdigit()==False or lp[3:6].isdigit()==False or lp[-2:].isdigit()==False or lp[-5]!=' '):
                    lp=input("\aInvalid license plate number!\nTry again: ")
                if lp=="End":
                    break
                for i in cars[::4]:
                    if i==lp:
                        print('\n\aThis car already exists in the parking lot!')
                        flag=True
                        break
                if flag==False:
                    name=input("Owner's name (for {}): ".format(lp))
                    cars+=[lp,name,((((str(datetime.now())).split('.'))[0]).split(' '))[0],((((str(datetime.now())).split('.'))[0]).split(' '))[1]]
    elif IN=='2':           #Car exit
        if len(cars)==0:
            print('\aThe parking lot is empty!\n')
            system('pause')
        else:
            while len(cars)!=0:
                print('CARS  IN  THE  PARKING  LOT\n=========================')
                for i in  range(0,len(cars),4):
                    print((i//4)+1,". ",cars[i],sep='')
                ex=input("=========================\n\nEnter 'End' when you're done\n\nChoose a number from the list above: ")
                while ex!='End' and(ex.isdigit()==False or not(0<int(ex)<=len(cars)//4)):
                    ex=input('\aWrong input!\nChoose a number from the shown list range: ')
                if ex=='End':
                    break
                del_cars+=cars[(int(ex)-1)*4:(int(ex)-1)*4+4]+[((((str(datetime.now())).split('.'))[0]).split(' '))[0],((((str(datetime.now())).split('.'))[0]).split(' '))[1]]
                del cars[(int(ex)-1)*4:(int(ex)-1)*4+4]
                system('cls')
    elif IN=='3': #Parking report
        if len(cars)==len(del_cars)==0:
            print('\aThere were no customers!\n')
            system('pause')
        else:
            print()
            if len(cars)!=0:
                ReportList(cars)
            if len(del_cars)!=0:
                ReportList(del_cars)
        system('pause')
print('The car parking program has been ended!\n')
system('pause')
