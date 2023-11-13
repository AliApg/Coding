from guizero import *
buttons={'button1': 1, 'button2': 2, 'button3': 3, 'button4': 4,
             'button5': 5, 'button6': 6, 'button7': 7, 'button8': 8,
             'button9': 9, 'button0': 0, 'buttonO': 11, 'buttonP': 12,
             'buttonS': 13, 'buttonM': 14, 'buttonD': 15, 'buttonE': 16}
def highlight():
    global x
    x.bg='lightblue'
def leaves():
    global x
    x.bg='gray'
def enter():
    for i in buttons:
        try:
            #global vars()[i]
            if vars()[i].value==1:
                eq.value=buttons[i]
                break
        except:
            print(i,type(i))
            eq.value='Error!!!!! '
global button1
form=App(title='Calculator',width='226',height='310',bg='gray',layout='grid')
space1=Text(form,'\n',grid=[0,0],height='1')
eq=Text(form,'Hi my name is Amirata Yazdani',width='24',grid=[0,1])
space2=Text(form,'\n',grid=[0,2],height='1')
box1=Box(form,layout='grid',grid=[0,3])
button1=PushButton(box1,enter,text='1',grid=[0,2],width='4',height='2')
"""button1.when_mouse_enters=highlight()
button1.when_mouse_moved=highlight()
button1.when_mouse_leaves=leaves()
button1.when_left_button_pressed=highlight()
button1.when_left_button_released=leaves()"""
button2=PushButton(box1,text='2',grid=[1,2],width='4',height='2')
button3=PushButton(box1,text='3',grid=[2,2],width='4',height='2')
button4=PushButton(box1,text='4',grid=[0,1],width='4',height='2')
button5=PushButton(box1,text='5',grid=[1,1],width='4',height='2')
button6=PushButton(box1,text='6',grid=[2,1],width='4',height='2')
button7=PushButton(box1,text='7',grid=[0,0],width='4',height='2')
button8=PushButton(box1,text='8',grid=[1,0],width='4',height='2')
button9=PushButton(box1,text='9',grid=[2,0],width='4',height='2')
button0=PushButton(box1,text='0',grid=[1,3],width='4',height='2')
buttonO=PushButton(box1,text='.',grid=[2,3],width='4',height='2')
buttonP=PushButton(box1,text='+',grid=[3,0],width='4',height='2')
buttonS=PushButton(box1,text='-',grid=[3,1],width='4',height='2')
buttonM=PushButton(box1,text='×',grid=[3,2],width='4',height='2')
buttonD=PushButton(box1,text='÷',grid=[3,3],width='4',height='2')
buttonE=PushButton(box1,text='=',grid=[0,3],width='4',height='2')
for i in buttons:
    global x
    x=vars()[i]
    '''
    vars()[i].when_clicked=highlight
    vars()[i].when_left_button_released=leaves
    '''
    print(vars()[i].when_clicked)
    if vars()[i].when_clicked!=None:
        vars()[i].when_left_button_pressed=highlight
        vars()[i].when_left_button_released=leaves
        break
form.display()
