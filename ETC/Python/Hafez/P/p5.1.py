so=input('Enter location of the file:\n\n')
c=-1
d=s=''
for i in so:
    if i=='\\':
        c+=1
for i in so[::-1]:
    if i!='.':
        s+=i
        continue
    break
for i in so:
    if i!=':':
        d+=i
        continue
    break
s=s[::-1]
print("Drive",d)
if c>=1:
    print(c,"foldrs")
if s=='txt':
    print(s,"is a simple text")
elif s=='docx':
    print(s,"is a word document")
elif s=='xlsx':
    print(s,"is an excel document")
#---------Alternative code---------
c=-1
for i in so:
    if i=='\\':
        c+=1
print("Drive",so[0])
if c>=1:
    print(c,"foldrs")
if so[-2]=='x':
    print("txt is a simple text")
elif so[-2]=='c':
    print("docx is a word document")
elif so[-2]=='s':
    print("xlsx is an excel document")
