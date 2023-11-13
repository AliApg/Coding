'''
import sqlite3 as db
import os

data=db.connect('Test.db')
cr=data.cursor()

a='0924978244'

cr.execute('drop table Entry')
cr.execute('drop table Storage')
cr.execute('drop table Users')
cr.execute('drop table Paid')
cr.execute(f'drop table "{a}"')

cr.execute(f'create table "{a}" (item text,amount int)')
cr.execute('create table Entry (username text,password text)')
cr.execute('create table Storage (name text,amount int,cost float)')
cr.execute('create table Users (ID text,firstname text,lastname text,gender text,age int,address text,items int,total float)')
cr.execute('create table Paid (ID text,firstname text,lastname text,gender text,age int,address text,items int,total float,trackingcode int)')

cr.execute('insert into Entry(username,password)values("admin","123456"),("ad","121212")')
cr.execute(f'insert into "{a}" (item,amount)values("Milk",12),("Bread",6)')
cr.execute('insert into Users(ID,firstname,lastname,gender,age,address,items,total)values("0924978244","Amir","Ata","Male",22,"Mashhad, Kowsar1",0,0)')
cr.execute(f'update "{a}" set amount=10 where amount=12')
data.commit()

cr.execute('select * from Entry')
print(cr.fetchall())
cr.execute('select * from Storage')
print(cr.fetchall())
cr.execute('select * from Users')
print(cr.fetchall())
cr.execute('select * from Paid')
print(cr.fetchall())
cr.execute(f'select * from "{a}"')
print(cr.fetchall())
os.system('pause')

a=[('a',),('b',)]
print(a)

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])
print(strike('123456'))

cr.execute('create table Entry (username text,password text)')
cr.execute('alter table Entry rename to Storage')
cr.execute('select * from Storage')
print(cr.fetchall())
'''
'''
cr.execute('drop table Users')
cr.execute('drop table Paid')
cr.execute('drop table "0924978244"')
cr.execute('create table "0924978244" (item text,amount int)')
cr.execute('create table Users (ID text,firstname text,lastname text,gender text,age int,address text,items int,total float)')
cr.execute('create table Paid (ID text,firstname text,lastname text,gender text,age int,address text,items int,total float,trackingcode int)')
cr.execute('insert into Users(ID,firstname,lastname,gender,age,address,items,total)values("0924978244","Amir","Ata","Male",22,"Iran, Mashhad, Vakilabad, Kowsar1, P 63, Floor 3",13,1358)')
cr.execute('insert into "0924978244"(item,amount)values("Milk",2),("Water",6),("Bread",5)')
storage_db.commit()

a=[('0924978244',), ('1212121212',)]
b=('0924978244',)
a.remove(('0924978244',))
print(a,type(a))
a+=[('distraction',)]
print(a,type(a))

from datetime import *
print(str(datetime.now()).split(" ")[1].split(".")[0])
'''

'''
print('Should I buy Galaxy Buds Pro?\n')
from random import randint
Yes=No=0
for i in range(0,1000000):
    x=randint(0,1000000)
    if x<(1000000/2):
        No+=1
    else:
        Yes+=1
if Yes>No:
    print('Yes:',Yes,'\nNo:',No)
else:
    print('No:',No,'\nYes:',Yes)
'''

'''
x=0
for i in [0.26,0.54,0.57,0.89]:
    x+=(1-i)
print(1-x)
'''
'''
for i in range(13,98,2):
    for j in range(13,98):
        if int(str(i)[::-1])==j and (i-j==27 or j-i==27):
            print('1st:',j,'\n2nd:',i,'\n')
'''


def time(sec):
    if str(sec).isdigit()==False:print('\n\aWrong input (Entry must be second)!\n')
    else:
        day=sec//(3600*24)
        sec=sec%(3600*24)
        hour=sec//3600
        sec=sec%3600
        minute=sec//60
        sec=sec%60
        p=f'\n{day} D\n{hour} Hr\n{minute} Min\n{sec} Sec\n'
        if day==0:
            p=p.replace('0 D\n','')
        if hour==0:
            p=p.replace('0 Hr\n','')
        if minute==0:
            p=p.replace('0 Min\n','')
        if sec==0:
            p=p.replace('\n0 Sec','')
        if p.strip()=='':
            p='\nZero!\n'
        print(p)

from os import system
from time import sleep
#ZS={}
#for i in range(int(input('Number of videos: '))): ZS[float(input('\nName: '))]=int(eval(input('Min: ')))*60+int(input('Sec: '));print('\n')

#ZS={1.0: 1154, 2.0: 2832, 3.0: 2774, 4.0: 2490, 5.1: 1623, 5.2: 1555, 6.1: 965, 6.2: 1850, 6.3: 1782, 6.4: 265,
#    7.0: 1651, 8.1: 1646, 8.2: 1565, 9.1: 1810, 9.2: 1554, 9.3: 992, 9.4: 1318, 10.0: 1472, 11.0: 1344, 12.0: 1827, 13.0: 1467}

ZS={1: 5625, 2: 5380, 6: 4801, 7: 5463, 8: 5050, 9: 7910, 10: 5484, 11: 5116, 12: 5220,
    13: 459, 14: 4589, 15: 5560, 16: 5616, 17: 4964, 18: 9530, 19: 6382, 20: 4799, 21: 8170}

sec_all=0
for i in ZS:
    sec_all+=ZS[i]

while True:
    try:
        seen=input('Input: ')
        seen=float(seen)
        if (seen in ZS) == False:
            print('\n\aOut of range!\n')
            continue
        else:
            sec_tot=0
            for i in ZS:
                if i<=seen:
                    sec_tot+=ZS[i]
                    continue
                break
            system('cls')
            print(f'\nProgress: {(sec_tot/sec_all)*100} %\n\nDone:')
            time(sec_tot)
            print('Left:')
            time(sec_all-sec_tot)
            system('pause')
            system('cls')
    except:
        if str(seen).lower()!='end': print('\n\aWrong input!\n')
        else:system('cls'); print('\nGood\abye! :)\n');sleep(3) ; break

        
