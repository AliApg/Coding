def M_list(x):
    o=0
    print('\n===============',x,'===============',sep='')
    for k in storage:
        o+=1
        strg_key.append(k)
        print(o,'. ',k,'\t',storage[k],sep='')
    print('======================================\n')
inp='';i=0;storage={};all_usr=[];strg_key=[];hlp=0;  YES=id_num=0  #Unnecessary?!!!!!!!!!!!!!
from os import *
while inp!='3':
    print()
    system('pause')
    system('cls')
    inp=input('=============ACCESS LEVEL=============\n1. Admin\n2. User\n3. Exit\n\nChoose: ')
    if inp=='1':#ADMIN
        system('cls')
        adminp=input('\n================ADMIN================\n1. Add items\n2. Edit previous data\n3. Data report\n4. Order low items\n\nChoose: ')
        while adminp!='1' and adminp!='2' and adminp!='3' and adminp!='4':
            adminp=input('\n\7Wrong input!\n\nChoose again: ')
        if adminp=='1':#ADMIN: Add items
            system('cls')
            name=input('\nEnter item {} name: '.format(i+1))
            while name.lower()!='end':
                avl=input('Enter availability of {}: '.format(name))
                if avl.isdigit()==False or int(avl)<0:
                    print('\n\7Availability must be integer and it cannot be negetive!\n')
                    continue
                storage[name]=int(avl)
                i+=1
                name=input('\nEnter item {} name: '.format(i+1))
        elif len(storage)<=0:
             print('\n\7There is no item!\nPlease add items first')
        elif adminp=='2':#ADMIN: Edit previous data
            system('cls')
            strg_key=[]
            edit=input('\n==============ADMIN:EDIT==============\n1. Edit availability of items\n2. Delete items\n\nChoose: ')
            while edit!='1' and edit!='2':
                edit=input('\n\7Wrong input!\nChoose again: ')
            if edit=='1':#ADMIN: Edit previous data: Change cost
                system('cls')
                M_list('THE LIST')
                ed=input('Choose number of the item you want to change: ')
                while ed.lower()!='end':
                    while ed.lower()!='end' and(int(ed)<=0 or int(ed)>len(strg_key)):
                        ed=input('\n\7Wrong input!\n\nChoose again: ')
                    if ed.lower()=='end':
                        continue
                    edcst=int(input('Enter new availability for {}: '.format(strg_key[int(ed)-1])))
                    while edcst<0:
                        edcst=int(input('\n\7Availability cannot be negetive!\n\nTry again: '))
                    storage[strg_key[int(ed)-1]]=edcst
                    ed=input('\nChoose another item to change: ')
                M_list('NEW LIST')
            else:#ADMIN: Edit previous data: Delete
                system('cls')
                M_list('THE LIST')
                dlt=input('Choose number of the item you want to delete: ')
                while dlt.lower()!='end':
                    while dlt.lower()!='end' and(int(dlt)<=0 or int(dlt)>len(strg_key)):
                        dlt=input('\n\7Wrong input!\n\nChoose again: ')
                    if dlt.lower()=='end':
                        continue
                    i-=1
                    storage.pop(strg_key[int(dlt)-1])
                    M_list('NEW LIST')
                    dlt=input('Choose another item to delete: ')
        elif adminp=='3':#ADMIN: Data report
            system('cls')
            rpth={};rptm={};rptl={}
            for j in storage:
                if storage[j]<=10:
                    rptl[j]=storage[j]
                elif storage[j]<=50:
                    rptm[j]=storage[j]
                else:
                    rpth[j]=storage[j]
            if len(rptl)>0:
                print('\nLow availability items:')
                for j in rptl:
                    print(j,'\t',rptl[j])
            if len(rptm)>0:
                print('\nMid availability items:')
                for j in rptm:
                    print(j,'\t',rptm[j])
            if len(rpth)>0:
                print('\nHigh availability items:')
                for j in rpth:
                    print(j,'\t',rpth[j])
        else:#ADMIN: Order low items
            system('cls')
            s=0
            for j in storage:
                if storage[j]<=5:
                    s+=1
                    addstrg=int(input('{} is low in storage please order some!\nHow much you want to add to {} (current: {})? '.format(j,j,storage[j])))
                    while addstrg<0:
                        addstrg=int(input('\nAddition cannot be negetive!\nTry again: '))
                    storage[j]+=addstrg
            if s==0:
                print('\nAvailability of the items is good')
    elif inp=='2':#USER
        system('cls')
        if len(storage)<=0:
             print('\n\7There is no item!\nPlease add items in admin section first')
        else:
            usinp=input('\n================USER================\n1. Order\n2. Users report\n\nChoose: ')
            while usinp!='1' and usinp!='2':
                usinp=input('\n\7Wrong input!\nChoose again: ')
            if usinp=='1': #User order
                system('cls')
                hlp=1
                exist=''
                usr_name=input('\nEnter your name: ')
                while exist!='yes': #Check for existing id
                    idk=0
                    id_num=input('Enter your identification code: ')
                    for y in range(len(all_usr)):
                        if id_num==all_usr[y][1]:
                            exist=input('\n\7This identification code is already exist!\n\nDo you want to continue? (yes/ press any key to try another id) ')
                            YES=y
                            break
                        else:
                            idk+=1
                    if len(id_num)!=10:
                        print('\n\7Identification code must contain 10 digits!\n')
                    elif idk==len(all_usr):
                        break
                strg_key=[]
                M_list('THE LIST')
                if exist=='yes':#Existing user
                    all_usr[YES][0]=usr_name
                    if all_usr[YES][2]==20:
                        print('\n\7You already ordered 20 items!\n')
                    else:
                         select=input('Choose number of the item you want: ')
                         while select.lower()!='end' and all_usr[YES][2]!=20:
                            while select.lower()!='end' and(int(select)<=0 or int(select)>len(strg_key)):
                                select=input('\n\7Wrong input!\n\nChoose again: ')
                            if select.lower()=='end':
                                continue
                            selnum=int(input('Enter number of {} you want: '.format(strg_key[int(select)-1])))
                            while selnum<0 or selnum+all_usr[YES][2]>20 or selnum>storage[strg_key[int(select)-1]]:
                                if  selnum<0:
                                    print('\n\7This number cannot be negetive!\n\nTry again: ',end='')
                                elif  selnum>storage[strg_key[int(select)-1]]:
                                    print('\n\7There is',storage[strg_key[int(select)-1]],strg_key[int(select)-1],'left!\n\nTry again: ',end='')
                                else:   #elif  selnum+usr[2]>20:
                                    print('\n\7You cannot order more than 20 items! (current: ',all_usr[YES][2],')\n\nTry again: ',sep='',end='')                            
                                selnum=int(input())
                            storage[strg_key[int(select)-1]]-=selnum
                            all_usr[YES][2]+=selnum
                            all_usr[YES]+=[strg_key[int(select)-1],selnum]
                            if all_usr[YES][2]==20:
                                continue
                            select=input('\nChoose another item: ')
                else:#New user's order
                    usr=[usr_name,id_num,0]
                    select=input('Choose number of the item you want: ')
                    while select.lower()!='end' and usr[2]!=20:
                        while select.lower()!='end' and(select.isdigit()==False or int(select)<=0 or int(select)>len(strg_key)):
                            select=input('\n\7Wrong input!\n\nChoose again: ')
                        if select.lower()=='end':
                            continue
                        selnum=int(input('Enter number of {} you want: '.format(strg_key[int(select)-1])))
                        while selnum<0 or selnum+usr[2]>20 or selnum>storage[strg_key[int(select)-1]]:
                            if  selnum<0:
                                print('\n\7This number cannot be negetive!\n\nTry again: ',end='')
                            elif  selnum>storage[strg_key[int(select)-1]]:
                                print('\n\7There is ',storage[strg_key[int(select)-1]],strg_key[int(select)-1],'left!\n\nTry again: ',end='')
                            else:   #elif  selnum+usr[2]>20:
                                print('\n\7You cannot order more than 20 items! (current: ',usr[2],')\n\nTry again: ',sep='',end='')                            
                            selnum=int(input())
                        storage[strg_key[int(select)-1]]-=selnum
                        usr[2]+=selnum
                        usr+=[strg_key[int(select)-1],selnum]
                        if usr[2]==20:
                            continue
                        select=input('\nChoose another item: ')
                    all_usr.append(usr)
            else: #User report
                system('cls')
                if hlp==0:
                    print('\n\7There is no user yet!\nOrder first...')
                else:
                    o=0
                    print('\n============CURRENT USERS============\n')
                    for u in all_usr:
                        o+=1
                        print(o,'. ',u[0],sep='')
                    usrpt=int(input('\nChoose: '))
                    while usrpt<=0 or usrpt>len(all_usr):
                        usrpt=input('\n\7Wrong input!\nChoose again: ')
                    print("\n",all_usr[usrpt-1][0],"'s identification code: ",all_usr[usrpt-1][1],sep='',end='\n=====================================\n')
                    for u in range(3,len(all_usr[usrpt-1]),2):
                        print(all_usr[usrpt-1][u],'\t',all_usr[usrpt-1][u+1])
                    print("=====================================\n",all_usr[usrpt-1][0]," ordered ",all_usr[usrpt-1][2],' items in total',sep='')
    elif inp=='3':
        system('cls')
        print('Goodbye!\n\7')
    else:
        print('\n\7Wrong input try number 1 to 3')
system('pause')
