from guizero import App, Text, PushButton , Box
displayString = ''
a = False
b = False
result = 0
operator = ''
operatorFlag = False
app = App(title='MyCalc', layout='grid', width=211, height=237)
def inputNumber(key):
    global displayString, operatorFlag
    if operatorFlag:
        displayString=''
        operatorFlag = False
    displayString = displayString + key
    display.value = displayString
def operatorKey(key):
    global a, operator, operatorFlag, displayString
    operator = key
    operatorFlag = True
    if not a:
        a = float(displayString)
def evaluate():
    global a, b, result, operator, displayString
    if not a and not b:
        return
    elif a and not b:
        b = float(displayString)
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        result = a / b
    elif operator == 'x':
        result = a * b
    # stop decimal places appearing for whole numbers
    if result - int(result) == 0:
        result = int(result)
    displayString = str(result)
    display.value = displayString
    a = result
def allClear():
    global a, b, operator, result, displayString
    a = 0
    b = 0
    operator = ''
    result = 0
    displayString = ''
    display.value = '0'
def backspace():
    global displayString
    if len(displayString) > 1:
        displayString = displayString[:-1]
        display.value = displayString
    else:
        displayString = ''
        display.value = '0'
Box0 = Box(app, grid=[0,0])
display = Text(Box0, text='0', size=18, height=2)
Box1 = Box(app, layout='grid', grid=[0,1])
btn7 = PushButton(Box1, command=inputNumber, args=['7'], text='7', grid=[0,0], width=2, height=1)
btn8 = PushButton(Box1, command=inputNumber, args=['8'], text='8', grid=[1,0], width=2, height=1)
btn9 = PushButton(Box1, command=inputNumber, args=['9'], text='9', grid=[2,0], width=2, height=1)
btn4 = PushButton(Box1, command=inputNumber, args=['4'], text='4', grid=[0,1], width=2, height=1)
btn5 = PushButton(Box1, command=inputNumber, args=['5'], text='5', grid=[1,1], width=2, height=1)
btn6 = PushButton(Box1, command=inputNumber, args=['6'], text='6', grid=[2,1], width=2, height=1)
btn1 = PushButton(Box1, command=inputNumber, args=['1'], text='1', grid=[0,2], width=2, height=1)
btn2 = PushButton(Box1, command=inputNumber, args=['2'], text='2', grid=[1,2], width=2, height=1)
btn3 = PushButton(Box1, command=inputNumber, args=['3'], text='3', grid=[2,2], width=2, height=1)
btn0 = PushButton(Box1, command=inputNumber, args=['0'], text='0', grid=[0,3,2,1], width=8, height=1)
btnDec = PushButton(Box1, command=inputNumber, args=['.'], text='.', grid=[2,3], width=2, height=1)

btnDiv = PushButton(Box1, command=operatorKey, args=['/'], text='÷', grid=[3,0], width=2, height=1)
btnMult = PushButton(Box1, command=operatorKey, args=['x'], text='x', grid=[3,1], width=2, height=1)
btnSub = PushButton(Box1, command=operatorKey, args=['-'], text='-', grid=[3,2], width=2, height=1)
btnAdd = PushButton(Box1, command=operatorKey, args=['+'], text='+', grid=[3,3], width=2, height=1)

btnEquals = PushButton(Box1, command=evaluate, text='=', grid=[4,2,1,2], width=2, height=4)
btnAC = PushButton(Box1, command=allClear, text='AC', grid=[4,0], width=2, height=1)
btnCE = PushButton(Box1, command=backspace, text='←', grid=[4,1], width=2, height=1)
app.display()

'''from multiprocessing import Process
from time import sleep
log=open('p12.1.txt','a+')
def LOG():
  for i in range(10):
    sleep(1)
    print(i+1)
  print ('func1: finished')
def main():
  for i in range(10):
    a=int(input(f'Yellow {i+1}: '))
  print (f'{a}:{i+1}\nfunc2: finished')
if __name__ == '__main__':
  p1 = Process(target=LOG)
  p1.start()
  p2 = Process(target=main)
  p2.start()
  p1.join()
  p2.join()
  '''
