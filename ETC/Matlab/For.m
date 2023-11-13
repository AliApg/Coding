clear all
close all
clc
%%
b=input('enter first num: ');
c=input('enter second num: ');
clc
a=b+round((c-b)*rand);
disp(['A random number between ',num2str(b),' and ' num2str(c),' is ',num2str(a)])