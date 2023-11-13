from guizero import *
username='';password='';fnt='Times New Roman';items={};usr_ordr={}
def admn():
    root.hide()
    global User,Pass,admin
    admin=Window(root,'Admin Entrance',width=200,height=280)
    Text(admin,'\nUsername:',font='Times New Roman')
    User=TextBox(admin,width=20)
    Text(admin,'\nPassword:',font='Times New Roman')
    Pass=TextBox(admin,hide_text=True,width=20)
    Text(admin,'')
    PushButton(admin,check_up,text='Submit',width=10,height=1)
    Text(admin,'')
    PushButton(admin,lambda:[admin.hide(),root.show()],text='Back',width=10,height=1)
def check_up():
    global username,password,admin_win
    if User.value!=username or Pass.value!=password:
        admin.hide()
        warn('Incorrect','Username or Password is incorrect!')
        admin.show()
    else:
        admin.hide()
        admin_win=Window(admin,'Admin Section',width=220,height=230)
        Text(admin_win,f'\nWhat do you want to do?\n',size=16,font=fnt)
        PushButton(admin_win,edt,text='Edit Admin Info',width=10,height=1)
        PushButton(admin_win,add,text='Add Items',width=10,height=1)
        PushButton(admin_win,lambda:[admin_win.hide(),root.show()],text='Back',width=10,height=1)
def edt():
    global edit,usr_box,pss_box,pss2_box
    admin_win.hide()
    edit=Window(admin_win,'Edit',width=200,height=300)
    Text(edit,'\nUsername:',font=fnt)
    usr_box=TextBox(edit,width=20)
    Text(edit,'\nNew password:',font=fnt)
    pss_box=TextBox(edit,hide_text=True,width=20)
    Text(edit,'\nConfirm password:',font=fnt)
    pss2_box=TextBox(edit,hide_text=True,width=20)
    Text(edit,'\n')
    PushButton(edit,check,text='Done')
def check():
    global edit,username,password,usr_box,pss_box,pss2_box
    if usr_box.value.strip()=='':
        edit.hide()
        warn('Username','Username cannot be empty!')
        edit.show()
    elif (' ' in pss_box.value)==True or len(pss_box.value)<6:
        edit.hide()
        warn('Password','Password length must be greater than 6 and it cannot contain white space!')
        edit.show()
    elif pss2_box.value!=pss_box.value:
        edit.hide()
        warn('Confirm Password','Passwords you entered don\'t match!')
        edit.show()
    else:
        username=usr_box.value.strip()
        password=pss_box.value
        edit.destroy()
        info('Success','Profile changed successfully\nplease reenter')
        User.value=username
        Pass.value=password
        admin.show()
def add():
    global item_name,item_price,add_win
    admin_win.hide()
    add_win=Window(admin,'Add Items',width=180,height=220)
    Text(add_win,'\nName of the food',font=fnt)
    item_name=TextBox(add_win,width=20)
    Text(add_win,'\nPrice of the food',font=fnt,)
    item_price=TextBox(add_win,width=20)
    Text(add_win)
    box2=Box(add_win,layout='grid')
    PushButton(box2,item_check,text='Add',grid=[2,0],width=3,height=1)
    PushButton(box2,show_menu,text='Menu',grid=[1,0],width=3,height=1)
    PushButton(box2,lambda:[add_win.hide(),admin_win.show()],text='Back',grid=[0,0],width=3,height=1)
def item_check():
    if item_name.value.strip()=='':
        add_win.hide()
        warn('Food Name','Name of the item cannot be empty!')
        add_win.show()
    elif (item_name.value.strip() in items)==True:
        add_win.hide()
        warn('Food Name','This item already exists in the menu!')
        add_win.show()
    elif item_price.value.strip().isdigit()==False or int(item_price.value.strip())<=0:
        add_win.hide()
        warn('Food Price','Items price must be a positive number!')
        add_win.show()
    else:
        add_win.hide()
        info('Item Added',f'{item_name.value.strip()} was added to the menu successfully!')
        items[item_name.value.strip()]=int(item_price.value.strip())
        usr_btn.visible=True
        item_name.value=''
        item_price.value=''
        add_win.show()
def show_menu():
    if len(items)==0:
        add_win.hide()
        warn('Menu is empty','There is no item in the menu')
        add_win.show()
    else:
        add_win.hide()
        admin_menu=Window(add_win,'Menu',width=150,height=70*(len(items)+1))
        for i,j in items.items():
            Text(admin_menu,f'\n{i}\n{j} $',font=fnt)
        Text(admin_menu)
        PushButton(admin_menu,lambda:[admin_menu.hide(),add_win.show()],text='OK',width=5,height=1)
def usr():
    global usr_nam,order,itm_num,usr_win,back,paym,txt
    root.hide()
    usr_win=Window(root,'User',width=200,height=350)
    txt=Text(usr_win,'Enter your name',font=fnt)
    usr_nam=TextBox(usr_win,width=20)
    Text(usr_win,'\nYour orders',font=fnt)
    order=Combo(usr_win,items.keys())
    Text(usr_win,f'\nHow many do you want',font=fnt)
    itm_num=Slider(usr_win,start='1',end='10')
    Text(usr_win)
    PushButton(usr_win,ordr,text='Add to orders',width=8,height=1)
    Text(usr_win)
    back=PushButton(usr_win,lambda:[usr_win.hide(),root.show()],text='Back',width=8,height=1)
    paym=PushButton(usr_win,pay,visible=False,text='Pay',width=8,height=1)
def ordr():
    global l
    if usr_nam.value.strip()=='':
        usr_win.hide()
        warn('Name','Name cannot be empty!')
        usr_win.show()
    else:
        back.visible=False
        txt.visible=False
        usr_nam.visible=False
        paym.visible=True
        if (order.value in usr_ordr)==True and (usr_ordr[order.value]+itm_num.value)>10:
            usr_win.hide()
            warn('Invalid',f'You can order 10 of {order.value} at most!')
            usr_win.show()
        else:
            if (order.value in usr_ordr)==True:
                usr_ordr[order.value]+=itm_num.value
            else:
                usr_ordr[order.value]=itm_num.value
            usr_win.hide()
            info('Added',f'{itm_num.value} {order.value} added successfully!')
            usr_win.show()
def pay():
    global usr_mnu,usr_pay,summ
    usr_win.destroy()
    usr_mnu=Window(root,'Payment',width=250,height=60*len(usr_ordr)+200)
    summ=0
    for i,j in usr_ordr.items():
        Text(usr_mnu,f'\n{j} {i} => {items[i]} $ × {j} = {items[i]*j}',font=fnt)
        summ+=items[i]*j
    Text(usr_mnu,f'\n========================\nYour total: {summ} $\n\nEnter payment cost',font=fnt)
    usr_pay=TextBox(usr_mnu,width=20)
    Text(usr_mnu)
    PushButton(usr_mnu,done,text='Done',width=3,height=1)
def done():
    global usr_ordr
    usr_mnu.hide()
    if usr_pay.value==str(summ):
        info('Success',f'Payment was successful!\nEnjoy your meal {usr_nam.value}!')
        usr_ordr={}
        root.show()
    else:
        warn('Error','Payment declined! Try again')
        usr_mnu.show()
root=App('Food App',width=300,height=140)
Text(root,'\nWelcome to the Food  Ordering Application\n',font=fnt)
box=Box(root,layout='grid')
usr_btn=PushButton(box,usr,text='User (order)',visible=False,width=10,height=1,grid=[0,0])
PushButton(box,admn,text='Admin',width=10,height=1,grid=[1,0])
root.display()