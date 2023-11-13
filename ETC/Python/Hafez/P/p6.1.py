while 1:
    a=int(input('Enter a number: '))
    if a>=2:
        f=[1,1]
        for i in range(a-2):
            f+=[f[i]+f[i+1]]
        print('The first ',a,' sentences of the fibonacci series are:\n',f,sep='')
        #break
    else:
        print('Your number can not be lower than 2!')
