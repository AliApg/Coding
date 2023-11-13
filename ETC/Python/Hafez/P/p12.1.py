def ReportList(x):
    if x==cars:
        alter=['License plate','Owner','Entry date','Entry time']+x[:]
        Max=len(alter[1])
        for i in x[1::4]:
            if len(i)>Max:
                Max=len(i)
        for i in range(1,len(alter),4):
            alter[i]=' '*((Max-len(alter[i]))//2)+alter[i]+' '*(Max-len(alter[i])-((Max-len(alter[i]))//2))
            #OR   alter[i]=alter[i].ljust(Max,' ')
        print(' '*((Max+46-27)//2),'CARS  IN  THE  PARKING  LOT','\n ','='*(Max+44),'\n| ',
              alter[0],' | ',alter[1],' | ',alter[2],' | ',alter[3],' |\n ','-'*15,' ','-'*(Max+2),' ','-'*12,' ','-'*12,sep='')
        for i in range(4,len(alter),4):
            print('|  ',alter[i],'  | ',alter[i+1],' | ',alter[i+2],' |  ',alter[i+3],'  |',sep='')
        print('','-'*15,'-'*(Max+2),'-'*12,'-'*12)
    elif x==del_cars:
        alter=['License plate','Owner','Entry date','Entry time','Exit date','Exit time']+x[:]
        Max=len(alter[1])
        for i in x[1::6]:
            if len(i)>Max:
                Max=len(i)
        for i in range(1,len(alter),6):
            alter[i]=' '*((Max-len(alter[i]))//2)+alter[i]+' '*(Max-len(alter[i])-((Max-len(alter[i]))//2))
            #OR   alter[i]=alter[i].ljust(Max,' ')
        print('\n',' '*((Max+71-38)//2),'CARS  THAT  WERE  IN  THE  PARKING  LOT','\n ','='*(Max+69),'\n| ',alter[0],' | ',
              alter[1],' | ',alter[2],' | ',alter[3],' | ',alter[4],'  | ',alter[5],' |\n ','-'*15,' ','-'*(Max+2),(' '+'-'*12)*3,' ','-'*11,sep='')
        for i in range(6,len(alter),6):
            print('|  ',alter[i],'  | ',alter[i+1],' | ',alter[i+2],' |  ',alter[i+3],'  | ',alter[i+4],' | ',alter[i+5],'  |',sep='')
        print('','-'*15,'-'*(Max+2),'-'*12,'-'*12,'-'*12,'-'*11)
#====================================================================================================================================================
cars=[]; del_cars=[]; temp=[]
import re
from os import system
from time import sleep
from datetime import datetime
'''
system('cls')
print('WELCOME TO PARKING LOT PROGRAM\n\n\n          ==== ====\n         |    |    |        \n         |    |    |        \n ======== ====',
    '==== ======== \n|                           |\n|      ***        ***       |\n =====*****======*****======\n       ***        ***\n\n\n')
system('pause')
'''
#     درصورت لازم بودن به حذف اطلاعات گذشته
log=open('p12.1.txt','w')
log.write('\n* PROGRAM LAUNCH *\n')
log.close()
while ('IN' in locals())==False or IN!='5':
        system('cls')
        IN=input('* CAR  PARKING   MENU *\n\n1. Car entry\n2. Car exit\n3. Parking report\n4. Log file report\n5. End program\n\nChoose a number from 1 to 5: ')
        while IN.isdigit()==False or not(0<int(IN)<6):
            IN=input('\n\aWrong input!\nChoose a number from 1 to 4: ')
        system('cls')
        if IN=='1':           #Car entry
            log=open('p12.1.txt','a+')
            if len(cars)==40:
                log.write('\n* CAR ENTRY was selected while parking lot was full!\n')
                print('\aParking lot is full!\n')
                system('pause')
            else:
                log.write('\n* CAR ENTRY was selected successfully\n\n License plate | Entry date | Entry time | Owner\n\n')
                print("An example for a car's license plate number: 00A000 IR00\nEnter 'End' when you're done")
                while len(cars)<40:
                    flag=False
                    lp=input("\nEnter your car's license plate number (car number {}): ".format(len(cars)//4+1))
                    while lp.lower()!='end' and (len(lp)!=11 or lp[2].isalpha()==False or lp[-4:-2].isalpha()==False or lp[0:2].isdigit()==False
                                        or lp[0:2].isdigit()==False or lp[3:6].isdigit()==False or lp[-2:].isdigit()==False or lp[-5]!=' '):
                        lp=input("\n\aInvalid license plate number!\nTry again: ")
                    if lp.lower()=="end":
                        break
                    for i in cars[::4]:
                        if i==lp:
                            print('\n\aThis car already exists in the parking lot!')
                            flag=True
                            break
                    if flag==False:
                        name=input(f"Owner's name (for {lp}): ").strip()
                        while all(i.strip().isalpha() for i in re.split('\ .|\. |\ . |\.|\ ',name))==False:
                            name=input(f"\n\aOwner's name is invalid!\nTry again (for {lp}): ").strip()
                        date=((str(datetime.now())).split(' '))[0]
                        time=((((str(datetime.now())).split('.'))[0]).split(' '))[1]
                        cars+=[lp,name,date,time]
                        log.write(f'  {lp}  | {date} |  {time}  | {name}\n')
            log.close()
        elif IN=='2':           #Car exit
            log=open('p12.1.txt','a+')
            if len(cars)==0:
                log.write('\n* CAR EXIT was selected while parking lot was empty!\n')
                print('\aThe parking lot is empty!\n')
                system('pause')
            else:
                log.write('\n* CAR EXIT was selected successfully\n\n License plate | Entry date | Entry time | Exit date  | Exit time  | Owner\n\n')
                while len(cars)!=0:
                    print('CARS  IN  THE  PARKING  LOT\n===========================')
                    for i in  range(0,len(cars),4):
                        print((i//4)+1,". ",cars[i],sep='')
                    ex=input("===========================\n\nEnter 'End' when you're done\n\nChoose a number from the list above: ")
                    while ex.lower()!='end' and(ex.isdigit()==False or not(0<int(ex)<=len(cars)//4)):
                        ex=input('\n\aWrong input!\nChoose a number from the shown list range: ')
                    if ex.lower()=='end':
                        break
                    #del cars[(int(ex)-1)*4:(int(ex)-1)*4+4]       OR:
                    for i in reversed(range(len(cars)//4)):
                        if cars[i*4]==cars[(int(ex)-1)*4]:
                            date=((str(datetime.now())).split(' '))[0]
                            time=((((str(datetime.now())).split('.'))[0]).split(' '))[1]
                            del_cars+=cars[(int(ex)-1)*4:(int(ex)-1)*4+4]+[date,time]
                            log.write(f'  {cars[(int(ex)-1)*4]}  | {cars[(int(ex)-1)*4+2]} |  {cars[(int(ex)-1)*4+3]}  | {date} |  {time}  | {cars[(int(ex)-1)*4+1]}\n')
                            cars=cars[:i*4]
                            break
                        #temp+=cars[i*4+3:i*4-1:-1]       OR:
                        for i in range(4):
                            temp+=[cars.pop()]
                    #cars+=temp[::-1]      OR:
                    #for i in temp[::-1]:
                    #    cars+=[i]         OR:
                    for i in range(len(temp)):
                        cars+=[temp.pop()]
                    system('cls')
            log.close()
        elif IN=='3': #Parking report
            log=open('p12.1.txt','a+')
            if len(cars)==len(del_cars)==0:
                log.write('\n* PARKING REPORT was selected while there was no customers!\n')
                print('\aThere were no customers!\n')
                system('pause')
            else:
                print()
                log.write('\n* PARKING REPORT was selected successfully\n')
                if len(cars)!=0:
                    ReportList(cars)
                    system('pause')
                if len(del_cars)!=0:
                    system('cls')
                    ReportList(del_cars)
                    system('pause')
                system('cls')
                print(f'\nThere is {10-len(cars)//4} avalaible spots in the parking lot! (number of cars in the parking lot:',
                f'{len(cars)//4})\n\n{len(cars)//4+len(del_cars)//6} cars have entered the parking lot and {len(del_cars)//6} cars have left the parking lot.\n')
                log.write(f'\n  There was {10-len(cars)//4} avalaible spots in the parking lot! (number of cars in the parking lot: '
                +f'{len(cars)//4})\n  Parking lot condition: {len(cars)//4+len(del_cars)//6} cars have entered and {len(del_cars)//6} cars have left the parking lot.\n')
                system('pause')
            log.close()
        elif IN=='4':      #Log file
            log=open('p12.1.txt','a+')
            log.write('\n* LOG FILE was selected\n\n')
            log.seek(0)
            car_dict={}
            ALL=log.read().split('\n')
            for i in ALL:
                if i.lstrip()[:2].isdigit()==True:
                    if (i.lstrip()[:11] in car_dict.keys())==True:
                        car_dict[i.lstrip()[:11]]+=1
                    else:
                        car_dict[i.lstrip()[:11]]=1
            for i in car_dict:
                log.write(f'  License plate: {i} => Entry: {car_dict[i]-(car_dict[i]//2)}   Exit: {car_dict[i]//2}\n')
            log.seek(0)
            print('CURRENT LOG FILE:\n',log.read(),sep='')
            system('pause')
log=open('p12.1.txt','a+')
log.write('\n* The parking lot was closed!\n\n')
log.close()
print('\nThe car parking program has been ended!\n')
sleep(1.5)
