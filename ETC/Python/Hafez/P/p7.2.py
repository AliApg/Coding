'''
while (user!='system' or pas!=123) and r!=5:
    user=input('Enter username: ')
    pas=int(input('Enter password: '))
    r+=1
'''
#-------------------------------------------------------------------------------------
from random import randint
def u_in():
    print('\n================================\nList of items\n')
    for j in range(2,len(menu)+1,2):
        print(j//2,'. ',menu[j-2],'\t',menu[j-1],sep='')
    print('\n================================\n\nEnter number of the product you want to purchase\n')
    global k
    k=0
    user_input=''
    while True:
        user=[]
        user_input=input('Item {}: '.format(k+1))
        if user_input=='end':
            break
        elif int(user_input)<=0 or int(user_input)>(len(menu)//2):
            print("\nItem number is'nt in the range\n")
            continue
        user.append(menu[(int(user_input)-1)*2])
        user.append(menu[((int(user_input)-1)*2)+1])
        total.append(user)
        k+=1
def print_list(pl):
    global final_cost
    final_cost=0
    for j in range(len(pl)):
        print(j+1,'. ',pl[j][0],'\t',pl[j][1],sep='')
        final_cost+=total[j][1]
    print('\nYour cheapest purchase:',pl[0][0],'\t',pl[0][1],'\nYour most expensive purchase: ',pl[-1][0],'\t',pl[-1][1]
                              ,'\n\n================================\nYour total cost is: ',final_cost,'\n================================')
#===========================================================================================================================================
total=[];order=tuple()  #Why?!!!!!!!!!!!!!!!!
r=s=0;menu=[]
#===========================================================================================================================================
while r!=5:
    user=input('Enter username: ')
    pas=input('Enter password: ')
    if pas!='123' or user!='system':
        print('\nWrong username or password!\n')
        r+=1
        continue
    break
if r==5:
    print('\n5 incorrect attempts\n\nSystem is locked!')
else:
    while True:
        level=input('\nEner your access level (admin / user / exit): ')
        while level!='admin' and level!='user' and level!='exit':
            level=input('\nWrong input!\n\nEnter your access level (admin / user) again: ')
        if level=='admin':
            ac=input('\n1. Creat a list \n2. Modify previous list\n\nChoose: ')
            while ac!='1' and ac!='2':
                ac=input('\nWrong input!\n\nChoose again: ')
            if ac=='1':
                i=0;menu=[]
                menu.append(input('\nEnter name of the product {}: '.format(1)))
                while menu[-1]!='end':
                    cost=float(input('Enter the cost of product {}: '.format(i+1)))
                    while cost<=0:
                        cost=float(input('\nCost must be above 0!\n\nEnter the cost of product {} again: '.format(i+1)))
                    menu.append(cost)
                    menu.append(input('\nEnter name of the product {}: '.format(i+2)))
                    i+=1
                del menu[-1]
            elif len(menu)>0:
                print('\n================================\nPreviously made list\n')
                for j in range(2,len(menu)+1,2):
                    print(j//2,'. ',menu[j-2],'\t',menu[j-1],sep='')
                select=int(input('\n================================\n\n1. Modify products\n2. Add products\n3. Delete products\nChoose: '))
                while select!=1 and select!=2 and select!=3:
                    select=int(input('\nWrong input!\n\nChoose again: '))
                if select==1:
                    edit=int(input('\nEnter number of the product you want to modify: '))
                    while edit<=0 or edit>(len(menu)//2):
                        edit=int(input("\nProduct number is'nt in the range\n\nEnter the product you want to modify again: "))
                    menu[(edit-1)*2]=input('\nEnter name of the new product {}: '.format(edit))
                    cost=float(input('Enter the new cost of product {}: '.format(edit)))
                    while cost<=0:
                        cost=float(input('Cost must be above 0!\n\nEnter the new cost of product {} again: '.format(edit)))
                    menu[((edit-1)*2)+1]=cost
                elif select==2:
                    menu.append(input('\nEnter name of the product {}: '.format((len(menu)//2)+1)))
                    cost=float(input('Enter the cost of product {}: '.format((len(menu)//2)+1)))
                    while cost<=0:
                        cost=float(input('\nCost must be above 0!\n\nEnter the cost of product {} again: '.format(len(menu)+1)))
                    menu.append(cost)
                else:
                    delete=int(input('\nEnter number of the product you want to delete: '))
                    while delete<=0 or delete>(len(menu)//2):
                        delete=int(input("\nProduct number is'nt in the range\n\nEnter the product you want to delete again: "))
                    #del menu[(delete-1)*2:((delete-1)*2)+1]
                    del menu[(delete-1)*2]
                    del menu[(delete-1)*2]
            else:
                print('\nYou must creat a list first!')
        elif level=='user':
            if len(menu)>0:
                command=input('\n1. New order\n2. Last order details\n\nChoose: ')
                while command!='1' and command!='2':
                    command=input('\nWrong input!\n\nChoose again: ')
                if command=='1':
                    total=[]
                    u_in()
                    answer=''
                    while answer!='yes':
                        print('\nYou have selected',k,'items.\n\nPurchases sorted from cheap to expensive\n')
                        for x in range(len(total)-1):
                            for y in range(len(total)-1):
                                if total[y][1]>total[y+1][1]:
                                    temp=total[y]
                                    total[y]=total[y+1]
                                    total[y+1]=temp
                        print_list(total)
                        answer=input('\nIs your order correct? (yes / no) ')
                        if answer=='no':
                            total=[]
                            u_in()
                            continue
                        elif answer!='yes':
                            print('\nWrong input!\nPlease enter yes or no')
                            continue                                                                
                    address=input('\nEnter your address:\n')
                    code=randint(1000000000000000,9999999999999999)
                    print('\nYour tracking code is: ',code)
                    order=tuple(total)+(address,code)
                    s=1
                elif command=='2':
                    if s==0:
                        print('\nThere is no previous order!\nPlease order and then try again')
                        continue
                    print('Your previous order\n')
                    print_list(total)
                    print('\nYour address\n',order[-2],'\n\nYour tracking code: ',order[-1],sep='')
                else:
                    print('\n\nWrog input!')
            else:
                print('\nThere is no list! Creat a list in admin level.')
        else:
            print('\nEXIT!')
            break
