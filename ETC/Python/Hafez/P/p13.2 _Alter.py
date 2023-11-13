from guizero import *
ans=''
def push(x):
    global ans,buttonC
    if ((eval(x).text) in ['×','÷','=','Clear'])==False:
        buttonC.enabled=True
        eq.value+=eval(x).text
        ans+=eval(x).text
    elif eval(x).text=='×':
        buttonC.enabled=True
        eq.value+=eval(x).text
        ans+='*'
    elif eval(x).text=='÷':
        buttonC.enabled=True
        eq.value+=eval(x).text
        ans+='/'
    elif eval(x).text=='Clear':
        if len(eq.value)>0:
            eq.value=eq.value[:-1]
            ans=ans[:-1]
            if len(ans)==0:
                eval(x).enabled=False
        '''else:
            form.hide()
            warn('Clear','Calculating box is empty!')
            form.show()'''
    else:
        try:
            eq.value=eval(ans)
            ans=eq.value
        except:
            form.hide()
            error('Error','Wrong input!')
            form.show()
form=App(title='Calculator',width='225',height='368',bg='lightgray',layout='grid')
space1=Text(form,'\n',grid=[0,0],height='1')
eq=Text(form,'',width='24',grid=[0,1])
space2=Text(form,'\n',grid=[0,2],height='1')
box1=Box(form,layout='grid',grid=[0,3])
button1=PushButton(box1,push,args=['button1'],text='1',grid=[0,2],width='4',height='2')
button2=PushButton(box1,push,args=['button2'],text='2',grid=[1,2],width='4',height='2')
button3=PushButton(box1,push,args=['button3'],text='3',grid=[2,2],width='4',height='2')
button4=PushButton(box1,push,args=['button4'],text='4',grid=[0,1],width='4',height='2')
button5=PushButton(box1,push,args=['button5'],text='5',grid=[1,1],width='4',height='2')
button6=PushButton(box1,push,args=['button6'],text='6',grid=[2,1],width='4',height='2')
button7=PushButton(box1,push,args=['button7'],text='7',grid=[0,0],width='4',height='2')
button8=PushButton(box1,push,args=['button8'],text='8',grid=[1,0],width='4',height='2')
button9=PushButton(box1,push,args=['button9'],text='9',grid=[2,0],width='4',height='2')
button0=PushButton(box1,push,args=['button0'],text='0',grid=[1,3],width='4',height='2')
buttonO=PushButton(box1,push,args=['buttonO'],text='.',grid=[2,3],width='4',height='2')
buttonP=PushButton(box1,push,args=['buttonP'],text='+',grid=[3,0],width='4',height='2')
buttonS=PushButton(box1,push,args=['buttonS'],text='-',grid=[3,1],width='4',height='2')
buttonM=PushButton(box1,push,args=['buttonM'],text='×',grid=[3,2],width='4',height='2')
buttonD=PushButton(box1,push,args=['buttonD'],text='÷',grid=[3,3],width='4',height='2')
buttonC=PushButton(box1,push,args=['buttonC'],text='Clear',grid=[0,3],width='4',height='2',enabled=False)
buttonE=PushButton(form,push,args=['buttonE'],text='=',grid=[0,4],width='28',height='2')
form.display()
