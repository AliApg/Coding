from guizero import *
f=1; n=0
pics=['1.png','2.png','3.png','4.png','5.png','6.png']   #,'7.png'
def nxt():
    global n
    n+=1
    if n==len(pics):
        n=0
    root.destroy()
def pre():
    global n
    n-=1
    if n==-1:
        n=len(pics)-1
    root.destroy()
def check():
    global box,add_window
    x=box.value.strip()
    if not(len(x)>4 and x[-4:]=='.png'):
        x+='.png'
    if (x in pics):
        add_window.hide()
        warn('Existing picture','This picture is already in the gallery!')
        add_window.show()
    else:
        try:
            Picture(root,image=x,visible=False)
            add_window.hide()
            info('Added',f'Picture "{x}" was added to gallery successfully!')
            box.value='         (Name of Picture)'
            add_window.show()
            pics.append(x)
        except:
            add_window.hide()
            error('Not found','This picture doesn\'t exist!')
            add_window.show()
def add():
    global box,add_window
    root.hide()
    add_window=Window(root,'Adding Picture To The List',height=300,width=420,bg='gray')
    Text(add_window,'\n\nEnter the name of the picture you want to add to gallery:\n\n')
    box=TextBox(add_window,'         (Name of Picture)',width=25)
    Text(add_window,'\n')
    PushButton(add_window,check,text='Submit')
    Text(add_window,'')
    PushButton(add_window,end,text='Back')
def end():
    add_window.destroy()
    root.show()
def dest():
    global f
    f=0
    root.destroy()
while f==1:
    root=App('Pictures',height=870,width=1350,bg='lightgray')
    pic=Picture(root,image=pics[n],align='top')
    Text(root)
    box=Box(root,layout='grid')
    button1=PushButton(box,pre,text='Previous Picture',grid=[0,0],width=20)
    button2=PushButton(box,nxt,text='Next Picture',grid=[2,0],width=20)
    button4=PushButton(box,add,text='Add a Pictures',grid=[1,0],width=20)
    button3=PushButton(root,dest,text='End',width=15)
    root.display()
