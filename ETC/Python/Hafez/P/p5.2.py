while 1:
    so=input('Enter at least two sentences:\n\n')
    a=b=c=0
    for i in so:
        if i=='.':
            a+=1
        elif i=='!':
            b+=1
        elif i=='?':
            c+=1
    if a+b+c>=2:
        break
    print('Your input was less than two sentences!')
while 1:
    ui=input('\nMenu:\n\na) Sentences types\nb) Lowercases\nc) Uppercases\nd) Number of sentences\ne) Number of spaces\nf) Exit\n\nEnter a character from the menu: ')
    print()
    if ui=='a':
        print('Thre are',a,'declarative ,',b,'exclamatory and',c,'interrogative sentences in this paragraph')
    elif ui=='b':
        l=0
        for i in so:
            if i>='a' and i<='z':
                l+=1
        print('There are',l,'lowercase characters in this paragraph')
    elif ui=='c':
        u=0
        for i in so:
            if i>='A' and i<='Z':
                u+=1
        print('There are',u,'uppercase characters in this paragraph')
    elif ui=='d':
        print('There are',a+b+c,'sentences in this paragraph')
    elif ui=='e':
        s=0
        for i in so:
            if i==' ':
                s+=1
        print('There are',s,'spaces in this paragraph')
    elif ui=='f':
        print('Goodbye...!')
        break
    else:
        print('Wrong input!')
