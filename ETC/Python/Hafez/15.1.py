from guizero import *
from os import *
def show():
    text.value='Welcome '+name.value+' !'
    button.bg='blue'
    #button._on_press
form=App(title='Test Form',width='1000',height='500',bg='gray',layout='grid')
text=Text(form,text='TEST PROGRAM! :)',grid=[0,0])
Text(form,'Enter your name: ',grid=[0,1],align='left')
name=TextBox(form,grid=[1,1])
button=PushButton(form,command=show,text='Submit!',grid=[0,2])
check1=CheckBox(form,text='ICDL',align='left',grid=[0,3])
check2=CheckBox(form,text='English',align='left',grid=[1,3])
combo=Combo(form,options=['Mashhad','Tehran','Shiraz'],grid=[0,4])
#piture=Picture(form,image='A.png',grid=[0,5])
group=ButtonGroup(form,options=[['Red','R'],['Green','G'],['Blue','B']],grid=[0,6])
slide=Slider(form,start='0',end='100',grid=[0,7])
form.display()
