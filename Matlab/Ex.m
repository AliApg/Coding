clc
clear all
close all
%%
d=input('Enter amount of numerical error: ');
d=1/2*10^(-d);
clc
x=input('Enter amount of x in the equation  " e^x= 1+x/1!+...+(x^n)/n! " : ');
clc
n=0;a=1/3;f=1;
while  f>=d
    
    f=(x^(n))/factorial(n); %f=exp^x
    n=n+1;a=a+f;
end
disp(['In the equation  "e^',num2str(x),'=1+',num2str(x),'/1!+...+',...
num2str(x),'^n/n!"  n>=',num2str(n-1),' and e^',num2str(x),'=',num2str(1+a)])