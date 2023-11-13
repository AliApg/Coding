from guizero import *
usr='Admin';pss='123456';clr='cyan';bclr='gray';name='Amitata Yazdani';ID='0924978244';sz=16;fnt='Times New Roman'
def highlight_user():
    User.bg='lightblue'
def leaves_user():
    User.bg='white'
def highlight_pass():
    global x
    x.bg='lightblue'
def leaves_pass():
    global x
    x.bg='white'
def check():
    global edit,usr,pss,clr,bclr,name,ID,sz,fnt,usr_box,pss_box,name_box,ID_box,sz_box,fnt_box,txt_clr_box,bg_clr_box,pss2_box
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
    elif name_box.value.strip()=='' or (name_box.value.replace(' ','')).isalpha()==False:
        edit.hide()
        warn('Name','Name cannot be empty and it must be alphabetic!')
        edit.show()
    elif ID_box.value.isdigit()==False or len(ID_box.value)!=10:
        edit.hide()
        warn('ID','ID must be a 10 digit number!')
        edit.show()
    elif (sz_box.value.strip()).isdigit()==False:
        edit.hide()
        warn('Text size','Text size must be a possetive integer number!')
        edit.show()
    elif fnt_box.value.strip()=='' or (fnt_box.value.strip()).isdigit()==True:
        edit.hide()
        warn('Font','Invalid font!')
        edit.show()
    else:
        try:
            Text(root,'color',color=bg_clr_box.value.strip(),visible=False)
        except:
            edit.hide()
            warn('Background color','This color does not exist!')
            edit.show()
            return
        try:
            Text(root,'color',color=txt_clr_box.value.strip(),visible=False)
            if txt_clr_box.value.strip()==bg_clr_box.value.strip():
                edit.hide()
                warn('Text color','Text color cannot be same as background color!')
                edit.show()
                return
        except:
            edit.hide()
            warn('Text color','This color does not exist!')
            edit.show()
            return
        usr=usr_box.value.strip()
        pss=pss_box.value
        clr=txt_clr_box.value.strip()
        bclr=bg_clr_box.value.strip()
        name=name_box.value.strip()
        ID=ID_box.value.strip()
        sz=int(sz_box.value.strip())
        fnt=fnt_box.value.strip()
        edit.destroy()
        info('Success','Profile changed successfully\nplease reenter')
        User.value=usr
        Pass.value=pss
        root.show()
def edt():
    global edit,usr_box,pss_box,name_box,ID_box,sz_box,fnt_box,txt_clr_box,bg_clr_box,pss2_box
    window.hide()
    edit=Window(window,'Edit',width=200,height=680)
    Text(edit,'\nUsername:',font='Times New Roman')
    usr_box=TextBox(edit,width=20)
    Text(edit,'\nNew password:',font='Times New Roman')
    pss_box=TextBox(edit,hide_text=True,width=20)
    Text(edit,'\nConfirm password:',font='Times New Roman')
    pss2_box=TextBox(edit,hide_text=True,width=20)
    Text(edit,'\nName:',font='Times New Roman')
    name_box=TextBox(edit,width=20)
    Text(edit,'\nID:',font='Times New Roman')
    ID_box=TextBox(edit,width=20)
    Text(edit,'\nSize:',font='Times New Roman')
    sz_box=TextBox(edit,width=20)
    Text(edit,'\nFont:',font='Times New Roman')
    fnt_box=TextBox(edit,width=20)
    Text(edit,'\nBackground color:',font='Times New Roman')
    bg_clr_box=TextBox(edit,width=20)
    Text(edit,'\nText color:',font='Times New Roman')
    txt_clr_box=TextBox(edit,width=20)
    Text(edit,'\n')
    PushButton(edit,check,text='Done')
def check_up():
    global usr,pss,window
    if User.value!=usr or Pass.value!=pss:
        root.hide()
        warn('Incorrect','Username or Password is incorrect!')
        root.show()
    else:
        root.hide()
        window=Window(root,'User info',width=220,height=230,bg=bclr)
        win_txt=Text(window,f'\nUsername: {usr}\nPassword: {pss}\nName: {name}\nID= {ID}\nSize: {sz}\n',color=clr,size=sz,font=fnt)
        ed_btn=PushButton(window,edt,text='Edit')
root=App('User Menu',width=200,height=220)
Text(root,'\nUsername:',font='Times New Roman')
User=TextBox(root,width=20)
Text(root,'\nPassword:',font='Times New Roman')
Pass=TextBox(root,hide_text=True,width=20)
Text(root,'')
User.when_mouse_enters=highlight_user
User.when_mouse_leaves=leaves_user
x=Pass
Pass.when_mouse_enters=highlight_pass
Pass.when_mouse_leaves=leaves_pass
'''for i in [User,Pass]:
    x=i
    i.when_mouse_enters=highlight_pass
    i.when_mouse_leaves=leaves_pass'''
PushButton(root,check_up,text='Submit')
Text(root,'')
root.display()