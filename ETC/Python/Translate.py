import os

import pyperclip

while True:
    os.system('cls')
    text = ''

    a = input('Enter text (type end to submit):\n')
    while a.upper() != 'END':
        text += f'{a} '
        a = input('\nEND?!   ')

    os.system('cls')
    out = text.replace('\n', ' ')

    pyperclip.copy(out)
    # print(out, '\n\n')
    # os.system('pause')
