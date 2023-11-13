from datetime import *
car_list=[]
dep_cars=[]
def reports(x):
    for i in x:
        for j in reversed(i):
            print("| ",j," ",sep="",end="")
        print()
    print()
while(1):
    action=input("\nParking Lot MENU\n1.Entrance\n2.Departure\n3.Report\n0.Exit\n\nWhat do you want to do? ")
    if action=="1":
        if len(car_list)==10:
            print("Parking lot is Full!")
        else:
            while len(car_list)!=10:
                flag=True
                while (flag!=False):
                    flag=False
                    plate_number=input("\nEnter your plate number: ").strip()
                    while plate_number.lower()!="end" and len(plate_number)!=10:
                         plate_number=input("invalid input! try again: ").strip()
                    if plate_number.lower()=="end":
                        break
                    for i in car_list:
                        if plate_number==i[4]:
                            print("This car is already in the parking lot!")
                            flag=True
                            break
                if plate_number.lower()=='end':
                        break
                name=input("Enter your name: ").strip()
                while name=='':
                    name=input("your name can't be empty! try again: ").strip()                    
                ID=input("enter your ID: ").strip()
                while ID.isdigit()==False or len(ID)!=10:
                         ID=input("invalid input! try again: ").strip()
                car_list.append([name,((((str(datetime.now())).split(' '))[0]).split('.'))[0]
                ,((str(datetime.now())).split(' '))[0],ID,plate_number])
    elif action=="2":
        if len(car_list)==0:
            print("Parking lot is empty!")
        else:
            plate_number='a'
            while plate_number.lower()!="end" and len(car_list)!=0:
                plate_number=input("\nEnter your plate number: ")
                for i in car_list:
                    flag=False
                    if plate_number==i[4]:
                        flag=True
                        temp=[]
                        for j in reversed(car_list):
                            if j!=i:
                                temp.append(car_list.pop())
                                continue
                            a=car_list.pop()
                            b=a.pop()
                            a+=[((str(datetime.now())).split(' '))[0],
                            ((((str(datetime.now())).split(' '))[0]).split('.'))[0],b]
                            dep_cars.append(a)
                            for k in range(len(temp)):
                                car_list.append(temp.pop())
                            break     
                        break
                if flag==False and plate_number.lower()!='end':
                    print("This car doesn't exist in the parking lot!")
    elif action=="3":
        if len(car_list)!=0:
            print(" Plate Number|  ID Number | Ent. Date | Ent. Time | Name")
            reports(car_list)
        if len(dep_cars)!=0:
            print(" Plate Number| ID Number  | Ent. Date  | Ent. Time  | Dep. Date  | Dep. Time  | Name")
            reports(dep_cars)
    elif action=="0":
        break
    else:
        print("Invalid input! Try again!")
#===========================================================
'''
L=-1
cstmr=[None]*20
from random import *
for i in range(10):
    if L==9:
        '''
        '''
        for j in reversed(range(len(cstmr))):
            if cstmr[j]!=None:
                cstmr=([None]*(20-len(cstmr[:j+1])))+cstmr[:j+1]
                L=(len(cstmr[:j+1])//2)+1
        '''
        '''
        while None in cstmr:
            cstmr.remove(None)
        L=(len(cstmr)//2)-1
        cstmr=([None]*(20-len(cstmr)))+cstmr
    name=input(f"Enter your name ({i+1}): ")
    ID=input(f"Enter your ID ({i+1}): ")
    L=randint(L+1,9)
    cstmr[(-L*2)+18:(-L*2)+20]=[name,ID]
print(cstmr)
'''
from random import *
P=-1
All=[None]*20
for i in range(10):
    if P==9:
        while None in All:
            All.remove(None)
        P=(len(All)//2)-1
        All=([None]*(20-len(All)))+All
    name=input("Name of costumer number {}: ".format(i+1)).strip()
    while name=="" or name.isalpha()==False:
        name=input("Your name cant be empty and must be alphabetic! try again: ").strip()
    ID=input("Enter your ID ({}): ".format(i+1)).strip()
    while len(ID)!=10 or ID.isdigit()==False:
        ID=input("Your ID must be 10 digits! Try again: ").strip()
    P=randint(P+1,9)
    All[(-P*2)+18:(-P*2)+20]=[name,ID]
counter=1
for i in reversed(range(0,len(All),2)):
    print(counter,All[i+1],All[i])
    counter+=1
